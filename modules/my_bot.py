import threading

from models.send_message_dto import SendMessageDto
from discord.ext import tasks, commands
from queue import Queue


class MyBot(commands.Bot):
    lock = threading.Lock()
    message_queue: Queue[SendMessageDto] = Queue()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg_sent = False

    async def on_ready(self):
        await self.message_queue_extract_handler.start()

    @tasks.loop(seconds=1)
    async def message_queue_extract_handler(self):
        with self.lock:
            while not self.message_queue.empty():
                message_data = self.message_queue.get()
                channel = self.get_channel(message_data.channel_id)
                await channel.send(message_data.message_text)

    def add_item_to_message_queue(self, channel_id: int, message: str):
        with self.lock:
            self.message_queue.put(SendMessageDto(channel_id, message))