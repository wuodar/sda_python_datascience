"""
Napisz test funkcji produce_double_signs przy użyciu biblioteki unittest
"""
import unittest


def produce_double_signs(string):
    """Tworzy nowy napis na podstawie podanego, podwajajac kazdy znak.

    :param string: napis, w ktorym znaki powinny byc podwojone
    :return: nowy napis z podwojonymi znakami.

    """
    new_string = ""

    for sign in string:
        new_string += sign
        new_string += sign

    return new_string


class ProduceDoubleSignsTestCase(unittest.TestCase):

    def test_produce_double_signs(self):
        self.string = "OzzyMiś"
        self.produce_double_signs = produce_double_signs(self.string)

unittest.TestCase()
