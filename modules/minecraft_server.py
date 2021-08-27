import os
from utils import utils


class MinecraftServer:
    launch_file_path = ''
    window_title = ''
    process_name = ''
    cmd_encoding = ''

    def __init__(self, launch_file_path, window_title, process_name, cmd_encoding):
        self.launch_file_path = launch_file_path
        self.window_title = window_title
        self.process_name = process_name
        self.cmd_encoding = cmd_encoding

    def is_launched(self):
        return utils.process_exists(self.window_title, self.process_name, self.cmd_encoding)

    def start_server(self):
        os.startfile(self.launch_file_path)

    def stop_server(self):
        os.system('taskkill /F /FI "WindowTitle eq '+self.window_title+'" /T')
