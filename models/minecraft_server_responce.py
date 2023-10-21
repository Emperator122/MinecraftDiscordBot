from abc import ABC, abstractmethod
import re

from res.resources import BotMessagesStrings


class MinecraftServerResponse(ABC):
    text: str = None

    @abstractmethod
    def identify(self, text=None) -> bool:
        pass

    @abstractmethod
    def get_reply_text(self) -> str:
        pass


class MinecraftServerUnrecognizedResponse(MinecraftServerResponse):

    def __init__(self, text=None):
        self.text = text

    def identify(self, text=None) -> bool:
        return True

    def get_reply_text(self) -> str:
        return ""


class MinecraftPlayersCountCommandResponse(MinecraftServerResponse):
    _identifyRegexp: str = r'.*There are (\d+) of a max of \d+ players online:.*'

    def __init__(self, text=''):
        self.text = text

    def identify(self, text=None) -> bool:

        if re.match(MinecraftPlayersCountCommandResponse._identifyRegexp, text if text else self.text):
            return True
        return False

    def get_players_count(self):
        matches = re.match(MinecraftPlayersCountCommandResponse._identifyRegexp, self.text)
        if matches:
            return int(matches.group(1))
        else:
            return -1

    def get_reply_text(self) -> str:
        return BotMessagesStrings.get_players_count_message(self.get_players_count())


class MinecraftServerResponseResolver(ABC):
    @staticmethod
    def resolve_response(text: str) -> MinecraftServerResponse:
        candidate = MinecraftPlayersCountCommandResponse(text)
        if candidate.identify():
            return candidate
        return MinecraftServerUnrecognizedResponse(text)
