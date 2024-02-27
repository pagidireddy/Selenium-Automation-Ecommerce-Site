from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    icon_search_ByXpath = "//button[@class='dropdown-toggle search-trigger']"
    txt_search_ByXpath = "//input[@name='search']"
    product_xpath = "(//div[@class = 'name'])[1]"
    btn_addtocart_xpath = "//a[@id='button-cart']"
    btn_popcart_xpath = "//a[contains(text(), 'View Cart')]"
    btn_maincart_xpath = "//i[@class='fa fa-shopping-cart']"
    btn_checkout_xpath = "(//span[contains(text(),'Checkout')])[2]"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def perform_search(self, product):
        icon = self.driver.find_element(By.XPATH, self.icon_search_ByXpath)
        txtbox = self.driver.find_element(By.XPATH, self.txt_search_ByXpath)
        self.actions.move_to_element(icon).perform()
        self.actions.move_to_element(txtbox).perform()
        txtbox.send_keys(product, Keys.ENTER)

    def clear_searchbox(self, clear):
        icon = self.driver.find_element(By.XPATH, self.icon_search_ByXpath)
        txtbox = self.driver.find_element(By.XPATH, self.txt_search_ByXpath)
        self.actions.move_to_element(icon).perform()
        self.actions.move_to_element(txtbox).perform()
        txtbox.send_keys(Keys.BACKSPACE * clear)

    def pdp_page(self):
        self.driver.find_element(By.XPATH, self.product_xpath).click()

    def addtocart(self):
        self.driver.find_element(By.XPATH, self.btn_addtocart_xpath).click()

    def viewcart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.btn_popcart_xpath)))
        self.driver.find_element(By.XPATH, self.btn_popcart_xpath).click()

    def checkout(self):
        self.driver.find_element(By.XPATH, self.btn_checkout_xpath).click()
