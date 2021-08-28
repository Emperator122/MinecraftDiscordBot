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
        'server stop': 'Принудительная остановка сервера. Может откатить до последнего автосохранения мира.'
                       'Лучше осуществлять, когда на сервере нет игроков и через некоторое время '
                       'после каких-либо изменений.',
        'server status': 'Запущен ли на даннный момент сервер.',
        'help': 'Помощь',
    }


class BotMessagesStyles:
    help_color = 0x3944bc


class ConsoleMessagesString:
    launching_message = 'Бот запущен.'
