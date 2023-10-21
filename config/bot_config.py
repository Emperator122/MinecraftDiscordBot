import os

from dotenv import load_dotenv


class BotConfig:
    token = None
    prefix = None
    mc_log_channel_id = None


def init_config():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dotenv_exist = os.path.exists(dotenv_path)
    assert dotenv_exist, '.env not found in config folder'
    if dotenv_exist:
        load_dotenv(dotenv_path)
        BotConfig.token = os.getenv("TOKEN")
        BotConfig.prefix = os.getenv("PREFIX")
        BotConfig.mc_log_channel_id = int(os.getenv("MC_LOG_CHANNEL_ID"))

init_config()
