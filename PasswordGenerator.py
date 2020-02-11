import random
import pandas as pd


class PasswordGenerator:
    data_url = ''

    def __init__(self, url):
        self.data_url = url

    @staticmethod
    def generate_password():
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '&', '?']
        password = ''
        for i in range(10):
            list_choice = random.randint(0, 3)  # choose a list to select from

            character = {
                0: lowercase[random.randint(0, 25)],
                1: uppercase[random.randint(0, 25)],
                2: numbers[random.randint(0, 9)],
                3: symbols[random.randint(0, 6)]
            }

            password += character[list_choice]  # add the random char from random list

        return password


x = PasswordGenerator()
print(x.generate_password())
