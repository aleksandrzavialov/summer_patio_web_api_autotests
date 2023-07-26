import allure
import pytest
from selene import browser
from allure_commons.types import Severity
from summerpatio_web_autotests.model import application


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Menu')
class TestsMenuScreen:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Validate filtering of dishes')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_check_search_in_menu_gm_1170(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Search for a dish in delivery menu'):
            application.menu_page.check_filtering('салат')
        with allure.step('Return to main menu'):
            browser.open('/')
        with allure.step('Open alcohol menu and check that search is switched off'):
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
            application.main_page.open_main_page_and_agree_with_cookies()
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
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add dish 1 to cart and check amount'):
            application.menu_page.check_dish(meat_dish)
            application.menu_page.add_to_cart(meat_dish)
            new_order.check_amount(new_order.calculate_amount(meat_dish))
        with allure.step('Add dish 2 to cart and check total amount of 2'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(soup_dish.name)
            application.menu_page.add_to_cart(soup_dish)
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish))
        with allure.step('Add dish 3 to cart and check total amount of 2'):
            application.menu_page.clear_search(soup_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
            application.menu_page.add_to_cart(fish_dish, 3)
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish, fish_dish))
        with allure.step('Delete 1 piece of 3rd dish from the cart and check total amount'):
            application.menu_page.delete_from_cart(fish_dish)
            new_order.check_amount(new_order.calculate_amount(meat_dish, soup_dish, fish_dish))
        with allure.step('Place an order and check cart content'):
            application.menu_page.place_order()
            application.cart.check_cart_dish_amount(meat_dish, soup_dish, fish_dish)
        with allure.step('Clear cart'):
            application.cart.clear_cart()

    @allure.severity(Severity.NORMAL)
    @allure.title('Add a dish from card part 1')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1194_gr_1_2(self, browser_management):
        meat_dish = application.meat_dish_1
        fish_dish = application.fish_dish_3
        new_order = application.new_order
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add 1 piece of dish 1 from card and check amount'):
            application.menu_page.check_dish(meat_dish)
            application.menu_page.open_dish_card(meat_dish)
            application.menu_page.add_in_card(meat_dish)
            new_order.check_amount(new_order.calculate_amount(meat_dish))
        with allure.step('Add 3 pieces of dish 2 from card and check total amount'):
            application.menu_page.clear_search(meat_dish.name)
            application.menu_page.search_for_a_dish(fish_dish.name)
            application.menu_page.open_dish_card(fish_dish)
            application.menu_page.add_in_card(fish_dish, 4)
            application.menu_page.delete_from_card(fish_dish)
            application.menu_page.add_to_cart_from_card()
            new_order.check_amount(new_order.calculate_amount(meat_dish, fish_dish))
        with allure.step('Place an order and check cart content'):
            application.menu_page.place_order()
            application.cart.check_cart_dish_amount(meat_dish, fish_dish)


    @allure.severity(Severity.NORMAL)
    @allure.title('Add a dish from card part 2')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1194_gr_3_4(self, browser_management):
        soup_dish = application.soup_dish_2
        new_order = application.new_order
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Open delivery menu'):
            application.delivery_tab.open_menu()
        with allure.step('Add 2 pieces of dish 1 and check amount'):
            application.menu_page.check_dish(soup_dish)
            application.menu_page.open_dish_card(soup_dish)
            application.menu_page.add_in_card(soup_dish, 2)
            application.menu_page.add_to_cart_from_card()
            new_order.check_amount(new_order.calculate_amount(soup_dish))
        with allure.step('Reopen menu of dish 1 and add 2 pieces'):
            application.menu_page.open_dish_card(soup_dish)
            application.menu_page.add_in_card(soup_dish, 2)
            application.menu_page.add_to_cart_from_card()
        with allure.step('Place an order and check cart content'):
            application.menu_page.place_order()
            application.cart.check_cart_dish_amount(soup_dish)

    @allure.severity(Severity.NORMAL)
    @allure.title('Check alcohol menu if agree to proceed')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1025_accept(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Open alcohol menu'):
            application.delivery_tab.open_menu('Карта бара')
            application.menu_page.confirm_age()

    @allure.severity(Severity.NORMAL)
    @allure.title('Refuse to open alcohol menu')
    @pytest.mark.parametrize('browser_management', ["IPhone_8"], indirect=True)
    def test_add_dish_from_cards_gm_1025_decline(self, browser_management):
        with allure.step('Open main page, check title'):
            application.main_page.open_main_page_and_agree_with_cookies()
        with allure.step('Refuse to open alcohol menu'):
            application.delivery_tab.open_menu('Карта бара')
            application.menu_page.decline_age()
        with allure.step('Check that unable to open until reload'):
            application.menu_page.check_unable_until_reload()
            application.delivery_tab.open_menu('Карта бара')
            application.menu_page.confirm_age()

