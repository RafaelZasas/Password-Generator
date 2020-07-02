import random
import numpy as np


class PasswordGenerator:
    """
        Main Class
        :method generate_password(): Main Method which creates and returns the password
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_password(p_length=10, use_symbols=False):
        """
        Creates a new 10 digit password, symbols optional.
        :param p_length: (int) length of the password to be created.
        :param use_symbols: (Boolean) Flag to use symbols or not in password generation.
        :return
            (string): unique string password.
        """

        characters = {
            'lowercase': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z'],
            'uppercase': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'symbols': ['!', '@', '#', '$', '%', '&', '?']
        }

        pwd = ''

        for i in range(p_length):  # one iteration per password char
            if use_symbols:
                list_choice = random.choice(list(characters))  # choose a list randomly from the dict keys
            else:
                list_choice = random.choice(list(characters)[:-1])  # dont include symbols list

            pwd += random.choice(list(characters[list_choice]))  # append a random char from the chosen list to pwd

        return pwd
