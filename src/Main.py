from board import Board, Node
from file_persistence import FilePersistence
from game import Game
from player import Player
import os


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
        board = Board(len(matrix), len(matrix[0]), matrix, nodes)
        
        # Create the player object
        player = Player(self.player_name)
        
        # Create the game object
        game = Game(board, player)
        
        # Display the initial board
        game.display_board()
        

# Example usage
if __name__ == "__main__":
    # Construct the relative path to the nodes.txt file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "../assets/files/nodes.txt")
    
    main = Main(file_path, "Alice")
    main.run()