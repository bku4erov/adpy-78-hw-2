import csv
from pprint import pprint

## Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# примеры из лекции:
# репл с лекции: https://replit.com/@shorstko/netologyregex230630#main.py
# регулярка для поиска телефонов: r"(+7|8)?\s((\d+))\s(\d+)[\s-](\d+)[\s-](\d+)"
# вариант регулярки для форматирования телефонов: r"+7(\2)\3-\4-\5"


## 1. Выполните пункты 1-3 задания.
## Ваш код
contacts_pattern = r"^(?P<lastname>\w+)[\s,]*(?P<firstname>\w+)[\s,]*(?P<surname>\w*)[\s,]*(?P<organization>[\w]*),(?P<position>[\w\s\-\–]*),(?P<phone>[\w\d\s\(\)\-\+\.]*),(?P<email>[\w\d\.\-\_@]*)"
contacts_pattern_replace = r"\g<lastname>,\g<firstname>,\g<surname>,\g<organization>,\g<position>,\g<phone>,\g<email>"

phone_with_ad_pattern = r"(\+7|8)?[\s\(]*(\d{3})[\)\s\-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\sдоб\.\(]*(\d*)\)*"
phone_with_ad_pattern_replace = r"+7(\2)\3-\4-\5 доб. \6"

phone_pattern = r"(\+7|8)?[\s\(]*(\d{3})[\)\s\-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
phone_pattern_replace = r"+7(\2)\3-\4-\5"

# ^(?P<lastname>\w+)[\s,]*(?P<firstname>\w+)[\s,]*(?P<surname>\w*)[\s,]*(?P<organization>[\w]*),(?P<position>[\w\s\-\–]*),(?P<phone>[\w\d\s\(\)\-\+\.]*),(?P<email>[\w\d\.\-\_@]*)
# \g<lastname>,\g<firstname>,\g<surname>,\g<organization>,\g<position>,\g<phone>,\g<email>

# (\+7|8)?[\s\(]*(\d{3})[\)\s\-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\sдоб\.\(]*(\d*)\)*

# (\+7|8)?[\s\(]*(\d{3})[\)\s\-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\w\.\(]*(\d*)\)*
# +7(\2)\3-\4-\5

# r"(^\w+)[\s,](\w+)[\s,](\w*)[\s,]{1,3}([\w\s]+),([\w\s\-\–]*),([\w\d\s\(\)\-\+\.]*),([\w\d\.\-\_@]*)"
# ^(\w+)[\s,]*(\w+)[\s,]*(\w*)[\s,]*([\w]*),([\w\s\-\–]*),([\w\d\s\(\)\-\+\.]*),([\w\d\.\-\_@]*)
# (^\w+)[\s,](\w+)[\s,](\w+)[\s,]{1,3}([\w\s]+),([\w\s\-\–]*),((\+7|8)?[\s\(\-]*(\d+)[\s\)\-]*(\d+)[\s\)\-]*(\d+)[\s\)\-]*(\d+)([\sдоб.]*)?)?,([\w\d@.\-]*)?


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)
