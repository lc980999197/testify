from domain.test_case import BaseCase, Step
from domain.request import Requests


class TestCaseOptimize(BaseCase):

    Name = "新增优化问题"

    def steps(self):
        return [
            Step(
                Requests("新增优化问题").post("/api/exstudio/v2/model-optimize").with_headers(**self.headers).with_json(
                    {
                        "title": "新增优化问题",
                }).validate().assert_success()
            )
        ]

