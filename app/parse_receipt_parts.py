from PIL import Image
import pytesseract
from .ocr_reader import get_ocr_data
from .crops import crop_by_coords_top, crop_by_coords_mid, crop_by_coords_bot, roi_sum


img, data = get_ocr_data('C:/checkreader/static/check_sample2.jpg')


#ПОЛУЧЕНИЕ ДАННЫХ ИЗ КРОПА ШАПКИ (НОМЕР ЧЕКА, ДАТА)
def extract_text_from_top(check) -> str:
    custom_config = r' --oem 3 --psm 6 -c tessedit_char_whitelist=0123456789abcdefghijklmnoprstquvwxyz.,'
    receipt_img = Image.fromarray(check)
    text_from_img = pytesseract.image_to_string(
        receipt_img,
        lang="eng",
        config=custom_config
    )
    text_from_img = text_from_img.lower()
    return text_from_img

roi_top = crop_by_coords_top(img)
check_top = extract_text_from_top(roi_top)
# print(check_top)

#-----------------------------------------------------------------------------------------------------------------------


#ПОЛУЧЕНИЕ ДАННЫХ ИЗ СЕРЕДИНЫ ЧЕКА (НАИМЕНОВАНИЕ УСЛУГ, ID ЗАДАНИЯ)
def extract_text_from_mid(check) -> str:
    #custom_config = r' --oem 3 --psm 6 -c tessedit_char_whitelist=0123456789абвгдеёжзийклмнопрстуфчцщшъыьэюя,.'
    receipt_img = Image.fromarray(check)
    text_from_img = pytesseract.image_to_string(
        receipt_img,
        lang="rus",
        #config=custom_config
    )
    text_from_img = text_from_img.lower()
    return text_from_img

roi_mid = crop_by_coords_mid(img)
check_mid = extract_text_from_mid(roi_mid)
# print(check_mid)

#-----------------------------------------------------------------------------------------------------------------------

#ПОЛУЧЕНИЕ ДАННЫХ О СУММЕ
def extract_sum(check) -> str:
    custom_config = r' --oem 3 --psm 6 -c tessedit_char_whitelist=0123456789,.'
    receipt_img = Image.fromarray(check)
    text_from_img = pytesseract.image_to_string(
        receipt_img,
        config=custom_config
    )
    text_from_img = text_from_img.replace(" ", "").replace(".", ",").replace("\n", "").replace("\r", "")
    parts = text_from_img


    return text_from_img


check_sum = extract_sum(roi_sum)
# print(check_sum)

#-----------------------------------------------------------------------------------------------------------------------

# #ПОЛУЧЕНИЕ ДАННЫХ О СУММЕ (ИТОГО)
# def extract_total_sum(check) -> str:
#     custom_config = r' --oem 3 --psm 6 -c tessedit_char_whitelist=0123456789,.'
#     receipt_img = Image.fromarray(check)
#     text_from_img = pytesseract.image_to_string(
#         receipt_img,
#         config=custom_config
#     )
#     text_from_img = text_from_img.replace(" ", "").replace(".", ",").replace("\n", "").replace("\r", "").replace(":","")
#     return text_from_img
#
#
#
# check_total_sum = extract_total_sum(roi_total_sum)
# print(check_total_sum)

#-----------------------------------------------------------------------------------------------------------------------


#ПОЛУЧЕНИЕ ДАННЫХ НИЗ ЧЕКА (ИНН)
def extract_bot(check) -> str:
    custom_config = "-c tessedit_char_whitelist=0123456789"
    receipt_img = Image.fromarray(check)
    text_from_img = pytesseract.image_to_string(
        receipt_img,
        lang="eng",
        config=custom_config
    )
    return text_from_img

roi_bot = crop_by_coords_bot(img)
check_bot = extract_bot(roi_bot)
# print(check_bot)