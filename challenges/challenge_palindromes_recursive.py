def is_palindrome_recursive(word, low_index, high_index):

    string = word
    # stringIndex = low_index
    # StringHigh = high_index

    if not string:
        return False
    if string[low_index] != string[high_index]:
        return False
    if low_index >= high_index or low_index == high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    # try:
    # stringSemEspaços = string.replace(' ', '')
    # stringTodaMinuscula = stringSemEspaços.lower()
    # stringInvertida = stringTodaMinuscula[::-1]
    # if stringInvertida == stringTodaMinuscula:
    #     return True
    # else:
    #     return False
    # except TypeError:
    #     return False
