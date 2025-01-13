text = ""
    for page_num, page_image in enumerate(pages):
        # Enhance contrast to make light text darker`
        enhanced_image = enhance_image_contrast(page_image, factor=2.0)

        # Apply OCR
        print('Fetching page number: ', page_num)
        text = text + pytesseract.image_to_string(enhanced_image)
