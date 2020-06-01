import random
import pandas as pd
import random

class PasswordGenerator:
    data_url = ''

    def __init__(self, url):
        self.data_url = url

    @staticmethod
    def generate_password(p_length=10, use_symbols=False):
        """
        Creates a new 10 digit password, symbols optional.

        :param
            p_length (int): length of the password string created
        :param
            use_symbols (boolean): are symbols allowed in the string password
        :return
            (string): returns unique string password
        """
        def random_index(x):
            return random.randint(0, x - 1) # This is to get a random index from a list so we want a value from 0 to (length-1)

        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '&', '?']
        password = ''
        # Decide whether we want symbols in the password
        if use_symbols:
            n = 4
        else:
            n = 3
        for i in range(p_length):
            list_choice = random.randint(n)  # choose a list to select from

            # From the chosen list pick a random character
            if list_choice == 0:
                character = lowercase[random_index(len(lowercase))]
            elif list_choice == 1:
                character = uppercase[random_index(len(uppercase))]
            elif list_choice == 2:
                character = numbers[random_index(len(numbers))]
            elif list_choice == 3:
                character = symbols[random_index(len(symbols))]

            password += character  # add the random char from random list

        return password


x = PasswordGenerator("name")
print(x.generate_password(15, True))
