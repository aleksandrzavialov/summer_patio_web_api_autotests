import time
import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity

import project
from summerpatio_web_api_autotests.data.devices import DeviceInfo
from summerpatio_web_api_autotests.model import application


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Home Page')
class TestsMainScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate main page')
    @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    def test_check_main_page_gm_1162(self, browser_management):
        with allure.step('Open main page, check title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
        with allure.step('Check link to the agreement and agree with cookies'):
            application.main_page.check_agreement()
            application.main_page.agree_with_cookies()
        with allure.step('Check burger menu'):
            application.main_page.check_burger_menu()
        with allure.step('Check logo'):
            application.main_page.check_logo()
        with allure.step('Check that menu items appear by default'):
            application.delivery_tab.check_if_tab_active()
        with allure.step('Click on Info tab'):
            application.info_tab.open_tab().check_if_tab_active()

    def test_fixture(self, browser_management):
        print(1)
        # for specs in DeviceInfo.deviceList.values():
        #     print(str(specs[0]))
        #     print('UUU '+project.config.driver_name)
        #     #print('ALL '+str(DeviceInfo.deviceList.values()))
        #     match project.config.driver_name:
        #         case 'chrome':
        #             print('I AM CHROME')
        #             if str(specs[0]) == 'Emulated':
        #                 print('O LA LA: '+str(specs[1]))
        #             # else:
        #             # yield ['Skip on Chrome']
        #         case 'firefox':
        #             print('I AM FF')
        #             if str(specs[0]) == 'NotEmulated':
        #                 print('O LALA: '+str(specs[1]))

