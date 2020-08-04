"""
    password generation file
"""
import random


class PasswordGenerator:
    """
        Main Class
        :method generate_password(): Main Method which creates and returns the password
    """
    data_url = ''

    def __init__(self):
        pass

    @staticmethod
    def random_index(x):
        """

        :param x: to get random index from list so we want a value from 0 to (length-1)
        :return: Random index to be used
        """
        return random.randint(0, x - 1)

    def generate_password(self, p_length, use_symbols):
        """
        Creates a new 10 digit password, symbols optional.

        :param use_symbols: (Boolean) Flag whether to use symbols in password generation or not
        :param p_length: (int) length of the password string created

        :return
            (string): returns unique string password
        """

        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '&', '?']
        pwd = ''
        # Decide whether we want symbols in the password
        if use_symbols:
            n = 4
        else:
            n = 3
        for i in range(p_length):
            list_choice = random.randint(0, n)  # choose a list to select from

            # From the chosen list pick a random character
            if list_choice == 0:
                character = lowercase[self.random_index(len(lowercase))]
            elif list_choice == 1:
                character = uppercase[self.random_index(len(uppercase))]
            elif list_choice == 2:
                character = numbers[self.random_index(len(numbers))]
            elif list_choice == 3:
                character = symbols[self.random_index(len(symbols))]

            pwd += character  # add the random char from random list

        return pwd
