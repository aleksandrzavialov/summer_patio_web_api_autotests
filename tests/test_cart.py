import allure
import pytest
from selene import browser
from allure_commons.types import Severity
from summerpatio_web_api_autotests.model import application


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Cart')
class TestsCart:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Check working with whole cart')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_check_cart_content_and_clearing_gm_1196(self, browser_management):
        meat_dish = application.meat_dish_1
        soup_dish = application.soup_dish_2
        fish_dish = application.fish_dish_3
        new_cart = application.cart

        with allure.step('Open main page'):
            browser.open('/')
        with allure.step('Check link to the agreement and agree with cookies'):
            application.main_page.check_agreement()
            application.main_page.agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add dish 1 to the cart'):
            application.menu_page.search_for_a_dish(meat_dish.name)
            application.menu_page.add_to_cart(meat_dish, 2)
        with allure.step('Add dish 2 to the cart from menu'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(soup_dish.name)
            application.menu_page.add_to_cart(soup_dish, 3)
        with allure.step('Add dish 3 from card'):
            application.menu_page.clear_search(soup_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
            application.menu_page.open_dish_card(fish_dish)
            application.menu_page.add_in_card(fish_dish, 4)
            application.menu_page.add_to_cart_from_card()
        with allure.step('Check cart content'):
            application.menu_page.place_order()
            new_cart.return_from_card()
            application.menu_page.place_order()
            new_cart.check_non_empty_cart_appearance(meat_dish, soup_dish, fish_dish)
        with allure.step('Clear cart after 2nd attempt'):
            new_cart.clear_cart(True)
            new_cart.check_non_empty_cart_appearance(meat_dish, soup_dish, fish_dish)
            new_cart.start_process_order()
            new_cart.return_to_cart()
            new_cart.clear_cart()
            new_cart.return_to_menu_from_empty_cart()

    @allure.severity(Severity.CRITICAL)
    @allure.title('Check working with separate positions in cart')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_check_cart_content_and_clearing_gm_1197(self, browser_management):
        meat_dish = application.meat_dish_1
        fish_dish = application.fish_dish_3
        new_cart = application.cart

        with allure.step('Open main page'):
            browser.open('/')
        with allure.step('Check link to the agreement and agree with cookies'):
            application.main_page.check_agreement()
            application.main_page.agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add dish 1 to the cart from menu'):
            application.menu_page.search_for_a_dish(meat_dish.name)
            application.menu_page.add_to_cart(meat_dish, 3)
        with allure.step('Add dish 2 from card'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
            application.menu_page.open_dish_card(fish_dish)
            application.menu_page.add_in_card(fish_dish, 2)
            application.menu_page.add_to_cart_from_card()
        with allure.step('Check cart content'):
            application.menu_page.place_order()
            new_cart.check_non_empty_cart_appearance(meat_dish, fish_dish)
        with allure.step('Add 1 piece of meat dish'):
            new_cart.add_dish_to_order(meat_dish, 3)
            new_cart.delete_dish_from_order(fish_dish, 1)
            new_cart.check_decrease_possibility(fish_dish)
            new_cart.check_non_empty_cart_appearance(meat_dish, fish_dish)
            new_cart.full_delete_of_dish(fish_dish)
            new_cart.check_non_empty_cart_appearance(meat_dish)