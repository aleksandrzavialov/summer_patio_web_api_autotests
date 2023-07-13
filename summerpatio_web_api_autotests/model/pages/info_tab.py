from selene.support.shared import browser


class InfoTab:
    def open_tab(self):
        browser.element("a[href='/info']").click()
        return self

    def check_if_tab_active(self):
        num_of_elements = len(browser.all('.devider-list'))
        #num_of_elements = len(browser.all('.work'))
        assert num_of_elements >= 1
        return self
