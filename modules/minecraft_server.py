import subprocess
import pathlib


class MinecraftServer:
    launch_file_path = ''
    minecraft_process: subprocess.Popen = None

    def __init__(self, launch_file_path):
        self.launch_file_path = launch_file_path

    def is_launched(self):
        return self.minecraft_process is not None and self.minecraft_process.poll() is None

    def start_server(self):
        assert not self.is_launched(), 'Сервер не должен быть запущен!'
        parent_folder = str(pathlib.Path(self.launch_file_path).parent.resolve())
        MinecraftServer.minecraft_process = subprocess.Popen([self.launch_file_path], cwd=parent_folder,
                                                             stdin=subprocess.PIPE)

    def stop_server(self):
        assert self.is_launched(), 'Сервер должен быть запущен!'
        self.minecraft_process.communicate(input=b'stop')
