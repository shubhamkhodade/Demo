import time

import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

@pytest.mark.usefixtures("setup_edge")
class TestThree(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        log.info("*****Testcase 3 : Search Micromax Mobile*****")
        homePage = HomePage(self.driver)
        name_to_search = self.read_from_excel("test3")
        log.debug(f"Successfully read the mobile name to search from Excel ::{name_to_search['Mobile_name'][0]} ")
        homePage.search_product_and_expect_error_screenshot(name_to_search['Mobile_name'][0])
        log.debug("Successfully taken the sceenshot of the error page")
        log.info("*****END : Testcase 5*****\n")