"""
Napisz test funkcji hide_password przy użyciu biblioteki unittest
"""
import unittest

def hide_password(password):
    """Ukrywa co trzecia litere w hasle password.
    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.
    """
    signs = list(password)
    for i, sign in enumerate(signs):
        if i > 1 and (i+1) % 3 == 0:
            signs[i] = "*"
    return "".join(signs)

class TestHidePassword(unittest.TestCase):
    def test_hide_password(self):
        password = "kajakarz"
        hidden = hide_password(password)

        self.assertEqual(hidden, "ka*ak*rz")

    def test_no_password(self):
        password = ""
        hidden = hide_password(password)

        self.assertEqual(hidden, "")

    def test_password_len_divbisible_by3_minus_2(self):
        password = "password12"
        hidden = hide_password(password)

        self.assertEqual(hidden, "pa*sw*rd*2")

    def test_super_long_password(self):
        password = "ab*" *1000
        hidden = hide_password(password)

        self.assertEqual(hidden, "ab*" * 1000)
