from shared.Operation import Operation
from typing import Self

class Report:
        
    def __init__(self) -> Self:
        self.TYPE_OF_REPORT = Operation.GENERIC
        
    def __str__(self) -> str:
        attributes = vars(self)  # or self.__dict__ or dir(self)
        s = ''
        s += "Attributes of " + self.__class__.__name__ + "\n"
        for attribute, value in attributes.items():
            s += f"{attribute}: {value}\n"
        return s