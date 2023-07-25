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
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
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
            browser.open('/')
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
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
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
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_check_search_in_menu_gm_1183(self, browser_management):
        meat_dish = application.meat_dish_1
        soup_dish = application.soup_dish_2
        fish_dish = application.fish_dish_3
        new_order = application.new_order
        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Find dish 1 attributes'):
            application.menu_page.check_dish(meat_dish)
        with allure.step('Add 1 dish to the cart'):
            application.menu_page.add_to_cart(meat_dish)
        with allure.step('Check order amount'):
            new_order.check_amount(new_order.calculate_amount(meat_dish))
        with allure.step('Find dish 2'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(soup_dish.name)
        with allure.step('Add 2 dish to the cart'):
            application.menu_page.add_to_cart(soup_dish)
        with allure.step('Check order amount'):
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish))
        with allure.step('Find dish 3'):
            application.menu_page.clear_search(soup_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
        with allure.step('Add 3rd dish to the cart'):
            application.menu_page.add_to_cart(fish_dish, 3)
        with allure.step('Check order amount'):
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish, fish_dish))
        with allure.step('Delete 1 piece of 3rd dish from the cart'):
            application.menu_page.delete_from_cart(fish_dish)
        with allure.step('Check order amount'):
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish, fish_dish))
        with allure.step('Place an order'):
            application.menu_page.place_order()
        with allure.step('Check cart content'):
            application.cart.check_cart_dish_amount(meat_dish, soup_dish, fish_dish)
        with allure.step('Clear cart'):
            application.cart.clear_cart()

    @allure.severity(Severity.CRITICAL)
    @allure.title('Add a dish from card part 1')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1194_gr_1_2(self, browser_management):
        meat_dish = application.meat_dish_1
        # soup_dish = application.soup_dish_2
        fish_dish = application.fish_dish_3
        new_order = application.new_order
        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add 1 piece of dish 1 '):
            application.menu_page.check_dish(meat_dish)
            application.menu_page.open_dish_card(meat_dish)
            application.menu_page.add_in_card(meat_dish)
        with allure.step('Check order amount'):
            new_order.check_amount(new_order.calculate_amount(meat_dish))
        with allure.step('Add 3 pieces of dish 2'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
            application.menu_page.open_dish_card(fish_dish)
            application.menu_page.add_in_card(fish_dish, 4)
            application.menu_page.delete_from_card(fish_dish)
            application.menu_page.add_to_cart_from_card()
            new_order.check_amount(new_order.calculate_amount(meat_dish, fish_dish))
        with allure.step('Place an order'):
            application.menu_page.place_order()
        with allure.step('Check cart content'):
            application.cart.check_cart_dish_amount(meat_dish, fish_dish)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Add a dish from card part 2')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1194_gr_3_4(self, browser_management):
        soup_dish = application.soup_dish_2
        fish_dish = application.fish_dish_3
        new_order = application.new_order
        with allure.step('Open main page, check title'):
            browser.open('/')
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add 2 pieces of dish 1 '):
            application.menu_page.check_dish(soup_dish)
            application.menu_page.open_dish_card(soup_dish)
            application.menu_page.add_in_card(soup_dish, 2)
            application.menu_page.add_to_cart_from_card()
            new_order.check_amount(new_order.calculate_amount(soup_dish))
        with allure.step('Reopen menu of dish 1 and add 2 pieces'):
            application.menu_page.open_dish_card(soup_dish)
            application.menu_page.add_in_card(soup_dish, 2)
            application.menu_page.add_to_cart_from_card()
        with allure.step('Place an order'):
            application.menu_page.place_order()
        with allure.step('Check cart content'):
            application.cart.check_cart_dish_amount(soup_dish)
