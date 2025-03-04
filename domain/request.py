from typing import Text

from httprunner.models import TStep, TRequest, MethodEnum
from httprunner.step_request import RequestWithOptionalArgs as RequestOptions, RunRequest
from domain.step_assert import StepAssert


class RequestWithOptionalArgs(RequestOptions):
    def __init__(self, step: TStep):
        super().__init__(step)

    def validate(self) -> StepAssert:
        return StepAssert(self.__step)


class Requests(RunRequest):
    def __init__(self, name: Text):
        super().__init__(name)
        self.__step = TStep(name=name)

    def get(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.GET, url=url)
        return RequestWithOptionalArgs(self.__step)

    def post(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.POST, url=url)
        return RequestWithOptionalArgs(self.__step)

    def put(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.PUT, url=url)
        return RequestWithOptionalArgs(self.__step)

    def head(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.HEAD, url=url)
        return RequestWithOptionalArgs(self.__step)

    def delete(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.DELETE, url=url)
        return RequestWithOptionalArgs(self.__step)

    def options(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.OPTIONS, url=url)
        return RequestWithOptionalArgs(self.__step)

    def patch(self, url: Text) -> RequestWithOptionalArgs:
        self.__step.request = TRequest(method=MethodEnum.PATCH, url=url)
        return RequestWithOptionalArgs(self.__step)


__all__ = ["Requests"]

