class User():
    def __init__(self , name, s, id) -> None:
        self.name = name
        self.secname = s
        self.id = id

    def __str__(self):
        return self.name + ' ' + self.secname 