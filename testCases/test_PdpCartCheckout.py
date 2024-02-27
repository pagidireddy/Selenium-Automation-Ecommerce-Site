import pytest
from pageObjects.SearchLocators import *
from utilities.customLogger import LogGenerator
from utilities.screenshotGen import Screenshot
from utilities.readConfigs import ReadConfig


@pytest.mark.smoke
@pytest.mark.regression
class TestPdpAndCart:
    url = ReadConfig.getUrl()
    product = "I9 14900"
    logger = LogGenerator.loggen()

    def test_pdpAndcart(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.s = Search(self.driver)
        self.s.perform_search(self.product)
        self.logger.info("TestCase01 Checking Product Description Page")
        self.s.pdp_page()
        self.logger.info("TestCase01 Checking Add to Cart")
        self.s.addtocart()
        self.logger.info("TestCase01 Checking View Cart")
        self.s.viewcart()
        self.logger.info("TestCase01 Checking Checkout Page")
        self.s.checkout()
        if "Quick Checkout" == self.driver.title:
            self.logger.info("TestCase01 All Check passed upto Checkout Page")
            self.driver.close()
            assert True
        else:
            self.logger.info("TestCase01 Checking Checkout Fail")
            Screenshot.take_screenshot(self.driver)
            assert False
