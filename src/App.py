import PasswordGenerator.pwdg as file

if __name__ == '__main__':
    obj = file.PasswordGenerator()
    pwd = obj.generate_password()
    print(f'Generated Password: {pwd}')
