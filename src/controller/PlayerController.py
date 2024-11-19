class PlayerController:
    def __init__(self, game, board):
        self.game = game
        self.board = board
        
    def selected_node_in_screen(self, pos, matrix):
        node = self.board.get_node(pos, matrix)
        if node is not None:
            return True
        return False
        
    def won(self):
        return self.game.won()
        
    def handle_click(self, selected_node, pos):
        node1 = self.board.get_node(selected_node, self.game.matrix)
        node2 = self.board.get_node(pos, self.game.matrix)
        
        print("NODE 1: ", node1.display())
        print("NODE 2: ", node2.display())
        
        if node1 is None or node2 is None:
            return False  # No redibujar aún
        
        else:
            
            # Si es conexion para borrar
            if self.game.count_node_connections(node1, node2) == 2:
                self.game.delete_edge(node1, node2)
                self.game.delete_edge(node2, node1)
                return True
                
            # Si es conexion valida
            if self.game.valid_connection(node1, node2, self.game.edges):
                self.game.add_edge(node1, node2)  
                return True  # Redibujar
            
            else:
                return False  # No redibujar