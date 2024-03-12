import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Check_service_garantii(unittest.TestCase):
    SERVICE_PAGE = (By.CLASS_NAME, "service")
    PAGE_TITLE_TEXT = (By.XPATH, "//h2[@class='articleTitle' and text()='Service & Garantii']")


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_acces_service_garantii(self):
        WebDriverWait(self.chrome, 4).until(EC.presence_of_element_located(self.SERVICE_PAGE)).click()
        actual_message = self.chrome.find_element(*self.PAGE_TITLE_TEXT).text
        if actual_message == "Service & Garantii":
            print("Correct page title displayed")
        else:
            print("Incorrect page title")
        assert actual_message == "Service & Garantii", "Incorrect page title displayed"




