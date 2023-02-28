import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    testImpar = encrypt_message("abacad", 3)
    assert testImpar == "aba_dac"

    testPar = encrypt_message("abcdef", 4)
    assert testPar == "fe_dcba"

    testValueInvalid = encrypt_message("abcdef", 9)
    assert testValueInvalid == "fedcba"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcdef", "3")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)
