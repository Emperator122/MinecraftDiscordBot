from typing import List

from config.bot_config import BotConfig
from models.extract_log_data_dto import ExtractLogDataTask
from modules.my_bot import MyBot
from threading import Lock


class MinecraftServerLogger:
    bot: MyBot = None
    _extract_log_data_tasks: List[ExtractLogDataTask] = []
    _lock = Lock()

    @staticmethod
    def on_console_log_message(msg: str):
        MinecraftServerLogger.send_log_message_to_channel(msg)
        found_tasks = []
        with MinecraftServerLogger._lock:
            for task in MinecraftServerLogger._extract_log_data_tasks:
                if task.response_type.identify(msg):
                    found_tasks.append(task)
                    task.response_type.text = msg
            for found_task in found_tasks:
                MinecraftServerLogger._extract_log_data_tasks.remove(found_task)
        for found_task in found_tasks:
            MinecraftServerLogger.bot.add_item_to_message_queue(found_task.channel_id,
                                                                found_task.response_type.get_reply_text())

    @staticmethod
    def send_log_message_to_channel(msg: str):
        if BotConfig.mc_log_channel_id is None or BotConfig.mc_log_channel_id == 0:
            return
        assert MinecraftServerLogger.bot is not None, 'Не задан ДС бот для логов'
        if msg == '' or msg is None:
            return
        MinecraftServerLogger.bot.add_item_to_message_queue(BotConfig.mc_log_channel_id, msg)

    @staticmethod
    def extract_log_data_task_add(task: ExtractLogDataTask):
        with MinecraftServerLogger._lock:
            MinecraftServerLogger._extract_log_data_tasks.append(task)
