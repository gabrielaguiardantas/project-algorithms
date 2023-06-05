def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "":
        return False
    if low_index == (len(word) // 2) + 1:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
