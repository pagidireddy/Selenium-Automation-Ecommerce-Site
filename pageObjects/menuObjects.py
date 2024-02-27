from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Menu:
    lnk_pccomp_xpath = "//span[normalize-space()='PC Components']"
    lnk_processor_xpath = "//span[normalize-space()='Processor/ CPU']"
    lnk_motherboard_xpath = "//span[@class='links-text'][normalize-space()='Motherboard']"
    lnk_ram_xpath = "//span[normalize-space()='Memory/ RAM']"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def pcCompProcessor(self):
        menu1 = self.driver.find_element(By.XPATH, self.lnk_pccomp_xpath)
        self.actions.move_to_element(menu1).perform()
        self.driver.find_element(By.XPATH, self.lnk_processor_xpath).click()

    def pcComMotherboard(self):
        menu1 = self.driver.find_element(By.XPATH, self.lnk_pccomp_xpath)
        self.actions.move_to_element(menu1).perform()
        self.driver.find_element(By.XPATH, self.lnk_motherboard_xpath).click()

    def pcComRam(self):
        menu1 = self.driver.find_element(By.XPATH, self.lnk_pccomp_xpath)
        self.actions.move_to_element(menu1).perform()
        self.driver.find_element(By.XPATH, self.lnk_ram_xpath).click()
