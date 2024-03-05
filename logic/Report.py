
class Report:
    def __init__(self):
        pass
        
    def __str__(self) -> str:
        attributes = vars(self)  # or self.__dict__ or dir(self)
        s = ''
        s += "Attributes of " + self.__class__.__name__ + "\n"
        for attribute, value in attributes.items():
            s += f"{attribute}: {value}\n"
        return s