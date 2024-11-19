import pygame

class MachineView:
    def __init__(self, game, board, controller):
        self.game = game
        self.board = board
        self.controller = controller
        self.running = True

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.board.screen_width, self.board.screen_height))
        pygame.display.set_caption("MACHINE PLAYING")

        clock = pygame.time.Clock()

        # Resolver 
        self.controller.solve()
        
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Dibujar fondo blanco
            screen.fill(self.board.background_color)

            # Dibujar nodos y conexiones actualizados
            self.board.draw_nodes(screen, self.game.matrix)
            self.board.draw_connections(screen, self.game.edges, self.game, self.board.node_positions)

            # Actualizar pantalla
            pygame.display.flip()

            # Controlar la velocidad del bucle
            clock.tick(60)

        pygame.quit()
