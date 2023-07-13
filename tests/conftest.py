import os

import pytest
from dotenv import load_dotenv
from summerpatio_web_api_autotests.data.devices import Device
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions

from selene.support.shared import browser
from selenium import webdriver
from utils.allure import attach

import project

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


#     browser_name = get_option_browser_name
#     browser_name = browser_name if browser_name != '' else DEFAULT_BROWSER
#
#     browser_version = get_option_browser_version
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#
#     selenoid_capabilities = {
#         "browserName": browser_name,
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#
#     login = os.getenv('SELENOID_LOGIN')
#     password = os.getenv('SELENOID_PASSWORD')
#
#     browser.config.driver = webdriver.Remote(
#         command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
#         desired_capabilities=selenoid_capabilities
#     )
#
#     yield browser
#
#


# @pytest.fixture(params=[devices.Device.IPhone_14ProMax, devices.Device.Galaxy_A13,
#                         devices.Device.IPhone_13Pro])

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(params=[device for device in Device])
def all_devices(request):
    browser.config.window_width = request.param.value[0][0]
    browser.config.window_height = request.param.value[0][1]

    yield browser
    browser.quit()


# iphone14ProMaxOnly = pytest.mark.parametrize("all_devices", [devices.Device.IPhone_14ProMax], indirect=True)


@pytest.fixture(scope='function', params=['horizontal', 'vertical'])
def both_orientation(request):
    if request.param == 'vertical':
        temp_height = browser.config.window_width
        browser.config.window_width = browser.config.window_height
        browser.config.window_height = temp_height
    yield browser
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = project.config.base_url
    #browser.config.driver = project.config.driver_name if project.config.driver_name
    browser.config.version = project.config.version if project.config.version else DEFAULT_BROWSER_VERSION
    browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.timeout = project.config.timeout

    if project.config.headless:
        if project.config.driver_name == 'edge':
            raise ValueError('Edge does not support headless mode')
        driver_options = (
            webdriver.ChromeOptions()
            if project.config.driver_name == 'chrome'
            else webdriver.FirefoxOptions()
        )
        driver_options.add_argument('--headless=new')
        browser.config.driver_options = driver_options

    selenoid_capabilities = {
        #"browserName": browser.config.driver_name,
        "browserName": "chrome",
        #"browserVersion": browser.config.version,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options = ChromeOptions()
    # if browser.driver.name == 'chrome' else FFOptions()
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    browser.config.driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)

    yield
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()
