import time
import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity
from summerpatio_web_api_autotests.model.pages.main_page import MainPage


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Home Page')
class TestsMainScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate main page')
    def test_check_main_page(self, browser_management):
        with allure.step('Open main page, check title'):
            main_page = MainPage()
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
        with allure.step('Check link to the aggreement and agree with cookies'):
            main_page.check_agreement()
            main_page.agree_with_cookies()
            time.sleep(3)
