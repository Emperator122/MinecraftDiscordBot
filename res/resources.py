class BotMessagesStrings:
    success_launch_message = 'Включение сервера...'
    not_success_launch_message = 'Сервер уже включен.'
    stopping_message = 'Выключение сервера...'
    success_stop_message = 'Сервер выключен.'
    not_success_stop_message = 'Сервер уже выключен.'
    status_on_message = 'Сервер онлайн.'
    status_off_message = 'Сервер оффлайн.'

    help_title = 'Список команд:\r\n'
    help_commands_list = {
        'server start': 'Запуск сервера;',
        'server stop': 'Остановка сервера. Корректно завершает работу сервера.',
        'server status': 'Запущен ли на даннный момент сервер.',
        'server sleep': 'Делает утро на сервере.',
        'server players_count': 'Получает количество игроков онлайн.',
        'sleep': 'Делает утро на сервере.',
        'help': 'Помощь.',
    }
    sleep_message = 'Сервер успешно поспал!'
    task_get_players_count_message = 'Задача получения информации о количестве игроков отправлена на сервер...'

    @staticmethod
    def get_players_count_message(players_count):
        return f"Количество игроков на сервере: {players_count}"


class BotMessagesStyles:
    help_color = 0x3944bc


class ConsoleMessagesString:
    launching_message = 'Бот запущен.'
