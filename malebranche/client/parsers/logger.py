import typing as t
from datetime import datetime
import orjson
import uuid

from malebranche.client.exceptions import MessageFormatNotValid


class LoggerParser(object):
    __slots__ = "_level", "_messages", "_uuid", "_parent"

    def __init__(self, level="INFO", parent=None):
        self._level = level
        self._messages = []
        uuid_instance = uuid.uuid1()
        self._uuid = str(uuid_instance)
        if parent is not None:
            self._parent = parent
        else:
            self._parent = None

    @property
    def stack(self):
        return self._messages

    def info(self, message: t.Any):
        message_formatted = self.__get_formatted_message(message)
        self._add_messagge(datetime.now(), message_formatted, self._level)

    def warning(self, message: t.Any):
        message_formatted = self.__get_formatted_message(message)
        self._add_messagge(datetime.now(), message_formatted, self._level)

    def debug(self, message: t.Any):
        message_formatted = self.__get_formatted_message(message)
        self._add_messagge(datetime.now(), message_formatted, self._level)

    def error(self, message: t.Any):
        message_formatted = self.__get_formatted_message(message)
        self._add_messagge(datetime.now(), message_formatted, self._level)

    def send(self):
        ...

    def _add_messagge(self, date: t.Any, message: str, level: str):
        self._messages.append({
            "date": date,
            "level": level,
            "message": self.__get_formatted_message(message)
        })

    def __get_formatted_message(self, message: t.Any) -> str:
        if isinstance(message, str):
            return message
        else:
            if isinstance(message, int) or isinstance(message, float) or isinstance(message, int):
                return str(message)
            elif isinstance(message, dict) or isinstance(message, list):
                return orjson.dumps(message)
            else:
                raise MessageFormatNotValid()