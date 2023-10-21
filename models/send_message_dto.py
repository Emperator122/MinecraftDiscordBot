class SendMessageDto:
    channel_id: int = None
    message_text: str = None

    def __init__(self, channel_id: int, message_text: str):
        self.channel_id = channel_id
        self.message_text = message_text
