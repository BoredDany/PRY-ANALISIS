from model.AutoSolver import AutoSolver
class MachineController:
    def __init__(self, game):
        self.game = game
        
    def solve(self):
        auto_solver = AutoSolver(self.game)
        res = auto_solver.solve()
        print(res)