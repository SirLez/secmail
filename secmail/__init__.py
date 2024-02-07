from .client import SecMail
from requests import get
from json import loads


try:
    __version__ = '1.0.2'
    __newest__ = loads(get("https://pypi.python.org/pypi/secmail/json").text)["info"]["version"]
    if __version__ != __newest__:
        print(f"\033[1;33m1SecMail New Version!: {__newest__} (Your Using {__version__})\033[1;0m")
except:
    pass
