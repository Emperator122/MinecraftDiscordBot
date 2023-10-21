
from config.bot_config import BotConfig
from modules.my_bot import MyBot


class MinecraftServerLogger:
    bot: MyBot = None

    @staticmethod
    def on_console_log_message(msg: str):
        if BotConfig.mc_log_channel_id is None or BotConfig.mc_log_channel_id == 0:
            return
        assert MinecraftServerLogger.bot is not None, 'Не задан ДС бот для логов'
        if msg == '' or msg is None:
            return
        MinecraftServerLogger.bot.add_item_to_message_queue(BotConfig.mc_log_channel_id, msg)
