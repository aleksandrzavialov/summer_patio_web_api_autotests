import time
import allure
import pytest
from selene import browser, have, be
from allure_commons.types import Severity
from summerpatio_web_api_autotests.model import application
from summerpatio_web_api_autotests.model.components.burger import Burger
from selenium import webdriver


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Home Page')
class TestsMainScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate main page')
    @pytest.mark.parametrize('browser_management', ["iPad Mini"], indirect=True)
    def test_check_main_page_gm_1162(self, browser_management):
        with allure.step('Open main page, check title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
        # with allure.step('Check link to the agreement and agree with cookies'):
        #     application.main_page.check_agreement()
        #     application.main_page.agree_with_cookies()
        # with allure.step('Check burger menu'):
        #     application.main_page.check_burger_menu()
        # with allure.step('Check logo'):
        #     application.main_page.check_logo()
        # with allure.step('Check that menu items appear by default'):
        #     application.delivery_tab.check_if_tab_active()
        # with allure.step('Click on Info tab'):
        #     application.info_tab.open_tab().check_if_tab_active()

    # @allure.severity(Severity.BLOCKER)
    # @allure.title('Validate side menu')
    # @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    # def test_check_side_menu_gm_1166(self, browser_management):
    #     with allure.step('Open main page, check title'):
    #         browser.open('/')
    #         browser.should(have.title_containing('Летний дворик'))
    #     with allure.step('Check link to the agreement and agree with cookies'):
    #         application.main_page.check_agreement()
    #         application.main_page.agree_with_cookies()
    #     with allure.step('Check burger menu'):
    #         application.main_page.check_burger_menu()
    #
    # @allure.severity(Severity.BLOCKER)
    # @allure.title('Validate Info tab')
    # @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    # def test_check_info_tab_gm_1165(self, browser_management):
    #     with allure.step('Open main page, check title'):
    #         browser.open('/')
    #     with allure.step('Check link to the agreement and agree with cookies'):
    #         application.main_page.check_agreement()
    #         application.main_page.agree_with_cookies()
    #     with allure.step('Click on Info tab'):
    #         application.info_tab.open_tab().check_if_tab_active()
    #     with allure.step('Check address'):
    #         application.info_tab.check_address()
    #     with allure.step('Check working hours'):
    #         application.info_tab.check_working_hours()
    #     with allure.step('Check payment methods'):
    #         application.info_tab.check_payment_methods()
    #     with allure.step('Check phone numbers'):
    #         application.info_tab.check_contacts()
    #
    # @allure.severity(Severity.BLOCKER)
    # @allure.title('Open Delivery Menu')
    # @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    # def test_check_opening_menu_gm_1163(self, browser_management):
    #     with allure.step('Open main page, check title'):
    #         browser.open('/')
    #     with allure.step('Check link to the agreement and agree with cookies'):
    #         application.main_page.check_agreement()
    #         application.main_page.agree_with_cookies()
    #     with allure.step('Check that menu appears'):
    #         application.delivery_tab.open_menu()
    #         application.menu_page.check_menu_page()
    #
    # @pytest.mark.parametrize('browser_management', ["iPad Mini"], indirect=True)
    # def test_authorize(self, browser_management):
    #     with allure.step('Open main page, check title'):
    #         browser.open('/')
    #     with allure.step('Check link to the agreement and agree with cookies'):
    #         application.main_page.check_agreement()
    #         application.main_page.agree_with_cookies()
    #     with allure.step('Check that menu appears'):
    #         time.sleep(1)
    #         browser.element(Burger.burger).should(be.visible).click()
    #         browser.element('.icon_auth').hover().click()
    #         time.sleep(5)
    #         browser.element('.auth-btn__apple').hover()
    #         browser.element('.btn-lable__phone').hover()
    #         browser.element('.google-btn').hover().click()
    #         #browser.element('.google-btn').hover().click()
    #         browser.switch_to_next_tab()
    #         browser.element('#identifierId').type('gis.menu.testing@gmail.com')
    #         time.sleep(3)
    #         browser.element('#identifierNext').click()
    #         browser.element('#password input').type('J[etyysqGfhjkm123')
    #         browser.element('#passwordNext').click()
    #         # browser.
    #         # headers = webdriver.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
    #         # time.sleep(15)
    #         print('1')


