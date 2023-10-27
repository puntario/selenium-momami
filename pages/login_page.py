from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.login_button = (By.ID, "send2")

    def get_url(self, url):
        self.driver.get(url)

    def input_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()