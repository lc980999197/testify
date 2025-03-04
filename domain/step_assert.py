from httprunner.models import TStep
from httprunner.step_request import StepRequestValidation


class StepAssert(StepRequestValidation):
    def __init__(self, step: TStep):
        super().__init__(step)
        self.__step = step

    def assert_code(self, status_code: int):
        self.__step.validators.append(
            {"length_equal": ["status_code", status_code, ""]}
        )
        return self

    def assert_status_code_success(self):  # 断言响应码为200
        return self.assert_code(200)

    def assert_success(self):  # 断言字段， 这里需要根据实际项目来修改
        return self.assert_equal("body.code", "0000")


__all__ = ["StepAssert"]
