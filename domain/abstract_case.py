import abc

import abc
from typing import List, Dict

from httprunner import HttpRunner, Step


class AbstractCase(abc.ABC, HttpRunner):
    Name = "BaseCase"

    @property
    def teststeps(self) -> List[Step]:
        return self.steps()

    @abc.abstractmethod
    def steps(self) -> List[Step]:
        ...

    def test_start(self, param: Dict = None) -> None:  # 解决pytest 用例输出不为none产生warning，但是需要看是否影响httprunner的报告产生
        super().test_start(param)
