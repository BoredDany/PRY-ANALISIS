class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def display(self):
        return f"Player {self.name} with score {self.score}"