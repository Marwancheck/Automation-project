import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Search_site(unittest.TestCase):
    SEARCH_FIELD = (By.XPATH, '//*[@id="keyword"]')
    SEARCH_ICON = (By.CLASS_NAME, "icon-search")


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_search_site(self):
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys('Acer')
        self.chrome.find_element(*self.SEARCH_ICON).click()
        product_elements = self.chrome.find_elements(By.CSS_SELECTOR, "h2.productTitle")
        for element in product_elements:
            assert "acer" in element.text.lower(), "Not all products contain 'acer' in their names"



