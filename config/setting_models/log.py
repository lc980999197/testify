import logging

from pydantic import BaseModel


class LogConfig(BaseModel):
    level: str
    path: str
    archive: int  # 日志保留月份数

    def get_level(self):
        return getattr(logging, self.level.upper())

