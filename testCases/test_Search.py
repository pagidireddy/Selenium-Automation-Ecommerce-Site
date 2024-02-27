import pytest
from pageObjects.SearchLocators import Search
from utilities.customLogger import LogGenerator
from utilities.readConfigs import ReadConfig
from utilities import XLFileHelper
from utilities.screenshotGen import Screenshot


@pytest.mark.smoke
class TestSearch:
    url = ReadConfig.getUrl()
    logger = LogGenerator.loggen()
    file = ".\\TestData\\ProductsList.xlsx"

    def test_1_search(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.s = Search(self.driver)
        self.logger.info("TestCase01 Checking Search")
        status = []
        x = XLFileHelper.getRowCount(self.file, "Products")
        for i in range(2, x + 1):
            p = XLFileHelper.readData(self.file, "Products", i, 1)
            self.s = Search(self.driver)
            self.s.perform_search(p)
            # time.sleep(1)
            act_tittle = self.driver.title
            if p in act_tittle:
                self.s.clear_searchbox(len(p))
                status.append("Pass")
            else:
                self.s.clear_searchbox(len(p))
                status.append("Fail")
        if "Fail" not in status:
            self.logger.info("TestCase01 Checking Search Success")
            self.driver.close()
            assert True
        else:
            Screenshot.take_screenshot(self.driver)
            self.logger.error("TestCase01 Checking Search Fail")
            self.driver.close()
            assert False
