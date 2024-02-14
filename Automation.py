import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture(scope="module")
def browser():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()

def test_invalid_login(browser):
    browser.get("https://www.cel.ro")
    sleep(2)
    user_icon = browser.find_element(By.CSS_SELECTOR, "span.icon-wrapper > i.icon-icon_user")
    user_icon.click()
    sleep(2)
    sign_in_button = browser.find_element(By.CSS_SELECTOR, "a[href='https://www.cel.ro/index.php?main_page=login&cust=1']")
    sign_in_button.click()
    sleep(2)
    email_input = browser.find_element(By.ID, "email_address")
    email_input.send_keys("test@yahoo.com")
    sleep(3)
    password_input = browser.find_element(By.XPATH, "//input[@name='passwordx']")
    password_input.send_keys("CW9WFKNn")
    sleep(3)
    sign_in_button = browser.find_element(By.XPATH, "//button[text()='Conecteaza-te']")
    sign_in_button.click()
    sleep(3)

    eroare_mesaj = "Eroare: Date incorecte."
    try:
        error_element = browser.find_element(By.XPATH, f"//*[contains(text(), '{eroare_mesaj}')]")
        print("Invalid credentials error message displayed.")
    except:
        raise NotImplementedError


def test_log_in(browser):
    # Open the webpage
    browser.get("https://www.cel.ro")
    sleep(3)
    user = browser.find_element(By.CSS_SELECTOR, "span.icon-wrapper > i.icon-icon_user")
    user.click()
    sleep(2)
    gg = browser.find_element(By.CSS_SELECTOR, "a[href='https://www.cel.ro/index.php?main_page=login&cust=1']")
    gg.click()
    sleep(2)
    mail = browser.find_element(By.ID, "email_address")
    mail.send_keys("ginasie@yahoo.com")
    sleep(3)
    passw = browser.find_element(By.XPATH, "//input[@name='passwordx']")
    passw.send_keys("CW9WFKNn")
    sleep(3)
    confirm = browser.find_element(By.XPATH, "//button[text()='Conecteaza-te']")
    confirm.click()

def test_add_item(browser):
    # Open the webpage
    browser.get("https://www.cel.ro")
    sleep(1)
    laptop = browser.find_element(By.XPATH, '//a[@class="parentCategName"]')
    laptop.click()
    sleep(1)
    # Open laptop category 2
    laptops = browser.find_element(By.CSS_SELECTOR, 'a.category[href="https://www.cel.ro/laptop-laptopuri/"]')
    laptops.click()
    addproduct = browser.find_element(By.XPATH, '//*[@id="bodycode"]/div[3]/div[1]/div[2]/div[1]/a/span')
    addproduct.click()
    sleep(2)

def test_remove_item(browser):
    browser.get("https://www.cel.ro")
    sleep(3)
    laptop = browser.find_element(By.XPATH, '//a[@class="parentCategName"]')
    laptop.click()
    sleep(2)
    laptops = browser.find_element(By.CSS_SELECTOR, 'a.category[href="https://www.cel.ro/laptop-laptopuri/"]')
    laptops.click()
    addproduct = browser.find_element(By.XPATH, '//*[@id="bodycode"]/div[3]/div[1]/div[2]/div[1]/a/span')
    addproduct.click()
    sleep(2)
    removeitem = browser.find_element(By.XPATH, "//a[@title='Sterge din cos']")
    removeitem.click()
    sleep(2)

def test_search(browser):
    browser.get("https://www.cel.ro")
    sleep(3)
    # Select search
    search = browser.find_element(By.XPATH, '//*[@id="keyword"]')
    search.send_keys("Acer")
    iconsearch = browser.find_element(By.CLASS_NAME, "icon-search")
    iconsearch.click()
    sleep(3)

def test_filter_laptop_price(browser):
    browser.get("https://www.cel.ro")
    sleep(3)
    laptop = browser.find_element(By.XPATH, '//a[@class="parentCategName"]')
    laptop.click()
    sleep(2)
    laptops = browser.find_element(By.CSS_SELECTOR, 'a.category[href="https://www.cel.ro/laptop-laptopuri/"]')
    laptops.click()
    sortare = browser.find_element(By.ID, "sortare")
    sortare.click()
    byprice = browser.find_element(By.XPATH, '//*[@id="sortare"]/option[3]')
    byprice.click()

def test_check_produsele_zilei(browser):
    browser.get("https://www.cel.ro")
    sleep(2)
    produse = browser.find_element(By.CSS_SELECTOR, "a.oferte")
    produse.click()

def test_youtube_redirect(browser):
    # Open the webpage
    browser.get("https://www.cel.ro")
    sleep(3)
    produse = browser.find_element(By.CSS_SELECTOR, "a.oferte")
    produse.click()
    sleep(3)
    youtube = browser.find_element(By.CSS_SELECTOR, "i.icon-youtube")
    youtube.click()
    browser.switch_to.window(browser.window_handles[-1])
    assert "https://consent.youtube.com" in browser.current_url, "Not redirected to youtube"
    sleep(3)

def test_facebook_redirect(browser):
    browser.get("https://www.cel.ro")
    sleep(3)
    produse = browser.find_element(By.CSS_SELECTOR, "a.oferte")
    produse.click()
    sleep(3)
    facebook = browser.find_element(By.CSS_SELECTOR, "i.icon-facebook")
    facebook.click()
    browser.switch_to.window(browser.window_handles[-1])
    assert "https://www.facebook.com/2celro" in browser.current_url, "Not redirected to youtube"

def test_log_out(browser):
    browser.get("https://www.cel.ro")
    sleep(2)
    user = browser.find_element(By.CSS_SELECTOR, "span.icon-wrapper > i.icon-icon_user")
    user.click()
    logout = browser.find_element(By.XPATH, '//*[@id="login_header2"]/div/a[5]')
    logout.click()
    sleep(3)

if __name__ == "__main__":
    pytest.main()


