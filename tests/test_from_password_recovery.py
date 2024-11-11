#Вход через кнопку в форме восстановления пароля

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from data import TestData


class TestFormPasswordRecovery:

    def test_enter_from_password_recovery(self, driver):
        driver.get(TestData.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.LINK_RECOVERY_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_ENTER))
        driver.find_element(*TestLocators.LINK_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.SEARCH_EMAIL).send_keys(TestData.correct_email)
        driver.find_element(*TestLocators.SEARCH_PASSWORD).send_keys(TestData.correct_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        driver.find_element(*TestLocators.LINK_LOGO).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))
        driver.quit()