from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_NAME = By.XPATH, ".//label[text()='Имя']/following-sibling::input" #Поле ввода Имя
    SEARCH_PERSONAL_ACCOUNT = By.LINK_TEXT, "Личный Кабинет" #Кнопка-ссылка "Личный кабинет"
    SEARCH_REGISTRATION = By.LINK_TEXT, "Зарегистрироваться" #Кнопка-ссылка "Зарегистрироваться"
    ELEMENTS_MAIN_PAGE = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2" #Для проверки загрузки главной страницы
    FORM_REGISTRATION = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']" #Форма с полями ввода на странице регистрации
    SEARCH_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input" #Поле ввода эл.почты
    SEARCH_PASSWORD = By.XPATH, ".//label[text()='Пароль']/following-sibling::input" #Поле ввода пароля
    REGISTRATION_BUTTON = By.XPATH, ".//form/button[text()='Зарегистрироваться']" #Кнопка регистрации
    FORM_ENTER_TO_PERSONAL_ACCOUNT = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']" #Форма для входа в личный кабинет
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, "Восстановить пароль" #Кнопка-ссылка "Восстановить пароль"
    LINK_ENTER = By.LINK_TEXT, "Войти" #Кнопка-ссылка "Войти"
    INSCRIPTION_REMEMBER_PASSWORD = By.XPATH, ".//p[class='underfined text text_type_main-default text_color_inactive mb-4']" #Надпись "Вспомнили пароль" в форме Восстановления пароля
    BUTTON_PLACE_AN_ORDER = By.XPATH, ".//section[2]//button[text()='Оформить заказ']" #Кнопка "Оформить заказ"
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, ".//section[2]//button[text()='Войти в аккаунт']" #Кнопка "Войти в аккаунт"
    LINK_LOGO = By.XPATH, ".//a[@href='/']" #Ссылка-логотип
    BUTTON_ENTER = By.XPATH, ".//button[text()='Войти']" #Кнопка "Войти"
    PERSONAL_ACCOUNT_FORM = By.XPATH, ".//div[@class='Account_account__vgk_w']" #Форма личного кабинета
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']" #Кнопка "Конструктор"
    BUTTON_LOGOUT = By.XPATH, "html/body/div/div/main/div/nav/ul/li[3]/button[text()='Выход']" #Кнопка "Выход"
    SEARCH_SECTION_SAUSE = By.XPATH, ".//span[text()='Соусы']" #Секция "Соусы"
    SEARCH_LIST_SAUSE = By.XPATH, ".//h2[text()='Соусы']" #Название списка "Соусы"
    SEARCH_SECTION_SMALL_BREADS = By.XPATH, ".//span[text()='Булки']"  # Секция "Булки"
    SEARCH_LIST_SMALL_BREADS = By.XPATH, ".//h2[text()='Булки']"  # Название списка "Булки"
    SEARCH_SECTION_FILLING = By.XPATH, ".//span[text()='Начинки']"  # Секция "Начинки"
    SEARCH_LIST_FILLING = By.XPATH, ".//h2[text()='Начинки']"  # Название списка "Начинки"