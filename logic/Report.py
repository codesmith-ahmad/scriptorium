from enum import Enum
from myutils.TypeLibrary import ReportType

class Report:
    class Type(Enum):
        CONNECTION = 'C'
        SELECTION = 'S'
        INSERTION = 'I'
        ALTERATION = 'U'
        DELETION = 'D'
        TRANSACTION = 'T'
        
    def __init__(self, report_type : ReportType = "unknown"):
        self.report_type = report_type
        
    def __str__(self) -> str:
        attributes = vars(self)  # or self.__dict__ or dir(self)
        s = ''
        s += "Attributes of " + self.__class__.__name__ + "\n"
        for attribute, value in attributes.items():
            s += f"{attribute}: {value}\n"
        return s