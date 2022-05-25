"""
Napisz test funkcji produce_double_signs przy użyciu biblioteki unittest
"""

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

import unittest

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print("Setting Up")
        self.word = "aabbccdd"
        self.basicword = "abcd"
        print(self.word)
        print(self.basicword)
    def testPass(self):
        self.assertEqual(self.word,produce_double_signs(self.basicword) )