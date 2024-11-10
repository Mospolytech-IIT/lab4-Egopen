'''Модуль отвечающий за валидацию данных'''
import re


def checkemail(email: str):
    '''Валидация почты'''
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        raise Exception("Incorrect email")
    print("Почта нормальная")
    return True

def checkpassword(password: str):
    'Валидация пароля'
    if len(password)<8:
        raise Exception("Пароль меньше 8 символов")
    print("Пароль нормальный")
    return True
