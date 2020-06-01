from main import PasswordGenerator

if __name__ == '__main__':
    func = PasswordGenerator.PasswordGenerator()
    pwd = func.generate_password()
    print(f'Generated Password: {pwd}')
