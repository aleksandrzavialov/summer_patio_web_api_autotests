from selene.support.shared import browser
from selene import be, have, query


class InfoTab:
    def open_tab(self):
        browser.element("a[href='/info']").click()
        return self

    def check_if_tab_active(self):
        browser.all('.devider-list').should(have.size_greater_than(1))
        return self
