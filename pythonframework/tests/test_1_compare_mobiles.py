import time
import unittest

import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        try:
            log = self.get_logger()
            log.info("*****Testcase 1 :Compare Mobile Testcase*****")
            homePage = HomePage(self.driver)
            homePage.click_compare().click()
            comparisionpage = homePage.click_mobile_compare()
            log.debug("Successfully clicked on compare")
            log.debug("User is nevigated to Comparision Page")
            name_to_search = self.read_from_excel("test1")
            log.debug(f"Successfully read the mobile name to search from Excel ::{name_to_search['Mobile_name'][0]}")
            comparisionpage.click_add_mobile(name_to_search['Mobile_name'][0])
            log.debug("Successfully get the mobile name to search from Excel")
            log.debug("User is able to see comparision of selected mobiles")
            dict_of_items = comparisionpage.get_battery_info()
            log.info(dict_of_items)
            log.debug("Successfully get the mobile name and battery rating into dictionary")
            self.write_to_excel(dict_of_items, "test1")
            log.debug("Successfully written data into Excel file from dictionary")
            log.info("*****END : Testcase 1*****\n")
            status = True
        except:
            log.info("Exception in Testcase 1 ")


