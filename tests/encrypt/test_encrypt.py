from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(None, 10) or encrypt_message("abc", None)
    assert encrypt_message("Galo Doido", -9) == "odioD olaG"
    assert encrypt_message("GaloDoido", 1) == "G_odioDola"
    assert encrypt_message("GaloDoido", 2) == "odioDol_aG"
