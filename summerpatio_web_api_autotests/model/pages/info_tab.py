from datetime import date

from selene.support.shared import browser
from selene import be, have
from summerpatio_web_api_autotests.data.contacts import Contact
from summerpatio_web_api_autotests.data.textings import Texting


class InfoTab:
    working_schedule = {
        'Пон.': '06:00 – 01:00',
        'Втр.': '09:00 – 04:00',
        'Ср.': '10:00 – 24:00',
        'Чтв.': '00:20 – 23:55',
        'Пт.': '06:00 – 24:00',
        'Сбт.': '00:00 – 23:00',
        'Вскр.': 'Выходной'
    }

    def open_tab(self):
        browser.element("a[href='/info']").click()
        return self

    def check_if_tab_active(self):
        browser.all('.devider-list').should(have.size_greater_than(1))
        return self

    def check_address(self):
        browser.element('.title_top').should(have.text('Адреса самовывоза'))
        browser.element('.address svg').should(be.visible)
        browser.element('.text_address').should(have.text(f'{Contact.delivery_address.value}'))
        return self

    def check_working_hours(self):
        current_day = date.strftime(date.today(), "%a")
        print('CURRENT DAY: '+current_day)
        actual_schedule = ''
        browser.element('.work svg:nth-child(1)').should(be.visible)
        match current_day:
            case 'Mon':
                actual_schedule = 'Пон.'
            case 'Tue':
                actual_schedule = 'Втр.'
            case 'Wed':
                actual_schedule = 'Ср.'
            case 'Thu':
                actual_schedule = 'Чтв.'
            case 'Fri':
                actual_schedule = 'Пт.'
            case 'Sat':
                actual_schedule = 'Сбт.'
            case 'Sun':
                actual_schedule = 'Вскр.'
        browser.element('.work-label').should(have.text(self.working_schedule[actual_schedule]))
        browser.element('.work svg:nth-child(2)').click()
        browser.all('.option-item .v-col-1').should(have.texts(self.working_schedule.keys()))
        browser.all('.option-item .v-col-auto').should(have.texts(self.working_schedule.values()))
        browser.element('.drop_open').click()
        return self

    def check_payment_methods(self):
        browser.element('.pay .title').should(have.text('Способы оплаты'))
        browser.all('.pay_name').should(have.texts(Texting.payment_methods.value[0]))
        browser.all('.pay_list circle').should(have.size(len(Texting.payment_methods.value[0])))
        return self

    def check_contacts(self):
        browser.element('.links .pb-6').should(have.text('Контакты'))
        browser.all('a.link_contact').should(have.size_greater_than(0))
        browser.element('.contacts-list li:nth-child(1) .link_contact').should(have.attribute('href').value(Contact.support_link_for_phone.value[0]))
        return self

