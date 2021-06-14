from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def test_career(browser):
        elem = browser.find_element_by_link_text("Карьера")
        elem.click()
        elem = browser.find_element_by_tag_name("h1")
        assert elem.text == 'Карьера'


def test_actions(browser):
    elem = browser.find_element_by_id("menu-actions-1")
    elem.click()
    elem = browser.find_element_by_link_text("Кейсы")
    elem.click()
    elem = browser.find_element_by_tag_name("h1")
    assert elem.text == 'Кейсы'


