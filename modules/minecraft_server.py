import subprocess
import pathlib
import threading


class MinecraftServer:
    launch_file_path = ''
    minecraft_process: subprocess.Popen = None
    on_console_log_message: callable(str) = None

    def __init__(self, launch_file_path, on_console_log_message=None):
        self.launch_file_path = launch_file_path
        self.on_console_log_message = on_console_log_message

    def is_launched(self):
        return self.minecraft_process is not None and self.minecraft_process.poll() is None

    def start_server(self):
        assert not self.is_launched(), 'Сервер не должен быть запущен!'
        parent_folder = str(pathlib.Path(self.launch_file_path).parent.resolve())
        MinecraftServer.minecraft_process = subprocess.Popen([self.launch_file_path], cwd=parent_folder,
                                                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        insert_thread = threading.Thread(target=self._console_log)
        insert_thread.daemon = True
        insert_thread.start()

    def stop_server(self):
        assert self.is_launched(), 'Сервер должен быть запущен!'
        self.minecraft_process.communicate(input=b'stop')

    def execute_command(self, command: str):
        self.minecraft_process.stdin.write(('%s\n' % command).encode())
        self.minecraft_process.stdin.flush()

    def _console_log(self):
        while True:
            try:
                line = self.minecraft_process.stdout.readline()
                if self.minecraft_process.poll() is not None:
                    break
                if line:
                    output = line.strip().decode('utf-8')
                    if self.on_console_log_message is not None:
                        self.on_console_log_message(output)
                    print(output)
            except ValueError:
                break
