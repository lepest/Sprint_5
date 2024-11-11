import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    web_driver = webdriver.Chrome()
    # search_form = SearchForm(driver, TestLocators.SEARCH_FORM_LOCATOR)
    return web_driver
    web_driver.quit()

