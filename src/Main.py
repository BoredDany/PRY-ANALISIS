import pygame
from model.Board import Board
from model.Node import Node
from model.Game import Game
from model.Player import Player
from persistence.FilePersistence import FilePersistence
from controller.Controller import Controller

class Main:
    def __init__(self, filename, player_name):
        self.filename = filename
        self.player_name = player_name

    def run(self):
        # Inicializar información del tablero de juego
        persistence = FilePersistence(self.filename)
        matrix, nodes = persistence.load()
        game = Game(len(matrix), len(matrix[0]), matrix, nodes)
        player = Player(self.player_name)
        board = Board()  # Board recibe game y player como parámetros
        board.node_positions = board.generar_posiciones(game.x, game.y, game.matrix)
        print("matriz: ", game.x, ", ", game.y)
        
        # Inicializar controlador
        controller = Controller(game, board)

        # Inicializar pantalla
        pygame.init()
        screen = pygame.display.set_mode((board.screen_width, board.screen_height))
        pygame.display.set_caption("Game Board")
        clock = pygame.time.Clock()
        

        running = True
        needs_redraw = True  
        selected_node = None
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if controller.selected_node_in_screen(mouse_pos, game.matrix) == True:
                        print(board.get_node(mouse_pos, matrix).display())
                        if selected_node is None:
                            selected_node = mouse_pos
                        else:
                            needs_redraw = controller.handle_click(selected_node, mouse_pos) 
                            selected_node = None
            
            if needs_redraw:
                print("CAMBIOS-----------")
                game.display()
                screen.fill((255, 255, 255)) 
                board.draw_nodes(screen, game.matrix)
                board.draw_connections(screen, game.edges, game)
                pygame.display.update()
                needs_redraw = False
            
            clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    main = Main("C:/Users/danym/OneDrive/Documentos/PRY-ANALISIS/assets/files/nodes.txt", "Alice")
    main.run()
