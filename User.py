class User():
    def __init__(self , name, s) -> None:
        self.name = name
        self.secname = s

    def __str__(self) -> str:
        return self.name + ' ' + self.secname