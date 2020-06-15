import random
import pandas as pd
import random


class PasswordGenerator:
    """
        Main Class
        :method generate_password(): Main Method which creates and returns the password
    """
    data_url = ''

    def __init__(self):
        self.lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '@', '#', '$', '%', '&', '?']
        self.__pwd = ''

    def getPrivatePassword(self):
        """
            Get Private attribute pwd
            :returns the password
        """
        return self.__pwd


    @staticmethod
    def random_index(x):
        """

        :param x: to get random index from list so we want a value from 0 to (length-1)
        :return: Random index to be used
        """
        return random.randint(0, x - 1)

    def generate_password(self, p_length=10, use_symbols=True):
        """
        Creates a new 10 digit password, symbols optional.

        :param use_symbols: (Boolean) Flag whether to use symbols in password generation or not
        :param p_length: (int) length of the password string created
        :return
            (string): returns unique string password
        """


        # Decide whether we want symbols in the password
        if use_symbols:
            n = 3
        else:
            n = 2
        for i in range(p_length):
            list_choice = random.randint(0, n)  # choose a list to select from
            character = ''
            # From the chosen list pick a random character
            if list_choice == 0:
                character = self.lowercase[self.random_index(len(self.lowercase))]
            elif list_choice == 1:
                character = self.uppercase[self.random_index(len(self.uppercase))]
            elif list_choice == 2:
                character = self.numbers[self.random_index(len(self.numbers))]
            elif list_choice == 3:
                character = self.symbols[self.random_index(len(self.symbols))]

            self.__pwd += character  # add the random char from random list

        return self.__pwd
