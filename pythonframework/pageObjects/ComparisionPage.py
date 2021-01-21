import time
from selenium.webdriver.common.by import By
from constants import web_page_locators as const
from utilites.BaseClass import BaseClass


class ComparisionPage(BaseClass):
    '''
    Class contains the methods for comparision page of mobiles.
    '''
    _click_add_mobile = (By.CSS_SELECTOR, const.CLICK_ADD_MOBILE_BY_CSS)
    _enter_mobile_name = (By.XPATH,const.VALIDATE_MOBILE_NAME_BY_XPATH)
    _select_mobile_name = (By.XPATH,const.SELECT_MOBILE_NAME_BY_XPATH)
    _battery_info = (By.XPATH,const.BATTERY_INFO_BY_XPATH)
    _device_names = (By.XPATH,const.DEVICE_NAMES_BY_XPATH)

    def __init__(self,driver):
        '''
        Initialize class object
        :param driver: Instance of webdriver
        '''
        self.driver = driver

    def click_add_mobile(self,name_to_search):
        '''
        Click on add mobile buttona and searched for given mobile to compare
        :param name_to_search (str): Name of mobile to search
        :return: None
        '''
        self.driver.find_element(*ComparisionPage._click_add_mobile).send_keys(name_to_search)
        assert self.driver.find_element(*ComparisionPage._click_add_mobile).get_property("value") == name_to_search, "Mobile name mismatched"
        self.wait_until_element_is_present(self._select_mobile_name[1]).click()
        self.wait_until_element_is_present(self._enter_mobile_name[1])

    def get_battery_info(self):
        '''
        Get the battery details for the compared mobiles.
        :return (dictionary): dictionary of mobile names and battery rating.
        '''
        dict={}
        device_names_list=[]
        battery_info_list=[]
        device_names=self.driver.find_elements(*ComparisionPage._device_names)
        for device in device_names:
            device_names_list.append(device.text)
        print(device_names_list)

        battery_value=self.driver.find_elements(*ComparisionPage._battery_info)
        for battery in battery_value:
            battery_info_list.append(battery.text)
        print(battery_info_list)

        assert len(device_names_list)==len(battery_info_list),"Mobile Names and Battery Rating both lists should be Equal in length"
        dict['Mobile Names']=device_names_list
        dict['Battery Rating']=battery_info_list
        print(dict)
        return dict
