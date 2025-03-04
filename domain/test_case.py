from typing import List

from httprunner import Step
from domain.abstract_case import AbstractCase
from domain.case_config import CaseConfig
from conftest import conf


class BaseCase(AbstractCase):

    Name = "BaseCase"

    @property
    def config(self):
        return CaseConfig(self.Name).base_url(conf.base_url)

    @property
    def headers(self):
        return conf.template.headers

    def steps(self) -> List[Step]:
        ...


__all__ = ["BaseCase"]

