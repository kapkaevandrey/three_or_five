import enum
import typing

import settings


class ResultMessageText(enum.Enum):
    DIV_BY_THREE = settings.MESSAGE_RESPONSE['divided by three']
    DIV_BY_FIVE = settings.MESSAGE_RESPONSE['divided by five']
    DIV_BY_THREE_AND_FIVE = settings.MESSAGE_RESPONSE['divided by three and five']
    NO_DIV = settings.MESSAGE_RESPONSE['no divided by three or five']


class ResultDividedStringCodes(enum.Enum):
    DIV_BY_THREE = 'foo'
    DIV_BY_FIVE = 'bar'
    DIV_BY_THREE_AND_FIVE = 'foobar'
    NO_DIV = 'no_divided'


class SimpleResponse:
    def __init__(self, message: typing.Optional[str] = None, string_code: typing.Optional[str] = None):
        self.message = message
        self.string_code = string_code
