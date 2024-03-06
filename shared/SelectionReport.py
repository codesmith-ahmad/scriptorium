from shared.Operation       import Operation
from shared.Report          import Report
from typing                 import Self

class SelectionReport(Report):
    def __init__(
        self,
        table: str = None,
        table_info: list[tuple] = None,
        headers: list[str] = None,
        query_results: list[tuple] = None) -> Self:
        super().__init__()
        self.TYPE_OF_REPORT = Operation.SELECTION
        self.table = table
        self.table_info = table_info
        self.headers = headers
        self.query_results = query_results