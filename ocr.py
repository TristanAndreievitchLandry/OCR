# pip install pytesseract

# pip install pillow

# pip install pdf2image

import os

import pytesseract

from PIL import Image

from pdf2image import convert_from_path

from tqdm import tqdm


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def ocr_to_text(file_path):

    # Conversion du PDF en images

    if file_path.endswith('.pdf'):

        images = convert_from_path(file_path)

        image_files = []

        for i, image in enumerate(images):

            image_file = f'page_{i+1}.jpg'

            image.save(image_file, 'JPEG')

            image_files.append(image_file)

    else:

        image_files = [file_path]

    # Extraction du texte de chaque image

    text = ''

    progress_bar = tqdm(total=len(image_files), desc="Processing images")

    for image_file in image_files:

        img = Image.open(image_file)

        extracted_text = pytesseract.image_to_string(img, lang='eng')

        text += extracted_text + '\n'

        progress_bar.update(1)

    # Suppression des fichiers d'images temporaires (si nécessaire)

    if file_path.endswith('.pdf'):

        for image_file in image_files:

            os.remove(image_file)

    # Save the extracted text to a file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(text)

    progress_bar.close()


# Example usage
file_path = "input.pdf"
output_file_path = "output.txt"
result = ocr_to_text(file_path)
print("Text saved to:", output_file_path)
