def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    sizeWord = len(word) - 1
    for index in range(len(word) // 2):
        if word[index] != word[sizeWord - index]:
            return False
    return True
