import time
from gettext import gettext

from selene.support.shared import browser
from selene import be, have, command, query
from selenium.webdriver import Keys

from summerpatio_web_api_autotests.model.components.dish import Dish
from selenium import webdriver

class MenuPage:
    def check_menu_page(self,menu_name: str = 'Меню доставка', last_menu_group: str = 'Прочее'):
        browser.element('.items-title').should(have.text(menu_name))
        browser.element('.v-toolbar-items svg').should(be.clickable)
        browser.element('.search').should(be.clickable)
        browser.all('.tab-link').should(have.size_greater_than(0))
        browser.all('.row-list').should(have.size_greater_than(0))
        browser.element('.wrapper-list .list:last-child').perform(command.js.scroll_into_view).should(have.text(last_menu_group))
        return self

    def search_for_a_dish(self, dish):
        browser.all('.name').should(have.size_greater_than(0))
        browser.element('.search').click()
        browser.all('.col-title_hidden').should(have.size(2))
        browser.element('.v-field__input').should(have.attribute('placeholder').value('Поиск'))
        browser.element('.mdi-magnify').should(be.visible)
        browser.element('.v-field__input').type(dish)
        self.check_result(dish)
        return self

    def check_result(self, dish):
        time.sleep(3)  # wait for filtering end. unfortunately, no signs of finished loading on UI, so used hardcoded value
        filtered_collection = browser.all('.v-list-item')
        for element in filtered_collection:
            element.should(have.text(dish))
        return self

    def check_filtering(self, dish: str):
        self.search_for_a_dish(dish).\
            check_result(dish)

    def return_to_main_page(self):
        browser.element('.v-field__input').press_tab()
        browser.element('.py-0 svg').click()
        return self

    def check_search_is_not_used(self):
        browser.element('.v - toolbar__content.closed').should(be.not_.visible)
        return self

    @staticmethod
    def calculate_item_count():
        filtered_collection = browser.all('.v-list-item')
        return len(filtered_collection)

    def clear_search(self, dish):
        for _ in dish:
            browser.element('.v-field__input').send_keys(Keys.BACKSPACE)
        time.sleep(3)
        return self

    def check_dish(self, dish: Dish):
        time.sleep(3)
        browser.all('.name').element_by(have.exact_text(dish.name)).click()
        browser.all('.name').element_by(have.exact_text(dish.name)).perform(command.js.scroll_into_view)
        browser.element('.tab_active').should(have.text(dish.group))
        self.search_for_a_dish(dish.name)

        browser.element('.name').should(have.exact_text(dish.name))
        browser.element('.measure').should(have.exact_text(dish.mass))
        browser.element('.price').should(have.exact_text(dish.price))
        browser.element('.image').should(have.attribute('src'))
        if dish.count == 0:
            browser.element('.btn-counter').should(have.exact_text('Добавить'))
        else:
            browser.element('.btn-counter').should(have.size(2))