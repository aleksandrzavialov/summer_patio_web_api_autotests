import time

import allure
import pytest
from selene import browser, have
from allure_commons.types import Severity
from summerpatio_web_api_autotests.model import application


@allure.tag("ui", "web")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Authorization')
class TestsMainScreen:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Validate main page')
    @pytest.mark.parametrize('browser_management', ["IPhone_14ProMax"], indirect=True)
    def test_check_google_authorization_gm_1041(self, browser_management):
        with allure.step('Open main page, check title'):
            browser.open('/')
            browser.should(have.title_containing('Летний дворик'))
        with allure.step('Authorize via Google'):
            application.main_page.authorize_in_ui()
            time.sleep(10)