from models.minecraft_server_responce import MinecraftServerResponse


class ExtractLogDataTask:
    channel_id: int = None
    response_type: MinecraftServerResponse = None

    def __init__(self, channel_id: int, response_type: MinecraftServerResponse):
        self.channel_id = channel_id
        self.response_type = response_type
