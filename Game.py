class Game():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.users = []

    def connect(self, user):
        self.users.append(user.id)

    def toJSON(self):
        buffer = {
            "id": self.id,
            "name": self.name,
            "users": self.users
        }
        return buffer