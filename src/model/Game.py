class Game:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.time = 0

    def connect_nodes(self, node1, node2):
        if self.is_valid_connection(node1, node2):
            self.board.add_edge(node1, node2)
        else:
            print("Invalid connection")

    def is_valid_connection(self, node1, node2):
        return True
    
    def won(self):
        return True
    
    def delete_connection(self, node1, node2):
        return True
    
    def display_board(self):
        self.board.display()