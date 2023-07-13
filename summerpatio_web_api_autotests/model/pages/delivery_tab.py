from selene.support.shared import browser


class DeliveryTab:
    def check_if_tab_active(self):
        num_of_elements = len(browser.all('.menu-list'))
        assert num_of_elements >= 1
        return self
