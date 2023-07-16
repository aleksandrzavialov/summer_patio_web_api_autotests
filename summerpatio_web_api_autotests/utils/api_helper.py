import json
import logging
import os.path

import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response
import curlify

import project


def load_json_schema(name: str):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../schemas', name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(
        self,
        method: str | bytes,
        url: str | bytes,
        *args,
        **kwargs
    ) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)
        curl_message = curlify.to_curl(response.request)
        status_code = response.status_code
        logging.info(f'Response Code: {status_code} for \n{curl_message}')
        if 'application/json' in response.headers.get('Content-Type', ''):
            response_attached = json.dumps(response.json(), indent=4)
        else:
            response_attached = response.text

        with step(f'{method} {url}'):
            allure.attach(body=f'Response code: {status_code} for CURL message: {curl_message}', name='Request curl', attachment_type=AttachmentType.TEXT, extension='txt')

        with step('Response'):
            allure.attach(body=response_attached, name='Response', attachment_type=AttachmentType.TEXT, extension='txt')
            return response


api_session = CustomSession(project.config.base_url)