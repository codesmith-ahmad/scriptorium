from shared.Operation import Operation
from shared.Command import Command
from typing import Self

class ConnectionCommand(Command):
    def __init__(self,connect_to:str) -> Self:
        super().__init__()
        self.TYPE_OF_COMMAND = Operation.CONNECTION
        self.connect_to = connect_to