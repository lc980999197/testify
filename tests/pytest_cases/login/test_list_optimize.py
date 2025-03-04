from typing import List

from httprunner import Step

from domain.test_case import BaseCase
from domain.request import Requests


class TestListOptimize(BaseCase):

    Name = "列表接口"

    def steps(self) -> List[Step]:

        return [
            Step(
                Requests("列表接口").get("/api/exstudio/v2/model-optimize/list?pageNo=1&pageSize=10&appId=81").validate().assert_success()
            ),
        ]