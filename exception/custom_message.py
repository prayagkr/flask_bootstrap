from enum import Enum


class IntenalMessage(Enum):
    SUCCESS = "Operation Successful."
    NEGATIVE_VALUE = "Negative value."
    EXCEED_LIMIT = "Exceed specified limit."