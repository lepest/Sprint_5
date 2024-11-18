#Успешная регистрация

import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from data import TestUrl
from helpers import Helpers

class TestRegistrationForm:

    def test_form_registration(self, driver, helpers_name, helpers_email, helpers_password):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.SEARCH_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_REGISTRATION))
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(helpers_name)
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(helpers_email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(helpers_password)
        save_email = driver.find_element(*TestLocators.SEARCH_EMAIL).get_attribute('value')
        save_password = driver.find_element(*TestLocators.SEARCH_PASSWORD).get_attribute('value')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(save_email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(save_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_LOGO))
        driver.find_element(*TestLocators.LINK_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        assert driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).is_displayed()

    def test_incorrect_name(self, driver, helpers_name, helpers_email, helpers_password):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_REGISTRATION))
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys("")
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(helpers_email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(helpers_password)
        assert driver.find_element(*TestLocators.REGISTRATION_BUTTON).click() is None

@pytest.mark.parametrize('email', ['', 'Просто-почта@yandex.ru', 'prosto-pochta-yandex.ru', 'pochta@yandex'])
def test_incorrect_email(email):
    driver = webdriver.Chrome()
    driver.get(TestUrl.main_page_url)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
    driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.SEARCH_REGISTRATION).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_REGISTRATION))
    name = Helpers.random_name()
    driver.find_element(*TestLocators.SEARCH_NAME).send_keys(name)
    driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(email)
    password = Helpers.random_password()
    driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(*TestLocators.REGISTRATION_BUTTON).click() is None
    driver.quit()

@pytest.mark.parametrize('password', ['', '1', '12', '1234', '12345'])
def test_incorrect_password(password):
    driver = webdriver.Chrome()
    driver.get(TestUrl.main_page_url)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
    driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.SEARCH_REGISTRATION).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_REGISTRATION))
    name = Helpers.random_name()
    driver.find_element(*TestLocators.SEARCH_NAME).send_keys(name)
    email = Helpers.random_email()
    driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert "Некорректный пароль"
    driver.quit()