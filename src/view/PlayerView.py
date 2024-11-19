import pygame

class PlayerView:
    def __init__(self, game, board, controller):
        self.game = game
        self.board = board
        self.controller = controller
        self.running = True
        self.selected_node = None

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.board.screen_width, self.board.screen_height))
        pygame.display.set_caption("Player View")
        clock = pygame.time.Clock()
        needs_redraw = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.controller.selected_node_in_screen(mouse_pos, self.game.matrix):
                        if self.selected_node is None:
                            self.selected_node = mouse_pos
                        else:
                            needs_redraw = self.controller.handle_click(self.selected_node, mouse_pos)
                            self.selected_node = None

            if needs_redraw:
                screen.fill((255, 255, 255))
                self.board.draw_nodes(screen, self.game.matrix)
                self.board.draw_connections(screen, self.game.edges, self.game, self.board.node_positions)
                pygame.display.update()
                needs_redraw = False

            clock.tick(60)

        pygame.quit()
