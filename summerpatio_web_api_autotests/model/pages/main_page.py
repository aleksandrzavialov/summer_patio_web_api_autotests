from selene import be, have
from selene.support.shared import browser


class MainPage:
    def agree_with_cookies(self):
        browser.element('.btn-cookie').click()
        return self

    def check_agreement(self):
        browser.element('.rules').should(have.attribute('href').value('https://drive.google.com/open?id=1LheLyyj1d7HdbJGm3CawY6hqk5hooGWZUDEXaY60V3w'))
        return self
