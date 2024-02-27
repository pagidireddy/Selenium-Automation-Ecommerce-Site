from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sort:
    lowtohigh_xpath = "//option[contains(text(), 'Price (Low > High)')]"
    hightolow_xpath = "//option[contains(text(), 'Price (High > Low)')]"
    firstproductprice_xpath = "(//span[@class='price-new'])[1]"
    secondproductprice_xpath = "(//span[@class='price-new'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def lowtohigh(self):
        self.driver.find_element(By.XPATH, self.lowtohigh_xpath).click()
        price = self.driver.find_element(By.XPATH, self.firstproductprice_xpath)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(price))
        price = self.driver.find_element(By.XPATH, self.firstproductprice_xpath).text
        price2 = self.driver.find_element(By.XPATH, self.secondproductprice_xpath).text
        return price, price2

    def hightolow(self):
        self.driver.find_element(By.XPATH, self.hightolow_xpath).click()
        price = self.driver.find_element(By.XPATH, self.firstproductprice_xpath)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(price))
        price = self.driver.find_element(By.XPATH, self.firstproductprice_xpath).text
        price2 = self.driver.find_element(By.XPATH, self.secondproductprice_xpath).text
        return price, price2
