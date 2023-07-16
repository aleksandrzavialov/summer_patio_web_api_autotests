from jsonschema import validate
from summerpatio_web_api_autotests.utils.api_helper import load_json_schema, api_session
from summerpatio_web_api_autotests.api_helpers.api_helpers import ApiHelper


def test_get_menu_list():
    ApiHelper.get_menus()
    # assert response.status_code == 200
    # assert response.json()['page'] == 1
    # assert response.json()['per_page'] == per_page
    # assert response.json()['total_pages'] == 4
    # assert response.json()['total'] == 12