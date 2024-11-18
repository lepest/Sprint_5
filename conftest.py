import pytest

from selenium import webdriver
from helpers import Helpers

@pytest.fixture(scope='function')
def driver():
    web_driver = webdriver.Chrome()
    return web_driver
    web_driver.quit()

@pytest.fixture
def helpers_name():
    name = Helpers.random_name()
    return name

@pytest.fixture
def helpers_email():
    email = Helpers.random_email()
    return email

@pytest.fixture
def helpers_password():
    password = Helpers.random_password()
    return password