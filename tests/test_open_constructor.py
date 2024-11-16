#Переход из личного кабинета в конструктор

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from data import TestData
from data import TestUrl

class TestFollowToPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(TestData.correct_email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(TestData.correct_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_LOGO))
        driver.find_element(*TestLocators.LINK_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_FORM))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))