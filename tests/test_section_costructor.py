#Тестирование раздела "Конструктор"

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators
from data import TestUrl

class TestSectionConstructor:
    def test_section_constructor_sause(self, driver):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_SECTION_SAUSE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        assert driver.find_element(*TestLocators.SEARCH_LIST_SAUSE).is_displayed()

    def test_section_constructor_small_breads(self, driver):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_SECTION_SAUSE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_SECTION_SMALL_BREADS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        assert driver.find_element(*TestLocators.SEARCH_LIST_SMALL_BREADS).is_displayed()

    def test_section_constructor_list_filling(self, driver):
        driver.get(TestUrl.main_page_url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        driver.find_element(*TestLocators.SEARCH_SECTION_FILLING).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ELEMENTS_MAIN_PAGE))
        assert driver.find_element(*TestLocators.SEARCH_LIST_FILLING).is_displayed()