from typing import Dict, Any

from pydantic import BaseModel


class Template(BaseModel):
    headers: Dict[str, Any] = dict()
    timeout: int = 10
    retries: int = 3

