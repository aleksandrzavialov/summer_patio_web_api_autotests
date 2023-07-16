from summerpatio_web_api_autotests.model.components.dish import Dish
from summerpatio_web_api_autotests.model.pages.main_page import MainPage
from summerpatio_web_api_autotests.model.pages.delivery_tab import DeliveryTab
from summerpatio_web_api_autotests.model.pages.info_tab import InfoTab
from summerpatio_web_api_autotests.model.pages.menu_page import MenuPage

main_page = MainPage()
delivery_tab = DeliveryTab()
info_tab = InfoTab()
menu_page = MenuPage()

meat_dish_1 = Dish('мясо #1', 'Мясо', '250 г', '340 ₽')

