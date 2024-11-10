'''модуль отвечающий за валидацию данных'''

users = {"eg@gmail.com": "12345678",
         "er@gmail.com": "12345678", "or@gmial.com": "12345678"}


def login(email: str, pas: str):
    '''Проверка на наличие пользователя'''
    try:
        if {email: pas} not in users:
            raise Exception("No such user")
        return True
    except Exception as ex:
        print(ex)
        return False
