from typing import Literal
import pydantic

from summerpatio_web_autotests.utils import path

BrowserType = Literal['chrome', 'firefox']


class Config(pydantic.BaseSettings):
    #context: Literal['local', 'test', 'stage'] = 'local'

    base_url: str = 'https://summer-patio-stage.gismenu.ru/'
    driver_name: BrowserType = 'firefox'
    version = '98.0'
    hold_driver_at_exit: bool = False
    #window_width: int = 480
    window_width: int = 1170
    #window_height: int = 640
    window_height: int = 2532
    timeout: float = 5.0
    headless: bool = False
    safari_user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
    chrome_device = 'Nexus 5'


# if you want to have optional .env file (without `.context` suffix)
# to allways override default values from .env.local, .env.test, .env.stage
# you may need it,
# as being ignored in .gitignore, – to store sensitive data (aka secrets)


#dotenv.load_dotenv()
'''
# you may emphasize its "secrets" nature by naming it as .env.secrets:
dotenv.load_dotenv(dotenv.find_dotenv('.env.secrets'))
# sometimes people keep such secrets file outside of the project folder, 
# often – in home directory...
from pathlib import Path
dotenv.load_dotenv(Path.home().joinpath('.env.secrets').__str__())
'''

#config = Config(dotenv.find_dotenv(f'.env.{Config().context}'))
#config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))
config = Config(_env_file=path.relative_from_root('.env'))
'''
# if you would keep .env file name for local context (instead of .env.local)
context = Config().context
config = Config(dotenv.find_dotenv('.env' if context == 'local' else f'.env.{context}'

# another example, utilizing custom path helper from selene_in_action.utils.path
from selene_in_action.utils import path
config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))
'''