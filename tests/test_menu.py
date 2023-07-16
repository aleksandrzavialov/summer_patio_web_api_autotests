import time

import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity
from summerpatio_web_api_autotests.model import application


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Menu')
class TestsMainScreen:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Validate filtering of dishes')
    @pytest.mark.parametrize('browser_management', ["Nexus 5"], indirect=True)
    def test_check_search_in_menu_gm_1170(self, browser_management):
        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Check link to the agreement and agree with cookies'):
            application.main_page.check_agreement()
            application.main_page.agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Search for a dish in delivery menu'):
            application.menu_page.check_filtering('салат')
        with allure.step('Return to main menu'):
            application.menu_page.return_to_main_page()
        with allure.step('Open alcohol menu'):
            application.delivery_tab.open_alcohol_menu()
            application.menu_page.check_search_is_not_used()
        with allure.step('Search for a dish in alcohol menu'):
            initial_count_of_alcohol_positions = application.menu_page.calculate_item_count()
            application.menu_page.check_filtering('бутылочное')
            application.menu_page.clear_search('бутылочное')
        with allure.step('Check that initial count of dishes is back'):
            count_of_alcohol_positions_after_filter_clear = application.menu_page.calculate_item_count()
            assert initial_count_of_alcohol_positions == count_of_alcohol_positions_after_filter_clear

    @allure.severity(Severity.CRITICAL)
    @allure.title('Validate dish cards')
    @pytest.mark.parametrize('browser_management', ["Nexus 5"], indirect=True)
    def test_check_search_in_menu_gm_1182(self, browser_management):
        meat_dish = application.meat_dish_1

        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Check dish attributes'):
            application.menu_page.check_dish(meat_dish)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Add a dish from menu')
    @pytest.mark.parametrize('browser_management', ["Nexus 5"], indirect=True)
    def test_check_search_in_menu_gm_1185(self, browser_management):
        meat_dish = application.meat_dish_1

        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Find dish attributes'):
            application.menu_page.check_dish(meat_dish)

