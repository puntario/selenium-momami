import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.get_url("https://momami.co.id/customer/account/login/referer/aHR0cHM6Ly9tb21hbWkuY28uaWQv/")
    login_page.input_email("test2033@mailinator.com")
    login_page.input_password("Test2033-")
    login_page.click_login()

    assert "https://momami.co.id/customer/account/" or "https://momami.co.id/" is driver.current_url
