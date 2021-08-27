class MinecraftServerConfig:
    launch_file_path = 'start.bat.lnk'  # Путь к файлу запуска сервера (lnk, bat, etc.) (для запуска)
    window_title = 'start.bat*'  # Заголовок активного окна (по ней будет закрываться сервер), можно юзать фильтр
    process_name = 'cmd.exe'  # Имя процесса (проверка на запуск осуществляется через window_title+process_name)
    cmd_encoding = 'cp866'  # Кодировка командной строки, для RU WIN10 - 'cp866'
