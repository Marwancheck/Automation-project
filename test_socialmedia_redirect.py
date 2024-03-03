import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Social_media_redirect(unittest.TestCase):
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, 'a.facebook')
    YOUTUBE_BUTTON = (By.XPATH, '//a[@class="giveawayBannerWrapper"]')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_facebook_redirect(self):
        self.chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.FACEBOOK_BUTTON)).click()
        self.chrome.implicitly_wait(3)
        self.chrome.switch_to.window(self.chrome.window_handles[-1])
        assert "https://www.facebook.com/2celro" in self.chrome.current_url, "Not redirected to facebook"

    def test_youtube_redirect(self):
        self.chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.chrome.find_element(*self.YOUTUBE_BUTTON).click()
        self.chrome.implicitly_wait(3)
        self.chrome.switch_to.window(self.chrome.window_handles[-1])
        assert "https://consent.youtube.com" in self.chrome.current_url, "Not redirected to youtube"
