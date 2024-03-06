from shared.Operation import Operation
from shared.Report import Report
from typing import Self

class ConnectionReport(Report):
    def __init__(self,sqlite_version:str = None, list_of_tables : list[str] = None) -> Self:
        super().__init__()
        self.TYPE_OF_REPORT = Operation.CONNECTION
        self.sqlite_version = sqlite_version
        self.list_of_tables = list_of_tables