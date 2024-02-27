import pytest
from pageObjects.TopHeaders import HeaderLinks
from utilities.customLogger import LogGenerator
from utilities.readConfigs import ReadConfig
from utilities.screenshotGen import Screenshot


@pytest.mark.sanity
class TestContactPage:
    url = ReadConfig.getUrl()
    logger = LogGenerator.loggen()

    def test_1_site(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()       
        self.logger.info("TestCase01 Site Open")
        act_tittle = self.driver.title
        if act_tittle == "Vedant Computers - Shop online for computer hardware, laptop, accessories etc.":
            self.driver.close()
            self.logger.info("TestCase01 Site Open Success")
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase01 Site Open Failure")
            self.driver.close()
            assert False

    def test_2_contact(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestCase02 Checking Contact us")
        self.cu = HeaderLinks(self.driver)
        self.cu.contact()
        act_tittle = self.driver.title
        if act_tittle == "Contact Us":
            self.logger.info("TestCase02 Checking Contact us Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase02 Checking Contact us Failure")
            self.driver.close()
            assert False

    def test_3_about(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestCase03 Checking About us")
        self.cu = HeaderLinks(self.driver)
        self.cu.about()
        act_tittle = self.driver.title
        if act_tittle == "About Us":
            self.logger.info("TestCase03 Checking About us Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase03 Checking About us Failure")
            self.driver.close()
            assert False

    def test_4_faq(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestCase04 Checking FAQ")
        self.cu = HeaderLinks(self.driver)
        self.cu.faq()
        act_tittle = self.driver.title
        if act_tittle == "Frequently Asked Questions":
            self.logger.info("TestCase04 Checking FAQ Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase04 Checking FAQ Failure")
            self.driver.close()
            assert False

    def test_5_tc(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.logger.info("TestCase05 Checking T&C")
        self.cu = HeaderLinks(self.driver)
        self.cu.tc()
        act_tittle = self.driver.title
        if act_tittle == "Terms & Conditions":
            self.logger.info("TestCase05 Checking T&C Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase05 Checking T&C Failure")
            self.driver.close()
            assert False
