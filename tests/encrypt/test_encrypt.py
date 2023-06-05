import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # caso a função receba tipos incorretos nos parâmetros
    with pytest.raises(TypeError):
        encrypt_message(0, "string")

    # caso a função receba um índice inválido na key
    assert encrypt_message("fail", -1) == "liaf"

    # caso a função receba uma key ímpar
    assert encrypt_message("fail", 1) == "f_lia"
