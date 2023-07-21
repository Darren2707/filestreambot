# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '9987125'))
    API_HASH = str(getenv('API_HASH', 'db97d01ceffed9938ef4a6297ba2954e'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5511455979:AAFC_waIfPEV-VnDn25YN0SiawfVMNwQHnU'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001976431041'))
    PORT = int(getenv('PORT', '56309'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '172.17.0.15'))
    OWNER_ID = int(getenv('OWNER_ID', '1529044460'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Darren_Samuel'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '172.17.0.15:56309')) if not ON_HEROKU or getenv('FQDN', '172.17.0.15:56309') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Darrem01:samuel123@cluster0.jctjrdc.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'TMVPEDIA'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
