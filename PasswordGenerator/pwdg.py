"""
    password generation file
"""
import random


class PasswordGenerator:
    """
        Main Class
        :method generate_password(): Main Method which creates and returns the password
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_password(p_length=10, use_symbols=False, use_numbers=False, use_letters=False):
        """
        Creates a new 10 digit password, symbols optional.

        :return
            (string): unique string password.

        Args:
            use_numbers: (Boolean) Flag to use numbers or not in password generation.

            use_letters: (Boolean) Flag to use letters or not in password generation.
            use_symbols: (Boolean) Flag to use symbols or not in password generation.
            p_length: (int) length of the password to be created.
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

        chosen_characters = []  # add all the characters that the user chose to a new list

        # use extend to add the list values to the new list
        if use_letters:
            chosen_characters.extend(characters['lowercase'])
            chosen_characters.extend(characters['uppercase'])

        if use_numbers:
            chosen_characters.extend(characters['numbers'])

        if use_symbols:
            chosen_characters.extend(characters['symbols'])

        if not use_symbols and not use_letters and not use_numbers:
            return "password is password :)"

        for i in range(p_length):  # one iteration per password char
            pwd += random.choice(chosen_characters)

        return pwd
