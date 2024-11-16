from random import choice
from random import randint

class Helpers:
    def random_name():
        list_name = ['Aleks', 'Sveta', 'Tanya', 'Tolya', 'Tamara', 'Boris', 'Valya', 'Vasilii', 'Katya', 'Irina', 'Roma']
        name = choice(list_name)
        return name

    #случайный адрес эл. почты для регистрации
    def random_email():
        e = randint(100, 1000)
        email = f'Nastya_Golenischeva_12_{e}@yandex.ru'
        return email

    #случайный пароль для регистрации
    def random_password():
        password = randint(100000, 1000000000)
        return password