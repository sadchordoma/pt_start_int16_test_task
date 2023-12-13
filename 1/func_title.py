from string import punctuation
import re

# Пример результата выполнения функции:
# «тесТОвое задание для pt» -> «ТесТОвое Задание Для Pt»


not_letters = " 0123456789" + punctuation


# Сперва сделал title1, затем понял, что легче будет сделать все через регулярку -> title2


def title1(input: str) -> str:
    s = list(input)
    index = None
    for i in range(len(s)):
        if s[i] == " ":
            if index is not None:
                s[index] = s[index].upper()
                index = None
        else:
            if index is None:
                index = i
    if index is not None:
        s[index] = s[index].upper()
    return "".join(s)


def title2(input: str) -> str:
    result = re.sub("(^|\s)(\S)",
                    lambda text: text.group(1) + text.group(2).upper(), input)
    return result


# В случае, если слова могут быть разделены не только пробелами, но и другими символами

def enhanced_title(input: str) -> str:
    s = list(input)
    index = None
    for i in range(len(s)):
        if s[i] in not_letters:
            if index is not None:
                s[index] = s[index].upper()
                index = None
        else:
            if index is None:
                index = i
    if index is not None:
        s[index] = s[index].upper()
    return "".join(s)


assert title1("тесТОвое    задание для   pt") == "ТесТОвое    Задание Для   Pt"
assert title1("тесТОвое    задание\n\t для   pt\n\r\t") == "ТесТОвое    Задание\n\t Для   Pt\n\r\t"
assert title1(" словО серДце") == " СловО СерДце"
assert title1("   дЕРЕВО               каМЕТА  ") == "   ДЕРЕВО               КаМЕТА  "

assert title2("тесТОвое    задание для   pt") == "ТесТОвое    Задание Для   Pt"
assert title2("тесТОвое    задание\n\t для   pt\n\r\t") == "ТесТОвое    Задание\n\t Для   Pt\n\r\t"
assert title2(" словО серДце") == " СловО СерДце"
assert title2("   дЕРЕВО               каМЕТА  ") == "   ДЕРЕВО               КаМЕТА  "

assert enhanced_title("  wh3rE aRe u, m#y  fr1enD") == "  Wh3RE ARe U, M#Y  Fr1EnD"
