import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass
import time
@pytest.mark.usefixtures("setup_edge")
class TestTwo(BaseClass):

    def test_e2e(self):
        try:
            log = self.get_logger()
            log.info("*****Testcase 2 : Price range*****")
            homePage = HomePage(self.driver)
            phonefinderpage = homePage.select_range(2000,30000)
            log.debug("Successfully selected the range")
            log.debug("User is nevigated to Phone Finder Page")
            phonefinderpage.select_popular_brands()
            log.debug("Successfully selected the popular brands")
            dict_of_mobiles = phonefinderpage.get_mobiles_and_prices()
            log.info(dict_of_mobiles)
            log.debug("Successfully get the mobile names and prices into dictionary")
            self.write_to_excel(dict_of_mobiles,"test2")
            log.debug("Successfully written data into Excel file from dictionary")
            log.info("*****END : Testcase 2*****\n")
        except:
            log.info("Exception in Testcase 2")
