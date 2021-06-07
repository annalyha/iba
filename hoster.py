import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HosterTestCase(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()

    def test_search_in_hoster_by(self):
        driver = self.driver
        # открытие в Firefox страницы https://hoster.by/
        driver.get("https://hoster.by/")
        # проверка наличия слова hoster.by в заголовке страницы
        self.assertIn("hoster.by", driver.title)
        # ждем 5 секунд
        time.sleep(5)

        # проверка имени домена
        elem = driver.find_element_by_name("domain_name")
        # ждем 5 секунд
        time.sleep(5)
        # набор слова tut в найденном элементе
        elem.send_keys("tut")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Проверить в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)

        elem = driver.find_element_by_class_name("group-valid")
        # ждем 5 секунд
        time.sleep(5)

        # находим элемент страницы по ID
        elem = driver.find_element_by_id("ui-id-5-button")
        # нажатие на кнопку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)

        elem = driver.find_element_by_id("ui-id-8")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)

        # Протестировать кнопку "В корзину". На данном этапе не получилось. Буду пробовать

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def test_Phone_in_hoster_by(self):
        driver = self.driver
        # открытие в Firefox страницы https://hoster.by/
        driver.get("https://hoster.by/")
        # ждем 5 секунд
        time.sleep(5)

        elem = driver.find_element_by_class_name("icon-phone-light")
        # нажатие на ссылку
        elem.click()
        # ждем 10 секунд
        time.sleep(10)

        elem = driver.find_element_by_id("callModal")
        elem = driver.find_element_by_class_name("close")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)


    def test_Clients_in_hoster_by(self):
        driver = self.driver
        # открытие в Firefox страницы https://hoster.by/
        driver.get("https://hoster.by/")
        # ждем 5 секунд
        time.sleep(5)
        elem = driver.find_element_by_link_text("Клиентам")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
