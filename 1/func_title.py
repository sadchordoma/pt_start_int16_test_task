from string import punctuation

# Пример результата выполнения функции:
# «тесТОвое задание для pt» -> «ТесТОвое Задание Для Pt»


not_letters = " 0123456789" + punctuation


def title(input: str) -> str:
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


assert title("тесТОвое    задание для   pt") == "ТесТОвое    Задание Для   Pt"
assert title(" словО серДце") == " СловО СерДце"
assert title(
    "               дЕРЕВО               каМЕТА               ") == "               ДЕРЕВО               КаМЕТА               "
assert enhanced_title("  wh3rE aRe u, m#y  fr1enD") == "  Wh3RE ARe U, M#Y  Fr1EnD"
