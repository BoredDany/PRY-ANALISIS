from model.Board import Board
from model.Node import Node
from model.Game import Game
from model.Player import Player
from persistence.FilePersistence import FilePersistence

class Main:
    def __init__(self, filename, player_name):
        self.filename = filename
        self.player_name = player_name

    def run(self):
        # Create the persistence object
        persistence = FilePersistence(self.filename)
        
        # Load the board data
        matrix, nodes = persistence.load()
        
        # Create the board object
        board = Game(len(matrix), len(matrix[0]), matrix, nodes)
        
        # Create the player object
        player = Player(self.player_name)
        
        # Create the game object
        game = Board(board, player)
        
        # Display the initial board
        game.display_board()
        

if __name__ == "__main__":
    main = Main("C:/Users/danym/OneDrive/Documentos/PRY-ANALISIS/assets/files/nodes.txt", "Alice")
    main.run()