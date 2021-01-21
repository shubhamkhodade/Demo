import inspect
import logging
from pandas import *
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass():
    '''
    Class contains the method which are commonly used.
    '''
    def element_is_clickable(self,text):
        '''
        Web driver wait till the web element is Clickable.
        :param text (str): locator of the webpage
        :return (bool): False if timeout or failed to found element clickable on page otherwise True
        '''
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, text)))
        return element

    def wait_until_element_is_present(self,text):
        '''
        Web driver wait till the web element is Present.
        :param text (str): locator of the webpage
        :return (bool): False if timeout or failed to found element clickable on page otherwise True
               '''
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, text)))
        return element

    def get_logger(self):
        '''
        Creating instance of logging.
        :return: logger object
        '''
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.handlers.clear()
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        return logger

    def read_from_excel(self,testcase_no):
        '''
        Function returns dictionary of data as per work sheet.
        :param testcase_no (str) : No. of testcase
        :return (dictionary): dictionary of values
        '''

        if testcase_no == 'test1':
            xls = ExcelFile('../Excel_files/testcase_1_compare_mobiles_input_data.xlsx')
        elif testcase_no == 'test3':
            xls = ExcelFile('../Excel_files/testcase_3_search_micromax_mobile_input_data.xlsx')
        elif testcase_no == "test4":
            xls = ExcelFile('../Excel_files/testcase_4_validate_presense_of_mobile_input_data.xlsx')
        elif testcase_no == 'cross_browser_testing':
            xls = ExcelFile('../Excel_files/cross_browser_testing.xlsx')

        data = xls.parse(xls.sheet_names[0])
        d =data.to_dict()
        return d

    def write_to_excel(self,dict_of_items,testcase_no):
        '''
        Writes the data into the excel sheet.
        :param dict_of_items (dictionary): dictionary of values
        :param testcase_no (str): No. of testcase
        :return: None
        '''
        import pandas as pd
        mobile_info=pd.DataFrame(dict_of_items)
        mobile_sheet = {'Result': mobile_info}
        if testcase_no == 'test1':
             writer = pd.ExcelWriter('../Excel_files/testcase_1_compare_mobiles_result.xlsx', engine='openpyxl')
        elif testcase_no == 'test2':
            writer = pd.ExcelWriter('../Excel_files/testcase_2_price_range_result.xlsx', engine='openpyxl')
        elif testcase_no == 'test3':
            writer = pd.ExcelWriter('../Excel_files/testcase_3_search_micromax_mobile_result.xlsx', engine='openpyxl')

        for sheet_name in mobile_sheet.keys():
            mobile_sheet[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()