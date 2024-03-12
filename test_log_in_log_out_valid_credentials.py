import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class Log_in_out(unittest.TestCase):
    USER_ICON = (By.CSS_SELECTOR, "span.icon-wrapper > i.icon-icon_user")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.cel.ro/index.php?main_page=login&cust=1']")
    MAIL = (By.ID, "email_address")
    PASSWORD = (By.XPATH, "//input[@name='passwordx']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Conecteaza-te']")
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Iesire din cont']")



    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_log_in_valid_credentials(self):
        self.chrome.find_element(*self.USER_ICON).click()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.MAIL).send_keys("ginasie@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("CW9WFKNn")
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        self.chrome.find_element(*self.USER_ICON).click()
        login_account_name = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "welcomeMsg")))
        assert login_account_name.text == "Test Testare", "Logged-in user is not 'Test Testare'"
        print("Successfully logged in as 'Test Testare'")

    def test_log_out(self):
        self.chrome.find_element(*self.USER_ICON).click()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.MAIL).send_keys("ginasie@yahoo.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("CW9WFKNn")
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        self.chrome.find_element(*self.USER_ICON).click()
        self.chrome.find_element(*self.LOG_OUT_BUTTON).click()
        logoff_message = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "logoutArea"))).text
        assert "V-ati deconectat de la contul dvs." in logoff_message, "No log-out message"
        print("Log-out message displayed")










