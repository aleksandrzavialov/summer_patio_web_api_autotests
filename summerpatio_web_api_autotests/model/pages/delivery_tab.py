from selene.support.shared import browser
from selene import have


class DeliveryTab:
    def check_if_tab_active(self):
        num_of_elements = len(browser.all('.menu-list'))
        assert num_of_elements >= 1
        return self

    def open_menu(self, menu_name: str = 'Меню доставка'):
        browser.all('.menu-name_mobile').element_by(have.exact_text(menu_name)).click()

    def open_alcohol_menu(self, menu_name: str = 'Карта бара'):
        browser.all('.menu-name_mobile').element_by(have.exact_text(menu_name)).click()
        browser.all('.v-btn__content span').element_by(have.exact_text('Да, исполнилось')).click()


