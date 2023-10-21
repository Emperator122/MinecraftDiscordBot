import os

from dotenv import load_dotenv


class MinecraftServerConfig:
    # Путь к файлу запуска сервера (bat) (для запуска). Рабочая директория будет совпадать с родительской
    # директорией файла
    launch_file_path = None


def init_config():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dotenv_exist = os.path.exists(dotenv_path)
    assert dotenv_exist, '.env not found in config folder'
    if dotenv_exist:
        load_dotenv(dotenv_path)
        MinecraftServerConfig.launch_file_path = os.getenv("LAUNCH_FILE_PATH")

init_config()
