import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class Log_in_invalid(unittest.TestCase):
    USER_ICON = (By.CSS_SELECTOR, "span.icon-wrapper > i.icon-icon_user")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.cel.ro/index.php?main_page=login&cust=1']")
    MAIL = (By.ID, "email_address")
    PASSWORD = (By.XPATH, "//input[@name='passwordx']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Conecteaza-te']")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Eroare: Date incorecte.')]")
    PAGE_TITLE_TEXT = (By.XPATH, "//h2[@class='articleTitle' and text()='Service & Garantii']")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_log_in_invalid_credentials(self):
        self.chrome.find_element(*self.USER_ICON).click()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.MAIL).send_keys("test@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("CW9WFKNn")
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        try:
            actual_message = self.chrome.find_element(*self.EMAIL_ERROR_MESSAGE).text
            print("Invalid credentials error message displayed.")
        except NotImplementedError:
            actual_message = "None"
        expected_message = "Eroare: Date incorecte."
        assert expected_message == actual_message





