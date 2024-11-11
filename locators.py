from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLocators:
    SEARCH_FORM_LOCATOR = [By.XPATH, "//*[@CLASS='App_App__aOmNj"]
    #SEARCH_BUTTON =
    SEARCH_NAME = By.XPATH, ".//form/fieldset[1]//input"
    SEARCH_PERSONAL_ACCOUNT = By.LINK_TEXT, "Личный Кабинет"
    SEARCH_REGISTRATION = By.LINK_TEXT, "Зарегистрироваться"