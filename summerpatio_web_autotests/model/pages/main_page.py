from selene import be, have
from selene.support.shared import browser
from summerpatio_web_autotests.data.contacts import Contact
from summerpatio_web_autotests.data.links import Link
from summerpatio_web_autotests.data.textings import Texting
from summerpatio_web_autotests.model.components.burger import Burger
from summerpatio_web_autotests.model.components.header import Header
from datetime import date


class MainPage:

    def agree_with_cookies(self):
        browser.element('.btn-cookie').click()
        return self

    def check_agreement(self):
        browser.element('.rules').should(have.attribute('href').value(f'{Link.agreement_link.value[0]}'))
        return self

    def open_main_page_and_agree_with_cookies(self):
        browser.open('/')
        browser.should(have.title_containing('Летний дворик'))
        if browser.element('.btn-cookie').matching(be.visible):
            self.check_agreement()
            self.agree_with_cookies()


    def check_burger_menu(self):
        date_today = date.today()
        browser.element(Burger.burger).should(be.visible).click()
        browser.element(Burger.authorize).should(have.text(f'{Texting.authorize.value[0]}'))
        browser.all(Burger.footer_texts).should(have.exact_texts(
            f'{Texting.question.value[0]} {Contact.support.value[0]}', f'{Texting.support_invite.value[0]}'))
        browser.element(Burger.phone_link).should(have.attribute('href').value(Contact.support_link_for_phone.value[0]))
        browser.element(Burger.mail_button).should(have.attribute('href').value(Contact.support_link_for_mail.value[0]))
        browser.element(Burger.telegram_button).should(have.attribute('href').value(Contact.support_link_for_telegram.value[0]))
        browser.element(Burger.offer_link).should(have.attribute('href').value(Link.offer_link.value[0])).\
            should(have.text(f'{Texting.offer.value[0]}'))
        browser.element(Burger.burger_footer).should(have.text(f'{Texting.developed.value[0]} {Texting.company.value[0]} '
                                                               f'{date.strftime(date_today,"%Y")}'))
        browser.element(Burger.return_button).click()

        return self

    def check_logo(self):
        browser.element('.logo').should(be.visible).should(have.attribute('width').value(Header.logo['width'])).\
            should(have.attribute('height').value(Header.logo['height']))
        return self


