from enum import Enum


class Source(Enum):
    BODY = "BODY"
    QUERY = "QUERY"
    PATH = "PATH"
    HEADERS = "HEADERS"
    COOKIES = "COOKIES"
