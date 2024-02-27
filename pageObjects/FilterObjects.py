from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Filters:
    btn_clr_xpath = "//button[text()='Clear']"
    tglbtn_price_xpath = "//a[contains(text(),'Price')]"
    txt_price_min_xpath = "//input[@name='min']"
    txt_price_max_xpath = "//input[@name='max']"
    tglbtn_brand_xpath = "//a[contains(text(),'Brands')]"
    tglbtn_memorysize_xpath = "//a[normalize-space()='Memory Size']"
    tglbtn_cores_xpath = "//a[normalize-space()='Cores']"
    brandlist_xpath = "//div[@class='module-item module-item-m panel panel-active']//label"
    tglbtn_series_xpath = "//a[normalize-space()='Series']"
    serieslist_xpath = "//div[@class='module-item module-item-f8 panel panel-active']//label"
    firstproductname_xpath = "(//div[contains(@class,'name')])[1]"
    firstproductprice_xpath = "(//span[@class='price-new'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def clearfilters(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.btn_clr_xpath))
        )
        self.driver.find_element(By.XPATH, self.btn_clr_xpath).click()

    def pricefilter(self, min, max):
        toggle_element = self.driver.find_element(By.XPATH, self.tglbtn_price_xpath)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.tglbtn_price_xpath))
        )
        if not toggle_element.get_attribute("aria-expanded") == "true":
            toggle_element.click()
        minprice = self.driver.find_element(By.XPATH, self.txt_price_min_xpath)
        minprice.clear()
        minprice.send_keys(min)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.txt_price_max_xpath))
        )
        maxprice = self.driver.find_element(By.XPATH, self.txt_price_max_xpath)
        maxprice.clear()
        maxprice.send_keys(max)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(maxprice))
        x = self.driver.current_url
        return x

    def brandsfilter(self):
        toggle_element = self.driver.find_element(By.XPATH, self.tglbtn_brand_xpath)
        if not toggle_element.get_attribute("aria-expanded") == "true":
            toggle_element.click()
        base_xpath = self.brandlist_xpath
        base_xpath1 = self.driver.find_elements(By.XPATH, base_xpath)
        lst = len(base_xpath1)
        items = []
        brands = []
        for i in range(1, lst + 1):
            bases_xpath = base_xpath + f"[{i}]"
            brandelement = self.driver.find_element(By.XPATH, bases_xpath)
            self.driver.find_element(By.XPATH, bases_xpath).click()
            WebDriverWait(self.driver, 10).until(EC.staleness_of(brandelement))
            brand = self.driver.find_element(By.XPATH, bases_xpath).text
            item = self.driver.find_element(By.XPATH, self.firstproductname_xpath).text
            itemelement = self.driver.find_element(By.XPATH, self.firstproductname_xpath)
            self.clearfilters()
            WebDriverWait(self.driver, 10).until(EC.staleness_of(itemelement))
            items.append(item)
            brands.append(brand)
        return brands, items

    def seriesfilter(self):
        toggle_element = self.driver.find_element(By.XPATH, self.tglbtn_series_xpath)
        if not toggle_element.get_attribute("aria-expanded") == "true":
            toggle_element.click()
        serieslst = self.driver.find_elements(By.XPATH, self.serieslist_xpath)
        seriessize = len(serieslst)
        sirieslst = []
        items = []
        for ele in range(1, seriessize + 1):
            dynamic_xpath = self.serieslist_xpath + f"[{ele}]"
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.XPATH, dynamic_xpath)))
            element.click()
            verifyfirstproduct = self.driver.find_element(By.XPATH, self.firstproductname_xpath)
            WebDriverWait(self.driver, 10).until(EC.staleness_of(verifyfirstproduct))
            series = self.driver.find_element(By.XPATH, dynamic_xpath).text
            item = self.driver.find_element(By.XPATH, self.firstproductname_xpath).text
            sirieslst.append(series)
            items.append(item)
            self.driver.find_element(By.XPATH, dynamic_xpath).click()
            firstproduct = self.driver.find_element(By.XPATH, self.firstproductname_xpath)
            WebDriverWait(self.driver, 10).until(EC.staleness_of(firstproduct))
        return sirieslst, items
