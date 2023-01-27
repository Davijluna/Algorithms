from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    # pass
    assert encrypt_message("testes", -1) == "setset"
    assert encrypt_message("testes", 1) == "t_setse"
    assert encrypt_message("testes", 2) == "sets_et"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("testes", "string")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)
