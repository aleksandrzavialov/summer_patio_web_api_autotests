import time
import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity

from summerpatio_web_api_autotests.data.devices import Device


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Home Page')
class TestsHomeScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Simple open Home Page')
    @pytest.mark.skip
    def test_add_todos_and_complete_one(self, browser_management, all_devices, both_orientation):
        with allure.step('Open main page and check the title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
            time.sleep(3)

    @pytest.mark.parametrize('all_devices', [Device.Galaxy_A13, Device.IPhone_13Pro], indirect=True)
    @pytest.mark.skip
    def test_add_todos_and_complete_two(self, browser_management, all_devices):
        with allure.step('Open main page and check the title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
            time.sleep(3)

    def test_add_todos_and_complete_three(self, browser_management):
        with allure.step('Open main page and check the title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
            time.sleep(20)
