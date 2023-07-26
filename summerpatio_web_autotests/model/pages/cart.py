import time
from selene.support.shared import browser
from selene import be, have
from summerpatio_web_autotests.model.components.dish import Dish


class Cart:
    def check_cart_dish_amount(self, args):
        browser.all('.tale-row').should(have.size(len(args)))
        counts = []
        sum_of = 0
        for dish in args:
            counts.append(str(dish.count))
            sum_of += dish.count
        browser.all('.count').should(have.texts(counts))
        browser.element('.table-title').should(have.text(str(sum_of)))
        return self

    def check_dish_attributes(self, args):
        time.sleep(3) #wait for pictures to load
        browser.all('.position-cover').should(have.size(len(args)))
        browser.all('.remove-item').should(have.size(len(args)))
        browser.all('.cart-table button[type="button"]').should(have.size(len(args) * 2))
        for dish in args:
            total_sum = dish.count * int(dish.price.split(' ')[0])
            browser.all('.name').element_by(have.exact_text(dish.name)).should(be.visible)
            temp_name = str(dish.name).capitalize()
            browser.element(f'//*[text()[contains(.,"{temp_name}")]]/ancestor::div[contains(@class, "tale-row")]//span[contains(@class, "subtitle")]').should(have.text(dish.mass))
            browser.element(f'//*[text()[contains(.,"{temp_name}")]]/ancestor::div[contains(@class, "tale-row")]//span[contains(@class, "cost-dishes")]').should(have.text(f'{total_sum} ₽'))

    def clear_cart(self, cancel: bool = False):
        browser.element('.v-btn__content').click()
        browser.element('.v-card-title .title').should(have.text('Очистить корзину?'))
        if not cancel:
            browser.all('.v-btn__content span').element_by(have.exact_text('Очистить')).click()
            browser.element('.empty-cart').should(be.visible)
            browser.all('.v-btn__content span').element_by(have.exact_text('Вернуться в меню')).should(be.clickable)
        else:
            browser.all('.v-btn__content span').element_by(have.exact_text('Отмена')).click()

    def check_decrease_possibility(self, dish: Dish):
        if dish.count == 1:
            temp_name = str(dish.name).capitalize()
            browser.element(
                f'//*[text()[contains(.,"{temp_name}")]]/ancestor::div[contains(@class, "tale-row")]//button[1]').should(have.css_class('btn-counter_dishes__disabled'))

    def add_dish_to_order(self, dish: Dish, count: int = 1):
        for _ in range(count):
            temp_name = str(dish.name).capitalize()
            browser.element(
                f'//*[text()[contains(.,"{temp_name}")]]/ancestor::div[contains(@class, "tale-row")]//button[2]').click()
            dish.count += 1

    def delete_dish_from_order(self, dish: Dish, count: int = 1):
        for _ in range(count):
            temp_name = str(dish.name).capitalize()
            browser.element(
                f'//*[text()[contains(.,"{temp_name}")]]/ancestor::div[contains(@class, "tale-row")]//button[1]').click()
            dish.count -=1

    def full_delete_of_dish(self, dish):
        temp_name = str(dish.name).capitalize()
        browser.element(f'//*[text()[contains(.,"{temp_name}")]]/parent::div/following-sibling::div').click()

    def check_sum(self, args):
        total_sum = 0
        total_count = 0
        for dish in args:
            total_sum += dish.count * int(dish.price.split(' ')[0])
            total_count += dish.count
        return f'{str(total_sum)} ₽'

    def check_non_empty_cart_appearance(self, *args):
        browser.element('.section-row .title').should(have.text('Корзина'))
        self.check_cart_dish_amount(args)
        self.check_dish_attributes(args)
        cart_sum = self.check_sum(args)
        browser.element('.btn-cart .title').should(have.text('Оформить заказ'))
        browser.element('.amount-cost').should(have.text(cart_sum))
        return cart_sum

    def return_from_card(self):
        browser.element('a svg').click()
        browser.all('.tab-link').should(have.size_greater_than(0))
        browser.all('.row-list').should(have.size_greater_than(0))

    def start_process_order(self):
        browser.element('.btn-cart').click()
        browser.element('.title').should(have.text('Авторизация'))

    def return_to_cart(self):
        browser.element('a[href="/auth"] svg').click()
        browser.element('.section-row .title').should(have.text('Корзина'))

    def return_to_menu_from_empty_cart(self):
        browser.element('.btn-back').click()
        browser.all('.tab-link').should(have.size_greater_than(0))
        browser.all('.row-list').should(have.size_greater_than(0))






