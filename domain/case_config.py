import inspect
from typing import Text

from httprunner import Config
from httprunner.models import VariablesMapping, TConfig


class CaseConfig(Config):
    def __init__(self, name: Text) -> None:
        super().__init__(name)
        caller_frame = inspect.stack()[1]
        self.__name: Text = name
        self.__base_url: Text = ""
        self.__variables: VariablesMapping = {}
        self.__config = TConfig(name=name, path=caller_frame.filename)

    @property
    def name(self) -> Text:
        return self.__config.name

    @name.setter
    def name(self, name: Text) -> None:
        self.__config.name = name


__all__ = ["CaseConfig"]
