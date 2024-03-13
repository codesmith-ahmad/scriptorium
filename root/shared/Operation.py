from enum import Enum

class Operation(Enum):
    GENERIC = 'G'
    CONNECTION = 'C'
    SELECTION = 'S'
    INSERTION = 'I'
    ALTERATION = 'U'
    DELETION = 'D'
    TRANSACTION = 'T'