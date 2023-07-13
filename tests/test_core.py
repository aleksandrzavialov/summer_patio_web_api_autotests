import time
import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity

from summerpatio_web_api_autotests.model.pages.delivery_tab import DeliveryTab
from summerpatio_web_api_autotests.model.pages.info_tab import InfoTab
from summerpatio_web_api_autotests.model.pages.main_page import MainPage


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Home Page')
class TestsMainScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate main page')
    def test_check_main_page(self, browser_management):
        main_page = MainPage()
        delivery_tab = DeliveryTab()
        info_tab = InfoTab()
        with allure.step('Open main page, check title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
        with allure.step('Check link to the agreement and agree with cookies'):
            main_page.check_agreement()
            main_page.agree_with_cookies()
        with allure.step('Check burger menu'):
            main_page.check_burger_menu()
        with allure.step('Check logo'):
            main_page.check_logo()
        with allure.step('Check that menu items appear by default'):
            delivery_tab.check_if_tab_active()
        with allure.step('Click on Info tab'):
            info_tab.open_tab().check_if_tab_active()

