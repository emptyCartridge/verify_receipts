import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def get_ocr_data(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Не удалось загрузить изображение {image_path}")

    data = pytesseract.image_to_data(
        image,
        lang='rus',
        config='--psm 6',
        output_type=pytesseract.Output.DICT
    )

    return image, data


