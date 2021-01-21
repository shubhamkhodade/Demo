import time

from selenium.webdriver.common.by import By
from constants import web_page_locators as const
from pageObjects.ComparisionPage import ComparisionPage
from pageObjects.PhonefinderPage import PhonefinderPage
from pageObjects.SpecificationPage import SpecificationPage
from utilites.BaseClass import BaseClass


class HomePage(BaseClass):
    '''
        Class contains the methods for HomePage of 99mobiles.com.
    '''
    _click_compare = (By.XPATH,const.CLICK_COMPARE_BY_XPATH)
    _click_mobile_compare = (By.XPATH,const.CLICK_MOBILE_COMPARE_BY_XPATH)
    _find_mobile_min_range = (By.XPATH,const.FIND_MOBILES_MIN_BY_XPATH)
    _find_mobile_max_range = (By.XPATH,const.FIND_MOBILES_MAX_BY_XPATH)
    _click_find_mobiles_by_range = (By.XPATH,const.CLICK_FIND_MOBILES_BY_XPATH)
    _search_products = (By.XPATH,const.SEARCH_PRODUCTS_BY_XPATH)
    _search_mobile = (By.XPATH,const.SEARCH_MOBILE_BY_PATH)

    def __init__(self,driver):
        '''
            Initialize class object
            :param driver: Instance of webdriver
         '''
        self.driver = driver

    def click_compare(self):
        '''
        Click on comare mobile button
        :return: None
        '''
        return self.driver.find_element(*HomePage._click_compare)

    def click_mobile_compare(self):
        '''
        Click on names of mobile to compare
        :return (object): object of the nextpage i.e comparision page
        '''
        self.element_is_clickable(self._click_mobile_compare[1]).click()
        comparisionpage = ComparisionPage(self.driver)
        return comparisionpage

    def select_range(self,min,max):
        '''
        Select the price range for the mobiles to search
        :return (object): object of the next page i.e phonefinder page
        '''
        self.wait_until_element_is_present(self._find_mobile_min_range[1]).clear()
        self.driver.find_element(*HomePage._find_mobile_min_range).send_keys(min)
        self.wait_until_element_is_present(self._find_mobile_max_range[1]).clear()
        self.driver.find_element(*HomePage._find_mobile_max_range).send_keys(max)
        elm = self.element_is_clickable(self._click_find_mobiles_by_range[1])
        elm.click()
        phonefinderpage = PhonefinderPage(self.driver)
        return phonefinderpage

    def search_for_product(self,product_name):
        '''
        Search for the given product name in search box.
        :param product_name (str): Name of mobile to search
        :return (object): object of the next page i.e specification page
        '''
        self.driver.find_element(*HomePage._search_products).send_keys(product_name)
        assert self.driver.find_element(*HomePage._search_products).get_property("value") == product_name, "Mobile name mismatched"
        self.wait_until_element_is_present(self._search_mobile[1]).click()
        specificationpage = SpecificationPage(self.driver)
        return specificationpage

    def search_product_and_expect_error_screenshot(self,product_name):
        '''
        Search for the given product name in search box and expect error and take sceenshot of the webpage.
        :param product_name (str): Name of mobile to search
        :return (object): object of the next page i.e specification page
        '''
        self.driver.find_element(*HomePage._search_products).send_keys(product_name)
        assert self.driver.find_element(*HomePage._search_products).get_property("value") != product_name, "Mobile name mismatched"
