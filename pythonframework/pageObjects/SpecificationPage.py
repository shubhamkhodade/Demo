from selenium.webdriver.common.by import By

from utilites.BaseClass import BaseClass
from constants import web_page_locators as const

class SpecificationPage(BaseClass):
    '''
        Class contains the methods for Specification page.
    '''
    _click_full_spec = (By.XPATH,const.SELECT_SEE_SPEC_BY_XPATH)
    _display_name = (By.XPATH,const.DISPLAY_NAME_BY_XPATH)
    _get_display_info = (By.XPATH,const.GET_DISPLAY_INFO_BY_XPATH)

    def __init__(self, driver):
        '''
            Initialize class object
            :param driver: Instance of webdriver
        '''
        self.driver = driver

    def see_full_spec(self):
        '''
        Click on see full spec
        :return: None
        '''
        self.wait_until_element_is_present(self._click_full_spec[1]).click()
        self.wait_until_element_is_present(self._display_name[1])

    def get_display_info(self,mobile_name):
        '''
        Get the display information of the searched mobile.
        :param mobile_name (str): name of the mobile
        :return (dictionary): dictionary of the mobile name and display info
        '''
        dict={}
        display_info = self.driver.find_element(*SpecificationPage._get_display_info).text
        dict['Mobile_name'] = [mobile_name]
        dict['Display'] = [display_info]
        return dict