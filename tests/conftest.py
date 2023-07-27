import os
import pytest
from dotenv import load_dotenv
from summerpatio_web_autotests.data.devices import DeviceInfo
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selene.support.shared import browser
from utils.allure import attach
from selenium import webdriver
import project

DEFAULT_BROWSER_VERSION = '100.0'
DEFAULT_BROWSER = 'chrome'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def return_device_list():
    return DeviceInfo.devices_resolution.keys()


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
        case 'firefox':
            browser.config.window_width = DeviceInfo.devices_resolution.get(request.param)[0]
            browser.config.window_height = DeviceInfo.devices_resolution.get(request.param)[1]

    options = ChromeOptions() if browser.config.driver_name == 'chrome' else FFOptions()
    options.add_experimental_option("mobileEmulation", {"deviceName": request.param}) \
        if browser.config.driver_name == 'chrome' else \
        options.set_preference("general.useragent.override", project.config.safari_user_agent)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    selenoid_capabilities = {
        "browserName": browser.config.driver_name,
        "browserVersion": browser.config.version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()
