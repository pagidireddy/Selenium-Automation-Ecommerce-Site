from selenium.webdriver.common.by import By


class HeaderLinks:
    lnk_contactsus_xpath = "//a[span[contains(text(), 'Contact')]]"
    lnk_aboutus_xpath = "//a[span[contains(text(), 'About Us')]]"
    lnk_faq_xpath = "//a[span[contains(text(), 'FAQ')]]"
    lnk_tandc_xpath = "//a[span[contains(text(), 'T&C')]]"

    def __init__(self, driver):
        self.driver = driver

    def contact(self):
        self.driver.find_element(By.XPATH, self.lnk_contactsus_xpath).click()

    def about(self):
        self.driver.find_element(By.XPATH, self.lnk_aboutus_xpath).click()

    def faq(self):
        self.driver.find_element(By.XPATH, self.lnk_faq_xpath).click()

    def tc(self):
        self.driver.find_element(By.XPATH, self.lnk_tandc_xpath).click()
