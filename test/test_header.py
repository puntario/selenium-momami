import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


def test_order_tracking(driver):
    home_page = HomePage(driver)
    home_page.get_url("https://momami.co.id/")
    home_page.click_track_order()

    assert "https://track.kanmogroup.com/" == driver.current_url


def test_logo(driver):
    home_page = HomePage(driver)
    home_page.get_url("https://momami.co.id/contact-us/")
    home_page.click_logo()

    assert "https://momami.co.id/" == driver.current_url


def test_search(driver):
    home_page = HomePage(driver)
    home_page.get_url("https://momami.co.id/")
    driver.maximize_window()
    home_page.input_search("hair")
    time.sleep(5)
    home_page.click_search()

    assert driver.find_element(By.XPATH, "//div[@class = 'search results']").is_displayed()


def test_wishlist_loggedin(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.get_url("https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/")
    login_page.input_email("test2033@mailinator.com")
    login_page.input_password("Test2033-")
    login_page.click_login()
    time.sleep(6)
    home_page.click_wishlist()
    time.sleep(3)

    assert "https://momami.co.id/wishlist/" == driver.current_url


def test_cart_go_to_bag(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    action = ActionChains(driver)

    login_page.get_url("https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/")
    login_page.input_email("test2033@mailinator.com")
    login_page.input_password("Test2033-")
    login_page.click_login()
    time.sleep(4)
    action.move_to_element(driver.find_element(By.XPATH, "//a[@href = 'https://momami.co.id/momami-baby-antibacterial-wipes-tisu-basah-anti-bakteri-bayi-30-lembar-52120140-mmm002.html']")).perform()
    home_page.add_to_cart()
    home_page.click_cart()
    home_page.go_to_cart()

    assert "https://momami.co.id/checkout/cart/" == driver.current_url


def test_cart_checkout(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    action = ActionChains(driver)

    login_page.get_url("https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/")
    login_page.input_email("test2033@mailinator.com")
    login_page.input_password("Test2033-")
    login_page.click_login()
    time.sleep(4)
    action.move_to_element(driver.find_element(By.XPATH, "//a[@href = 'https://momami.co.id/momami-baby-antibacterial-wipes-tisu-basah-anti-bakteri-bayi-30-lembar-52120140-mmm002.html']")).perform()
    home_page.add_to_cart()
    home_page.click_cart()
    home_page.checkout_header()

    assert "https://momami.co.id/onestepcheckout/" == driver.current_url


def test_login_header(driver):
    home_page = HomePage(driver)

    home_page.get_url("https://momami.co.id/")
    home_page.click_profile()
    home_page.click_login_header()

    assert "https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/" == driver.current_url


def test_logout(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.get_url("https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/")
    login_page.input_email("test2033@mailinator.com")
    login_page.input_password("Test2033-")
    login_page.click_login()
    time.sleep(4)
    home_page.click_profile()
    home_page.click_logout_header()

    assert "https://momami.co.id/customer/account/logoutSuccess/" == driver.current_url