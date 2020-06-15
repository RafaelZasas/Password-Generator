#!/usr/bin/env Python3
from PasswordGenerator.pwdg import PasswordGenerator as obj
import unittest


class TestPasswordGenerator(unittest.TestCase):  # inherits from unittest.TestCase
    def test_password(self):
        """
        Tests the generate_password() function within password generator
        """

        pwd1 = obj().generate_password(10, False)# to test with no symbols
        pwd2 = obj().generate_password(46, True)  # to test with symbols

        test_case1 = len(pwd1) == 10  # check to see if the length is 10
        test_case2 = len(pwd2) == 46  # check to see if the length is 10

        for symbol in obj().symbols:
            if symbol in pwd1:  # check to see if the password contains symbols
                test_case1 = False
                break

        for symbol in obj().symbols:
            if symbol in pwd2:  # check to see if the password contains symbols
                test_case2 = True
                break

        self.assertEqual(test_case1 is True, test_case2 is True)  # evaluate if both tests are true




if __name__ == '__main__':
    unittest.main()
