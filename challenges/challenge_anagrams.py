def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    # ordenando as strings
    ordered_first_string = ordering_string(first_string)
    ordered_second_string = ordering_string(second_string)

    # invalidamos a presença de strings vazias nos parâmetros
    if len(first_string) == 0 or len(second_string) == 0:
        return (ordered_first_string, ordered_second_string, False)

    # anagramas devem ter o mesmo tamanho, validemos isso
    elif len(first_string) != len(second_string):
        return (ordered_first_string, ordered_second_string, False)

    # anagramas devem ser a mesma palavra após ordenação
    elif ordered_first_string != ordered_second_string:
        return (ordered_first_string, ordered_second_string, False)

    return (ordered_first_string, ordered_second_string, True)


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(
            numbers, start, p - 1
        )  # Os menores em relação ao pivô ficarão à esquerda
        quick_sort(
            numbers, p + 1, end
        )  # Os maiores elementos em relação ao pivô ficarão à direita


# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        """o índice será o elemento em análise no momento,
        ele passará por todos os elementos"""
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            numbers[index], numbers[delimiter] = (
                numbers[delimiter],
                numbers[index],
            )

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


def ordering_string(string):
    """ajustaremos os parâmetros para serem
    case insensitive, convertidos em
    números de acordo com o unicode de cada
    character e em formato de lista"""
    string_insensitive_list = [letter for letter in list(string.casefold())]

    # ordenaremos com o método quick_sort
    quick_sort(string_insensitive_list, 0, len(string_insensitive_list) - 1)

    # unificaremos de lista para string de volta, agora ordenada
    s1 = ""
    for letter in string_insensitive_list:
        s1 += letter
    return s1
