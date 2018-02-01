#Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в ней за исключением пробелов встречаются только один раз.
#Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами, а само слово 'изограмма' - нет.

import re
str = 'https://en.wikipedia.org/wiki/Isogram'


def indicate_isogramm(str):
    reg = re.compile('[^a-zA-Z]')
    str_letters = reg.sub('', str)
    print(reg.sub('', str))

    for i in range((len(str_letters)) - 1):
        if str_letters[i] in str_letters[i + 1:]:
            return False

    return True

print(indicate_isogramm(str))









