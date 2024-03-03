import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Add_remove_item_cart(unittest.TestCase):
    LAPTOP_CATEGORY = (By.XPATH, '//a[@class="parentCategName"]')
    LAPTOP_CATEGORY_2 = (By.CSS_SELECTOR, 'a.category[href="https://www.cel.ro/laptop-laptopuri/"]')
    ADD_LAPTOP = (By.XPATH, '//a[@class="buy-product hasCBF"]')
    REMOVE_ITEM = (By.XPATH, "//a[@title='Sterge din cos']")
    QUANTITY_ITEM = (By.NAME, "cart_quantity[]")
    ITEM_REMOVE_MESSAGE = (By.XPATH, "//h2[text()='Cosul tau de cumparaturi a ramas fara produse!']")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_add_item_cart(self):
        self.chrome.find_element(*self.LAPTOP_CATEGORY).click()
        self.chrome.find_element(*self.LAPTOP_CATEGORY_2).click()
        self.chrome.find_element(*self.ADD_LAPTOP).click()
        select_element = self.chrome.find_element(*self.QUANTITY_ITEM)
        select = Select(select_element)
        selected_option = select.first_selected_option
        assert selected_option.get_attribute("value") == '1', "Quantity is not equal to 1"
        print("Only one quantity is added.")

    def test_remove_item_cart(self):
        self.chrome.find_element(*self.LAPTOP_CATEGORY).click()
        self.chrome.find_element(*self.LAPTOP_CATEGORY_2).click()
        self.chrome.find_element(*self.ADD_LAPTOP).click()
        self.chrome.find_element(*self.REMOVE_ITEM).click()
        try:
            actual_message = self.chrome.find_element(*self.ITEM_REMOVE_MESSAGE).text
            print("Item removed message displayed.")
        except NotImplementedError:
            actual_message = "None"
        expected_message = "Cosul tau de cumparaturi a ramas fara produse!"
        assert expected_message == actual_message





