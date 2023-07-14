import os
import time

import pytest
from dotenv import load_dotenv
from summerpatio_web_api_autotests.data.devices import FirefoxList, ChromeList, DeviceInfo
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions

from selene.support.shared import browser
from selenium import webdriver
from utils.allure import attach

from selenium import webdriver

import project

DEFAULT_BROWSER_VERSION = '100.0'
DEFAULT_BROWSER = 'chrome'
DEVICE_LIST = [1, 2]


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def return_device_list():
    if project.config.driver_name == 'chrome':
        return DeviceInfo.chrome_devices
    else:
        return DeviceInfo.firefox_devices

# iphone14ProMaxOnly = pytest.mark.parametrize("all_devices", [devices.Device.IPhone_14ProMax], indirect=True)


# @pytest.fixture(scope='session', params=['horizontal', 'vertical'])
# def both_orientation(request):
#     if request.param == 'vertical':
#         temp_height = browser.config.window_width
#         browser.config.window_width = browser.config.window_height
#         browser.config.window_height = temp_height
#     yield browser
#     browser.quit()


@pytest.fixture(scope='function', params=return_device_list())
def browser_management(request):
    browser.config.base_url = project.config.base_url
    browser.config.driver_name = project.config.driver_name if project.config.driver_name else DEFAULT_BROWSER
    browser.config.version = project.config.version if project.config.version else DEFAULT_BROWSER_VERSION
    browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.timeout = project.config.timeout

    match browser.config.driver_name:
        case 'chrome':
            driver_options = webdriver.ChromeOptions() # comment for selenide
            driver_options.add_experimental_option("mobileEmulation", {"deviceName": request.param}) # comment for selenide
            browser.config.driver_options = driver_options # comment for selenide
        case 'firefox':

            browser.config.window_width = DeviceInfo.firefox_devices_dict.get(request.param)[0]# comment for selenide
            browser.config.window_height = DeviceInfo.firefox_devices_dict.get(request.param)[1]# comment for selenide

            driver_options = webdriver.FirefoxOptions()
            driver_options.set_preference("general.useragent.override", project.config.safari_user_agent)
            browser.config.driver_options = driver_options

    # options = ChromeOptions() if browser.config.driver_name == 'chrome' else FFOptions()
    # options.add_experimental_option("mobileEmulation", {"deviceName": request.param}) \
    #     if browser.config.driver_name == 'chrome' else \
    #     options.set_preference("general.useragent.override", project.config.safari_user_agent)
    #
    # login = os.getenv('SELENOID_LOGIN')
    # password = os.getenv('SELENOID_PASSWORD')
    #
    # selenoid_capabilities = {
    #     "browserName": browser.config.driver_name,
    #     "browserVersion": browser.config.version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    # browser.config.driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()
