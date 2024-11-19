class MachineController:
    def __init__(self, game):
        self.game = game
        
    def solve(self):
        self.game.solve()