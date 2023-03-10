
import os

class Config(object):
    LOGGER = False
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN', None)
    # required for running on Heroku
    URL = os.environ.get('URL', "")
    PORT = int(os.environ.get('PORT', 5000))
    # get a token from ChatBase.com for analytics
    CBTOKEN = os.environ.get('CBTOKEN', None)
    # dump channel
    TG_DUMP_CHANNEL = int(os.environ.get("TG_DUMP_CHANNEL", "0"))
    #
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    # the above example values will no longer work.
    # changed to List usage to circumvent https://t.me/H4CK1NG_CL4SSES


class Development(Config):
    LOGGER = True
