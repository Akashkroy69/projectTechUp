import fitz  # PyMuPDF
import re
import pandas as pd

from PIL import Image, ImageEnhance
import pytesseract
from pdf2image import convert_from_path
import os

def enhance_image_contrast(image, factor=2.0):
    """
    Enhances the contrast of an image.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def extract_pdf_data_with_contrast(pdf_path):
    # Define patterns to capture specific fields
    patterns = {
        "Sheriff Sale Number": re.compile(r"SHERIFF\s*SALE\s*#:\s*[0-9\n]*(?=\n*|TAX PARCEL ID:)"),
        "Tax Parcel ID": re.compile(r"(TAX\s*PARCEL\n[0-9]|TAX\s*PARCEL\s*ID:)\s*[0-9A-Z-\n]*(?=\n*|CURRENT)"),
        # "Current Record Holder": re.compile(r"Current\s+RECORD(?:\s*\n*)*holder:\s*[A-Z]([\s\S]*?)(?=\n*|DEFENDANT IN FIFA:)", re.IGNORECASE),
        "Current Record Holder": re.compile(r"CURRENT\n*(\s*(?:—|-)\s*)*\s*\n*(RECORD|)(?:\s*\n*[0-9]*)*(?:HOLDER|SHAW __AT-)\s*(.*|\n*HOLDER):\s*([\s\S]*?)(?=\n{2,}|DEFENDANT IN FIFA:)"),
        # "Defendant in FIFA": re.compile(r"DEFENDANT[\s_\n]*IN[\s_\n]*\n*FIFA:\s*([\s\S]*?)(?=\n*|AMOUNT DUE:)", re.IGNORECASE),
        "Defendant in FIFA": re.compile(r"DEFENDANT[\s_\n]*IN[\s_]*FIFA:\s*([\s\S]*?)(?=\n{2,}|AMOUNT DUE:)", re.DOTALL|re.IGNORECASE),
        "Amount Due": re.compile(r"(AMOUNT\n[0-9]*|AMOUNT[\s_\n]*DUE:)\s*\$([\d\.,]+)"),
        "Tax Years Due": re.compile(r"TAX YEARS DUE:\s*[\d, \n]+(?=\n*|DEED)"),
        "Deed Book and Page": re.compile(r"DEED[\s_]*BOOK:\s*([\d/, \n]+)"),
        "Legal Description": re.compile(r"LEGAL[\s\n_]*DESCRIPTION:\s*([\s\S]*?)(?=#|SHERIFF)")
    }

    # Convert PDF to images
    pages = convert_from_path(pdf_path, dpi=300)
    data = []

    entry = {"Sheriff Sale Number": {},
             "Tax Parcel ID": {},
             "Current Record Holder": {},
             "Defendant in FIFA": {},
             "Amount Due": {},
             "Tax Years Due": {},
             "Deed Book and Page": {},
             "Legal Description": {}}

    # Process each page
    text = ""
    for page_num, page_image in enumerate(pages):
        # Enhance contrast to make light text darker`
           enhanced_image = enhance_image_contrast(page_image, factor=2.0)

        # Apply OCR
           print('Fetching page number: ', page_num)
           text = text + pytesseract.image_to_string(enhanced_image)

    text1 = text
    # Extract data using regex patterns
    print('Extracting the required data from the text ... ')
    for key, pattern in patterns.items():
        print('Key: ', key)

        # Find the pattern in the text using regex
        match = pattern.finditer(text1)

        # Obtain the required text and save it into data frame
        match_length = 0
        number_of_entries_saved = len(entry[key])
        for i in match:
            match_length = match_length + 1
            try:
                val = i.group().split(":")[1].replace("\n", " ")
            except:
                val = i.group().split("\n")[1].replace("\n", " ")

            # Append the prefix number of sheriff sale number. This is distorted in the extracted text.
            # Note that this prefix is same for all the sale number in the provided pdf.
            if key == "Sheriff Sale Number":
                if "1124" not in val:
                    val = "1124" + val
            
            # For text data remove the special characters such as _, - etc
            if key == "Current Record Holder" or key == "Defendant in FIFA" or key == "Legal Description":
                val = val.replace("-", "")
                val = val.replace("_", "")
            
            # Remove the text "current" in the tax parcel id.
            if key == "Tax Parcel ID":
                val = val.replace("CURRENT", "")

            entry[key][number_of_entries_saved + match_length] = val

        print('Number of occurrences in text: ', match_length)

    # Convert to DataFrame and save to Excel
    df = pd.DataFrame(entry)
    return df

# Usage
pdf_path = r"C:\Users\Lenovo\OneDrive\Desktop\TechUp\python_codeTogether\Advertisement.pdf"  # Replace with your PDF file path
df = extract_pdf_data_with_contrast(pdf_path)

# Save to Excel
df.to_excel("extracted_sheriff_sales_info.xlsx", index=False)
print("Data extraction complete and saved to 'extracted_sheriff_sales_info.xlsx'.")