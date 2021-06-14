import pytest

from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    page = driver.get('https://hoster.by/')
    yield driver
    driver.close()



