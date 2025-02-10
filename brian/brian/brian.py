import re
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def enhance_image_contrast(image, factor=2.0):
    """
    Enhances the contrast of an image.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def extract_pdf_data_with_contrast(pdf_path):
    """
    Extracts data from a PDF using OCR and regex patterns.
    """
    # Define patterns to capture specific fields
    patterns = {
        "Sheriff Sale Number": re.compile(r"SHERIFF\s*SALE\s*#:\s*[0-9\n]*(?=\n*|TAX PARCEL ID:)"),
        "Tax Parcel ID": re.compile(r"(TAX\s*PARCEL\n[0-9]|TAX\s*PARCEL\s*ID:)\s*[0-9A-Z-\n]*(?=\n*|CURRENT)"),
        "Current Record Holder": re.compile(r"CURRENT\n*(\s*(?:—|-)\s*)*\s*\n*(RECORD|)(?:\s*\n*[0-9]*)*(?:HOLDER|SHAW __AT-)\s*(.*|\n*HOLDER):\s*([\s\S]*?)(?=\n{2,}|DEFENDANT IN FIFA:)"),
        "Defendant in FIFA": re.compile(r"DEFENDANT[\s_\n]*IN[\s_]*FIFA:\s*([\s\S]*?)(?=\n{2,}|AMOUNT DUE:)", re.DOTALL | re.IGNORECASE),
        "Amount Due": re.compile(r"(AMOUNT\n[0-9]*|AMOUNT[\s_\n]*DUE:)\s*\$([\d\.,]+)"),
        "Tax Years Due": re.compile(r"TAX YEARS DUE:\s*[\d, \n]+(?=\n*|DEED)"),
        "Deed Book and Page": re.compile(r"DEED[\s_]*BOOK:\s*([\d/, \n]+)"),
        "Legal Description": re.compile(r"LEGAL[\s\n_]*DESCRIPTION:\s*([\s\S]*?)(?=#|SHERIFF)")
    }

    # Convert PDF to images
    try:
        pages = convert_from_path(pdf_path, dpi=300)
    except Exception as e:
        logging.error(f"Failed to convert PDF to images: {e}")
        return None

    data = []
    entry = {key: {} for key in patterns.keys()}
    text = ""

    # Process each page
    for page_num, page_image in enumerate(pages):
        logging.info(f"Processing page {page_num + 1}...")
        try:
            enhanced_image = enhance_image_contrast(page_image, factor=2.0)
            page_text = pytesseract.image_to_string(enhanced_image)
            text += page_text
        except Exception as e:
            logging.error(f"Error processing page {page_num + 1}: {e}")

    # Extract data using regex patterns
    logging.info("Extracting data from text...")
    for key, pattern in patterns.items():
        matches = pattern.finditer(text)
        match_length = 0
        number_of_entries_saved = len(entry[key])

        for match in matches:
            match_length += 1
            try:
                val = match.group().split(":")[1].replace("\n", " ").strip()
            except IndexError:
                val = match.group().split("\n")[1].replace("\n", " ").strip()

            # Post-process extracted values
            if key == "Sheriff Sale Number" and "1124" not in val:
                val = "1124" + val
            if key in ["Current Record Holder", "Defendant in FIFA", "Legal Description"]:
                val = val.replace("-", "").replace("_", "")
            if key == "Tax Parcel ID":
                val = val.replace("CURRENT", "")

            entry[key][number_of_entries_saved + match_length] = val

        logging.info(f"Found {match_length} occurrences for {key}.")

    # Convert to DataFrame and save to Excel
    df = pd.DataFrame(entry)
    return df

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_path>")
        return

    # pdf_path = sys.argv[1]
    pdf_path = r"C:\Users\Lenovo\OneDrive\Desktop\TechUp\python_codeTogether\brian\extracted_sheriff_sales_info.xlsx"

    logging.info(f"Extracting data from {pdf_path}...")
    df = extract_pdf_data_with_contrast(pdf_path)

    if df is not None:
        output_file = "extracted_sheriff_sales_info.xlsx"
        df.to_excel(output_file, index=False)
        logging.info(f"Data extraction complete. Saved to '{output_file}'.")
    else:
        logging.error("Data extraction failed.")

if __name__ == "__main__":
    main()