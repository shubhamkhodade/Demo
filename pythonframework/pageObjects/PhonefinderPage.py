import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from conftest import _capture_screenshot
from utilites.BaseClass import BaseClass
from constants import web_page_locators as const

class PhonefinderPage(BaseClass):
    '''
    Class contains the methods for Phonefinder page of mobiles.
    '''
    _select_popular_brands = (By.XPATH,const.SELECT_CHECKBOX_POPULAR_BRANDS_BY_XPATH)
    _validate_price_range = (By.XPATH,const.VALIDATE_PRICE_RANGE_BY_XPATH)
    _mobile_names = (By.XPATH,const.MOBILE_NAMES_BY_XPATH)
    _mobile_prices = (By.XPATH,const.MOBILE_PRICE_BY_XPATH)
    _select_micromax_brand = (By.XPATH,const.SELECT_BRAND_MICROMAX_BY_XPATH)
    _mobile_names_scroll = (By.XPATH,const.MOBILE_NAMES_SCROLL_BY_XPATH)
    _mobile_to_search = (By.XPATH,const.MOBILE_TO_SEARCH)
    _click_next = (By.XPATH,const.CLICK_NEXT_BY_XPATH)

    def __init__(self,driver):
        '''
            Initialize class object
            :param driver: Instance of webdriver
        '''
        self.driver = driver

    def select_popular_brands(self):
        '''
        Click on the select popular brands checkbox
        :return: None
        '''
        elm = self.element_is_clickable(self._select_popular_brands[1])
        elm.click()
        assert elm.is_selected()
        assert self.wait_until_element_is_present(self._validate_price_range[1])


    def get_mobiles_and_prices(self):
        '''
        Get the names of mobiles for selected range and their prices
        :return (dictionary): dictionary  of mobile names and prices
        '''
        dict = {}
        device_names_list = []
        device_price_list = []

        assert self.wait_until_element_is_present(self._mobile_names[1])
        device_names = self.driver.find_elements(*PhonefinderPage._mobile_names)
        for device in device_names:
            device_names_list.append(device.text)
        print(device_names_list)
        assert len(device_names_list),"Device names list cannot be empty"

        assert self.wait_until_element_is_present(self._mobile_prices[1])
        device_price = self.driver.find_elements(*PhonefinderPage._mobile_prices)
        for price in device_price:
            device_price_list.append(price.text)
        print(device_price_list)
        assert len(device_price_list), "Device price list cannot be empty"

        assert len(device_names_list) == len(device_price_list), "Mobile Names and Price both lists should be Equal in length"
        dict['Mobile Names'] = device_names_list
        dict['Price'] = device_price_list
        print(dict)
        return dict

    def select_micromax_brand(self):
        '''
        Click on the micromax checkbox as brand
        :return: None
        '''
        elm = self.element_is_clickable(self._select_micromax_brand[1])
        elm.click()
        assert elm.is_selected()
        assert self.wait_until_element_is_present(self._validate_price_range[1]).text,"Micromax"

    def traverse_and_validate_presence_of_mobile(self,mobile_name):
        '''
        Validate presence of Mobile until not found
        :return:
        '''
        flag = True
        page = 1
        while flag:
            assert self.wait_until_element_is_present(self._mobile_names[1])
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            if page == 1:
                assert self.wait_until_element_is_present(self._mobile_names_scroll[1])
            try:
                is_present = self.driver.find_element(*PhonefinderPage._mobile_to_search)
                if is_present:
                    print("mobile is on : " + page)
                    flag= False
                    return True
            except:
                try:
                    page+=1
                    self.wait_until_element_is_present(self._click_next[1]).click()
                except:
                    print("Mobile is not found on all pages")
                    flag= False
                    return False

