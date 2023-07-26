import allure
import pytest
from allure_commons.types import Severity
from summerpatio_web_autotests.model import application


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
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Check burger menu'):
            application.main_page.check_burger_menu()
        with allure.step('Check logo'):
            application.main_page.check_logo()
        with allure.step('Check that menu items appear by default'):
            application.delivery_tab.check_if_tab_active()
        with allure.step('Click on Info tab'):
            application.info_tab.open_tab().check_if_tab_active()

    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate side menu')
    @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    def test_check_side_menu_gm_1166(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Check burger menu'):
            application.main_page.check_burger_menu()

    @allure.severity(Severity.BLOCKER)
    @allure.title('Open Delivery Menu')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_check_opening_menu_gm_1163(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Check that menu appears'):
            application.delivery_tab.open_menu()
            application.menu_page.check_menu_page()

    @allure.severity(Severity.NORMAL)
    @allure.title('Validate Info tab')
    @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    def test_check_info_tab_gm_1165(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Click on Info tab'):
            application.info_tab.open_tab().check_if_tab_active()
        with allure.step('Check content of Info tab'):
            application.info_tab.check_info_tab_content()


