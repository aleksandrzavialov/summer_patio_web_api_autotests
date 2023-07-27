import enum


class Texting(enum.Enum):
    authorize = 'Авторизоваться',
    question = 'Есть вопрос по поводу вашего заказа? Звоните:',
    support_invite = 'По вопросам о работе сайта напишите в поддержку:',
    offer = 'Оферта и политика безопасности платежей',
    developed = '© Сайт разработан',
    company = 'GisMenu',
    payment_methods = ['Наличные', 'Безналичные'],

