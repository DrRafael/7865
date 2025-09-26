import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_zero_length():
    password = generate_password(0)
    assert len(password) == 0
    assert password == ""

def test_twopasswords():
    length = 15
    password_1 = generate_password(length)
    password_2 = generate_password(length)

    assert len(password_1) == length 
    assert len(password_1) == length 

    assert password_1 != password_2, ""

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""