import PasswordGenerator

if __name__ == '__main__':
    func = PasswordGenerator.pwdg.PasswordGenerator()
    pwd = func.generate_password(10, True)
    print(f'Generated Password: {pwd}')
