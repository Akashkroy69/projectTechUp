import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance
import threading
import time

# Configure Tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def enhance_image_contrast(image, factor=2.0):
    """
    Enhances the contrast of an image.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def extract_pdf_data_with_contrast(pdf_path, progress_callback=None, status_callback=None):
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
    if status_callback:
        status_callback("Converting PDF to images...")
    try:
        pages = convert_from_path(pdf_path, dpi=300)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert PDF to images: {e}")
        return None

    data = []
    entry = {key: {} for key in patterns.keys()}
    text = ""

    # Process each page
    total_pages = len(pages)
    start_time = time.time()
    for page_num, page_image in enumerate(pages):
        if status_callback:
            status_callback(f"Processing page {page_num + 1}/{total_pages}...")
        try:
            enhanced_image = enhance_image_contrast(page_image, factor=2.0)
            page_text = pytesseract.image_to_string(enhanced_image)
            text += page_text

            # Update progress
            if progress_callback:
                progress = int((page_num + 1) / total_pages * 100)
                elapsed_time = time.time() - start_time
                estimated_total_time = elapsed_time / ((page_num + 1) / total_pages)
                estimated_time_remaining = estimated_total_time - elapsed_time
                progress_callback(progress, estimated_time_remaining)
        except Exception as e:
            messagebox.showerror("Error", f"Error processing page {page_num + 1}: {e}")

    # Extract data using regex patterns
    if status_callback:
        status_callback("Extracting data with regex...")
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

    # Convert to DataFrame
    if status_callback:
        status_callback("Saving data to Excel...")
    df = pd.DataFrame(entry)
    return df

def upload_pdf():
    """
    Opens a file dialog to upload a PDF file.
    """
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_path.set(file_path)
        messagebox.showinfo("Success", "PDF file uploaded successfully!")

def extract_data():
    """
    Extracts data from the uploaded PDF and saves it to an Excel file.
    """
    pdf_file = pdf_path.get()
    if not pdf_file:
        messagebox.showerror("Error", "Please upload a PDF file first!")
        return

    # Disable buttons during extraction
    upload_button.config(state=tk.DISABLED)
    extract_button.config(state=tk.DISABLED)

    # Start extraction in a separate thread
    def run_extraction():
        try:
            df = extract_pdf_data_with_contrast(
                pdf_file,
                progress_callback=update_progress,
                status_callback=update_status
            )
            if df is not None:
                output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
                if output_file:
                    df.to_excel(output_file, index=False)
                    messagebox.showinfo("Success", f"Data extracted and saved to {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            # Re-enable buttons
            upload_button.config(state=tk.NORMAL)
            extract_button.config(state=tk.NORMAL)
            progress_bar["value"] = 0  # Reset progress bar
            status_label.config(text="Ready")  # Reset status label

    # Start the extraction thread
    threading.Thread(target=run_extraction, daemon=True).start()

def update_progress(progress, estimated_time_remaining):
    """
    Updates the progress bar and estimated time.
    """
    progress_bar["value"] = progress
    time_remaining_label.config(text=f"Estimated time remaining: {int(estimated_time_remaining)} seconds")
    root.update_idletasks()

def update_status(status):
    """
    Updates the status label.
    """
    status_label.config(text=status)
    root.update_idletasks()

# Create the main application window
root = tk.Tk()
root.title("PDF Data Extractor")
root.geometry("500x500")

# Variable to store the PDF file path
pdf_path = tk.StringVar()

# GUI Components
label = tk.Label(root, text="Upload a PDF file to extract data:", font=("Arial", 12))
label.pack(pady=10)

upload_button = tk.Button(root, text="Upload PDF", command=upload_pdf, bg="lightblue", font=("Arial", 10))
upload_button.pack(pady=10)

extract_button = tk.Button(root, text="Extract Data to Excel", command=extract_data, bg="lightgreen", font=("Arial", 10))
extract_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Estimated Time Remaining Label
time_remaining_label = tk.Label(root, text="Estimated time remaining: --", font=("Arial", 10))
time_remaining_label.pack(pady=5)

# Status Label
status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=5)

# Run the application
root.mainloop()