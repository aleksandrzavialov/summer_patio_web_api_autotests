import logging
from summerpatio_web_api_autotests.utils.api_helper import load_json_schema, api_session
from summerpatio_web_api_autotests.data.api_data import ApiCredentials


class ApiHelper:
    def __init__(self):
        self.api_session = api_session

    @staticmethod
    def get_menus():
        response = api_session.get('/api/v1/menu', params={'Content-Type': ApiCredentials.content_type.value,
                                                           'Authorization': ApiCredentials.external_token_menu})
        logging.info(response.json())
