from shared.Operation import Operation
from shared.Command import Command
from typing import Self

class SelectionCommand(Command):
    def __init__(self,target:str,columns:list[str],filters:list[str] = None,ordering_terms:list[str]=None) -> Self:
        super().__init__()
        self.TYPE_OF_COMMAND = Operation.SELECTION
        self.target = target
        self.columns = columns
        self.filters = filters
        self.ordering_terms = ordering_terms