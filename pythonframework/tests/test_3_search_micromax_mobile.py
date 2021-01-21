import time

import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestThree(BaseClass):

    def test_e2e(self):
        try:
            log = self.get_logger()
            log.info("*****Testcase 3 : Search Micromax Mobile*****")
            homePage = HomePage(self.driver)
            name_to_search = self.read_from_excel("test3")
            log.debug(f"Successfully read the mobile name to search from Excel ::{name_to_search['Mobile_name'][0]} ")
            specificationpage=homePage.search_for_product(name_to_search['Mobile_name'][0])
            log.debug("Successfully searched for product")
            specificationpage.see_full_spec()
            log.debug("User in nevigated to specifiction page")
            dict_of_items = specificationpage.get_display_info(name_to_search['Mobile_name'][0])
            log.debug("Successfully get the display info into dictionary")
            log.info(dict_of_items)
            self.write_to_excel(dict_of_items, "test3")
            log.debug("Successfully written data into Excel file from dictionary")
            log.info("*****END : Testcase 3*****\n")
        except:
            log.info("Exception in Testcase 3")
