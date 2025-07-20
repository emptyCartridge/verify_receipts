from app.parse_receipt_parts import check_top, check_mid, check_sum, check_bot
from static_data import etal_sum, check_num_date, check_customer_inn


def find_match_top(check: str, etal: str):
    matches = []
    for value in etal:
        if value in check:
          matches.append(f"Найдено совпадение: {value}")
        else:
          matches.append(f"Совпадений не найдено: {value}")
    return matches


result_top = find_match_top(check_top, check_num_date)
print(result_top)


#ПРОВЕРКА НА СОВПАДЕНИЯ (УСЛУГА, ID ЗАДАНИЯ)

# def find_match_mid(check: str, etal: str):
#     matches = []
#     for value in etal:
#         if value in check:
#           matches.append(f"Найдено совпадение: {value}")
#         else:
#           matches.append(f"Совпадений не найдено: {value}")
#     return matches
#
# result_mid = find_match_mid(check_mid, check_service_and_id)
# print(result_mid)

#СРАВНЕНИЕ СУММЫ

def sum_comparison(check: str, etal: str):
    if check == etal:
        return "Сумма корректна"
    else:
        return "Некорректная сумма"

result_sum = sum_comparison(check_sum, etal_sum)
print(result_sum)

# #СРАВНЕНИЕ ИТОГО(СУММА)
#
# def total_sum_comparison(check: str, etal: str):
#     if check == etal:
#         return "Сумма (ИТОГО) корректна"
#     else:
#         return "Некорректная сумма (ИТОГО)"
#
# result_total_sum = total_sum_comparison(check_total_sum, etal_sum)
# print(result_total_sum)

#ПРОВЕРКА ИНН ПОКУПАТЕЛЯ

def find_match_inn(check: str, etal: str):
    matches = []
    for value in etal:
        if value in check:
          matches.append(f"Найдено совпадение: {value}")
        else:
          matches.append(f"Совпадений не найдено: {value}")
    return matches

result_inn = find_match_inn(check_bot, check_customer_inn)
print(result_inn)