from enum import Enum


class DataSource(Enum):
    #   Enum to hold possibilities for obtaining corona table
    TODAY_TABLE = 0
    YESTERDAY_TABLE = 1
