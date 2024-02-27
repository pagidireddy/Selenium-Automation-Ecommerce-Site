import pytest
from pageObjects.FilterObjects import Filters
from pageObjects.menuObjects import Menu
from utilities.customLogger import LogGenerator
from utilities.readConfigs import ReadConfig
from utilities.screenshotGen import Screenshot


@pytest.mark.smoke
class TestFilters:
    url = ReadConfig.getUrl()
    logger = LogGenerator.loggen()

    def test_price(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.m = Menu(self.driver)
        self.m.pcComRam()
        self.filter = Filters(self.driver)
        self.logger.info("TestCase01 Checking price filter")
        minprice = ReadConfig.get_random_min_price()
        maxprice = ReadConfig.get_random_max_price()
        x = self.filter.pricefilter(minprice, maxprice)
        if f"{minprice}" and f"{maxprice}" in x:
            self.logger.info("TestCase01 Checking price filter Success")
            self.driver.close()
            assert True
        else:
            self.logger.info("TestCase01 Checking price filter Fail")
            self.driver.close()
            assert False

    def test_brandsfilter(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.maximize_window()
        Menu(self.driver).pcComMotherboard()
        self.filter = Filters(self.driver)
        self.logger.info("TestCase02 Checking brands filter")
        x = self.filter.brandsfilter()
        status = []
        for i in range(len(x[0])):
            if x[0][i] in x[1][i]:
                status.append("Pass")
            else:
                status.append("Fail")
        if "Fail" not in status:
            self.logger.info("TestCase02 Checking brands filter Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.info("TestCase02 Checking brands filter Fail")
            self.driver.close()
            assert False

    def test_seriesfilter(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.m = Menu(self.driver)
        self.m.pcCompProcessor()
        self.filter = Filters(self.driver)
        self.logger.info("TestCase03 Checking Series filter")
        x = self.filter.seriesfilter()
        status = []
        for i in range(len(x[0])):
            if x[0][i] in x[1][i]:
                status.append("Pass")
            else:
                status.append("Fail")
                Screenshot.take_screenshot(self.driver)
        if "Fail" not in status:
            self.logger.info("TestCase03 Checking Series filter Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.info("TestCase03 Checking Series filter Fail")
            self.driver.close()
