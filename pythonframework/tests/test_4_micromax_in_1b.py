import pytest

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestFour(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        log.info("*****Testcase 4 : Validate Micromax IN 1B is present*****")
        homePage = HomePage(self.driver)
        phonefinderpage = homePage.select_range(6000,8000)
        log.debug("Successfully selected the range")
        log.debug("User is nevigated to Phone Finder Page")
        phonefinderpage.select_micromax_brand()
        log.debug("Successfully selected the Micromax as a brand")
        name_to_search = self.read_from_excel("test4")
        log.debug(f"Successfully read the mobile name to search from Excel ::{name_to_search['Mobile_Name'][0]}")
        is_present = phonefinderpage.traverse_and_validate_presence_of_mobile(name_to_search['Mobile_Name'][0])
        if is_present:
            log.debug(f"{name_to_search['Mobile_Name'][0]} is present")
        else:
            log.debug(f"{name_to_search['Mobile_Name'][0]} is not present")
        log.info("*****END : Testcase 4*****\n")