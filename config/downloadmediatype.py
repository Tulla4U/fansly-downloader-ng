"""Download Media Type"""

from strenum import StrEnum
from enum import auto


class DownloadMediaType(StrEnum):
    ALL = auto()
    IMAGE = auto()
    VIDEO = auto()
