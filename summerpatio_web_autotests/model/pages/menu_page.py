import time
from selene.support.shared import browser
from selene import be, have, command
from selenium.webdriver import Keys
from summerpatio_web_autotests.model.components.dish import Dish


class MenuPage:
    def check_menu_page(self, menu_name: str = 'Меню доставка', last_menu_group: str = 'Прочее'):
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
        time.sleep(3)
        self.check_result(dish)
        return self

    def check_result(self, dish):
        time.sleep(3)  # wait for filtering end. unfortunately, no signs of finished loading on UI, so used hardcoded value
        filtered_collection = browser.all('.v-list-item .name')
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

    def add_to_cart(self, dish: Dish, count: int = 1):
        if dish.count == 0:
            for _ in range(count):
                if _ == 0:
                    browser.element('.btn-counter').click()
                else:
                    browser.element('.btn-counter:nth-of-type(2)').click()
                dish.count += 1
        else:
            for _ in range(count):
                browser.element('.btn-counter:nth-of-type(2)').click()
            dish.count += 1
        return dish.count

    def delete_from_cart(self, dish: Dish, count: int = 1):
        for _ in range(count):
            browser.element('.btn-counter:nth-of-type(1)').click()
            dish.count -= 1

    @staticmethod
    def check_amount(dish: Dish):
        total_price_of_dish = 0.0
        for count in range(dish.count):
            total_price_of_dish += float(dish.price.split(' ')[0])
            dish.total_amount = total_price_of_dish

    def place_order(self):
        browser.element('.order').click()
        return self

    def open_dish_card(self, dish: Dish):
        browser.element('.image').click()
        browser.element('.title_link').should(have.text(dish.group))
        browser.element('.image').should(be.visible)
        browser.element('.title_link').should(have.text(dish.group))
        browser.element('.measure_subtitle').should(have.text(dish.mass))
        browser.element('.router-link-active span').should(have.text('К меню'))
        browser.element('a[href="/menu"] span').should(have.text('К заведению'))
        browser.element('.count').should(have.text('1'))
        browser.element('.add-action button').should(be.visible)
        browser.all('button svg').should(have.size(2))
        browser.element('.add-action span:nth-of-type(1)').should(have.text('Добавить'))
        browser.element('.add-action span:nth-of-type(2)').should(have.text(dish.price))

    def add_in_card(self, dish: Dish, count: int = 1):
        for _ in range(count):
            if count == 1:
                browser.element('.add-action').click()
            else:
                if _ < count - 1:
                    browser.element('.btn-counter:nth-of-type(2)').click()
            dish.count += 1
        if count > 1:
            self.check_total_price_in_card(dish, count)
        return dish.count

    def delete_from_card(self, dish: Dish, count: int = 1):
        for _ in range(count):
            browser.element('.btn-counter:nth-of-type(1)').click()
            dish.count -= 1
        self.check_total_price_in_card(dish, count)
        return dish.count

    def check_total_price_in_card(self, dish, count):
        dish_amount = count * int(dish.price.split(' ')[0])
        text_amount = f'{dish_amount} ₽'
        browser.element('.count').should(have.text(str(count)))
        browser.element('.add-action span:nth-of-type(2)').should(have.text(text_amount))

    def add_to_cart_from_card(self):
        browser.element('.add-action button').click()

    def confirm_age(self, menu_name: str = 'Карта бара'):
        browser.element('.title').should(have.text('Вам исполнилось 18 лет?'))
        browser.element('#agree').click()
        browser.all('.tab-link').should(have.size_greater_than(0))
        browser.element('.items-title').should(have.text(menu_name))

    def decline_age(self, menu_name: str = 'Карта бара'):
        browser.element('.title').should(have.text('Вам исполнилось 18 лет?'))
        browser.element('#none').click()

    def check_unable_until_reload(self, menu_name: str = 'Карта бара'):
        browser.all('.tab-link').should(have.size(0))
        browser.all('.row-list').should(have.size(0))
        browser.all('.menu-name_mobile').element_by(have.exact_text(menu_name)).click()
        browser.all('.tab-link').should(have.size(0))
        browser.all('.row-list').should(have.size(0))
        browser.driver.refresh()






