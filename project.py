from typing import Literal
import pydantic
from summerpatio_web_autotests.utils import path

BrowserType = Literal['chrome', 'firefox']


class Config(pydantic.BaseSettings):
    base_url: str = 'https://summer-patio-stage.gismenu.ru/'
    driver_name: BrowserType = 'chrome'
    version = '100.0'
    hold_driver_at_exit: bool = False
    window_width: int = 1080
    window_height: int = 1920
    timeout: float = 5.0
    headless: bool = False
    safari_user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
    chrome_device = 'Nexus 5'


config = Config(_env_file=path.relative_from_root('.env'))
