from abc import ABC, abstractmethod

class Report:
    def __init__(self, success: bool = False) -> None:
        self.success : bool = success
        
    def __str__(self) -> str:
        return f"Report[sucess={self.success}]"