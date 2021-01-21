# write fixtures which are commonly used in testcases here

import pytest
from selenium import webdriver

from utilites.BaseClass import BaseClass

ex = BaseClass()
driver = None

# to get brower name from cmd line and got from https://docs.pytest.org/en/latest/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    dict_of_items = ex.read_from_excel("cross_browser_testing")
    print(dict_of_items)
    list_of_headers=[]
    import os
    wd =os.getcwd()
    print(wd)
    for key in dict_of_items.keys():
        list_of_headers.append(key)
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r'C:\Users\112285\chromedriver.exe')
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=r'C:\Users\112285\msedgedriver.exe')
    driver.maximize_window()
    driver.get('https://www.91mobiles.com/')
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def setup_edge(request):
    global driver
    driver = webdriver.Edge(executable_path=r'C:\Users\112285\msedgedriver.exe')
    driver.maximize_window()
    driver.get('https://www.91mobiles.com/')
    request.cls.driver = driver
    yield
    driver.close()


# this function is copy paste to take scrrenshot of failure so no need to look into it
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

