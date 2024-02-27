import pytest
from utilities.customLogger import LogGenerator
from pageObjects.sortObjects import Sort
from pageObjects.menuObjects import Menu
from utilities.readConfigs import ReadConfig
from utilities.screenshotGen import Screenshot


@pytest.mark.smoke
@pytest.mark.regression
class TestSort:
    url = ReadConfig.getUrl()
    logger = LogGenerator.loggen()

    def testLowtoHigh(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        Menu(self.driver).pcCompProcessor()
        self.logger.info("TestCase01 Checking Sort  Price Low to High")
        x = Sort(self.driver).lowtohigh()
        prices = []
        for i in range(len(x)):
            price = float(x[i].replace("₹", "").replace(",", ""))
            prices.append(price)
        if prices[0] < prices[1]:
            self.logger.info("TestCase01 Checking Sort  Price Low to High Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase01 Checking Sort  Price Low to High Fail")
            self.driver.close()
            assert False

    def testHightoLow(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        Menu(self.driver).pcComMotherboard()
        self.logger.info("TestCase02 Checking Sort  Price High to Low")
        x = Sort(self.driver).hightolow()
        prices = []
        for i in range(len(x)):
            price = float(x[i].replace("₹", "").replace(",", ""))
            prices.append(price)
        if prices[0] > prices[1]:
            self.logger.info("TestCase02 Checking Sort  Price High to Low Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase02 Checking Sort  Price High to Low Fail")
            self.driver.close()
            assert False
