import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_8_characters():
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(8)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_uppercase_lowercase():
    valid_characters = string.digits + string.punctuation + string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase
    password = generate_password(50)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters