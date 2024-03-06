from enum import Enum
from myutils.TypeLibrary import CommandType

class Command():
    class Type(Enum):
        CONNECTION = 'C'
        SELECTION = 'S'
        INSERTION = 'I'
        ALTERATION = 'U'
        DELETION = 'D'
        TRANSACTION = 'T'
        
    def __init__(self, command_type : CommandType = "unknown"):
        self.command_type = command_type
        
    def reveal(self):
        attributes = vars(self)  # or self.__dict__ or dir(self)
        print("Attributes of", self.__class__.__name__)
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")