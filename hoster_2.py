from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def test_new(browser):
    # находим на странице заголовок 2-ого уровня (h2)
    elem = browser.find_element_by_id("menu-domains-1")
    elem.click
    wait = WebDriverWait(browser, 20)

def test_actions(browser):
    elem = browser.find_element_by_id("menu-actions-1")
    elem.click
    wait = WebDriverWait(browser, 20)

def test_hosting(browser):
    elem = browser.find_element_by_id("menu-hosting-1")
    options = elem.find_elements_by_tag_name("item")
    for item in options:
        if item.text.find("Стандартные") >= 0:
            item.click()
