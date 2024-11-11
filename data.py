from random import randint
from random import choice

class TestData:

    #ссылка на главную страницу
    main_page_url = 'https://stellarburgers.nomoreparties.site'

    #случайное имя для регистрации
    list_name = ['Aleks', 'Sveta', 'Tanya', 'Tolya', 'Tamara', 'Boris', 'Valya', 'Vasilii', 'Katya', 'Irina', 'Roma']
    name = choice(list_name)
    name_1 = choice(list_name)
    name_2 = choice(list_name)

    #случайный адрес эл. почты для регистрации
    e = randint(100, 1000)
    email = f'{name}_12_{e}@yandex.ru'
    email_1 = f'{name_1}_12_{e}@yandex.ru'
    email_2 = f'{name_2}_12_{e}@yandex.ru'

    #случайный пароль для регистрации
    p = randint(100000, 1000000000)
    password = p
    password_1 = p
    password_2 = p

    #зарегистрированный адрес эл. почты
    correct_email = 'Nastya_Golenischeva_12_321@yandex.ru'
    correct_password = 'Boolki'



