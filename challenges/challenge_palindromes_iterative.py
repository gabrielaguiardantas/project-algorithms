def is_palindrome_iterative(word):
    """Faça o código aqui."""
    i = 0
    if len(word) == 0:
        return False
    for letter in word:
        if letter == word[i - 1]:
            i -= 1
        else:
            return False
    return True
