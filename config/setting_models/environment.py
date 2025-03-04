from typing import Dict

from pydantic import BaseModel, Field


class Environment(BaseModel):
    base_url: str = Field(alias="base_url")
    db_url: str = Field(alias="db_url")


class Environments(BaseModel):
    root: Dict[str, Environment]

    def __getattr__(self, name: str):
        # 支持属性访问，如 environments.test
        return self.root.get(name)

    def __getitem__(self, name: str):
        # 支持字典访问，如 environments["test"]
        return self.root.get(name)
