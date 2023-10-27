from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.track_order = (By.XPATH, "//a[@href = 'https://track.kanmogroup.com/']")
        self.logo_momami = (By.XPATH, "//img[@src = 'https://momami.co.id/media/logo/websites/19/Momami_2_.jpeg']")
        self.search_bar = (By.ID, "search")
        self.search_button = (By.XPATH, "//button[@type = 'submit']")
        self.wishlist_button = (By.XPATH, "//a[@class = 'action toggle switcher-trigger']")
        self.product_sample = (By.XPATH, "//a[@class = 'product-item-photo']")
        self.add_to_cart_button = (By.XPATH, "//body/div[1]/main[1]/div[3]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
        self.cart_button = (By.XPATH, "//a[@class = 'action showcart']")
        self.go_to_cart_button = (By.XPATH, "//a[@class = 'action viewcart']")
        self.checkout_button = (By.ID, "top-cart-btn-checkout")
        self.profile_logo_header = (By.XPATH, "//header/div[2]/div[3]/div[3]/a[1]")
        self.login_menu_header = (By.XPATH, "//header/div[2]/div[3]/div[3]/div[1]/ul[1]/li[1]/a[1]")
        self.logout_menu_header = (By.XPATH,"//a[contains(text(),'Keluar')]")

    def get_url(self, url):
        self.driver.get(url)

    def click_track_order(self):
        self.driver.find_element(*self.track_order).click()

    def click_logo(self):
        self.driver.find_element(*self.logo_momami).click()

    def input_search(self, search):
        self.driver.find_element(*self.search_bar).send_keys(search)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def click_wishlist(self):
        self.driver.find_element(*self.wishlist_button).click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.go_to_cart_button).click()

    def checkout_header(self):
        self.driver.find_element(*self.checkout_button).click()

    def click_profile(self):
        self.driver.find_element(*self.profile_logo_header).click()

    def click_login_header(self):
        self.driver.find_element(*self.login_menu_header).click()

    def click_logout_header(self):
        self.driver.find_element(*self.logout_menu_header).click()
