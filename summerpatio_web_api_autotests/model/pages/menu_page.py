from selene.support.shared import browser
from selene import be, have


class MenuPage:
    def check_menu_page(self, menu_name: str = 'Меню доставка'):
        browser.element('.items-title').should(have.text(menu_name))
        browser.element('.v-toolbar-items svg').should(be.clickable)
        browser.element('.search').should(be.clickable)
        browser.all('.tab-link').should(have.size_greater_than(0))
        browser.all('.row-list').should(have.size_greater_than(0))
        return self
