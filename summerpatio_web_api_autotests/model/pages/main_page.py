from selene import be, have
from selene.support.shared import browser
from summerpatio_web_api_autotests.data.contacts import Contact
from summerpatio_web_api_autotests.data.links import Link
from summerpatio_web_api_autotests.data.textings import Texting
from summerpatio_web_api_autotests.model.components.burger_menu import Burger
from summerpatio_web_api_autotests.model.components.header_menu import Header
from datetime import date


class MainPage:

    def agree_with_cookies(self):
        browser.element('.btn-cookie').click()
        return self

    def check_agreement(self):
        browser.element('.rules').should(have.attribute('href').value(f'{Link.agreement_link.value[0]}'))
        return self

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

    # def authorize_in_ui(self):
    #     browser.element('.burger').should(be.visible).click()
    #     browser.element('.modal-link').click()
    #     browser.element('[class=google]').click()
    #     browser.switch_to_next_tab()
    #     browser.element('#identifierId').type(Contact.google_account.value[0])
    #     browser.element('#identifierNext').click()
    #     return self



