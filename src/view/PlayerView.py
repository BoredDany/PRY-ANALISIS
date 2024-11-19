import pygame
import time

class PlayerView:
    def __init__(self, game, board, controller, player):
        self.game = game
        self.board = board
        self.player = player
        self.controller = controller
        self.running = True
        self.selected_node = None
        self.start_time = time.time()  # Para el cronómetro
        self.result_message = ""  # Para el mensaje de verificación

    def run(self):
        pygame.init()
        # Incrementar la altura de la ventana para incluir el espacio adicional para la UI
        screen = pygame.display.set_mode((self.board.screen_width, self.board.screen_height + 80))
        pygame.display.set_caption(self.player.name)
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 24)
        needs_redraw = True

        # Configuración del botón
        button_width, button_height = 200, 50  # Botón más grande
        button_x = 300  # Centrado horizontalmente respecto al cronómetro
        button_y = self.board.screen_height + 15  # Espaciado uniforme
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Verificar si se presiona el botón "Verificar"
                    if button_rect.collidepoint(mouse_pos):
                        if self.controller.won():
                            self.result_message = "¡Ganaste!"
                        else:
                            self.result_message = "Perdiste. Intenta de nuevo."
                        # Forzar redibujado inmediato para reflejar cambios en la pantalla
                        needs_redraw = True

                    # Selección de nodos
                    elif self.controller.selected_node_in_screen(mouse_pos, self.game.matrix):
                        if self.selected_node is None:
                            self.selected_node = mouse_pos
                        else:
                            needs_redraw = self.controller.handle_click(self.selected_node, mouse_pos)
                            self.selected_node = None

            # Actualizar cronómetro
            elapsed_time = time.time() - self.start_time
            formatted_time = time.strftime("%M:%S", time.gmtime(elapsed_time))

            if needs_redraw:
                # Dibujar tablero y conexiones
                screen.fill((255, 255, 255))
                self.board.draw_nodes(screen, self.game.matrix)
                self.board.draw_connections(screen, self.game.edges, self.game, self.board.node_positions)

                # Dibujar cronómetro
                timer_text = font.render(f"Tiempo de juego: {formatted_time}", True, (0, 0, 0))
                screen.blit(timer_text, (50, self.board.screen_height + 25))  # Posición alineada con el botón

                # Dibujar botón
                pygame.draw.rect(screen, (0, 128, 255), button_rect)
                button_text = font.render("Verificar Solución", True, (255, 255, 255))
                text_rect = button_text.get_rect(center=button_rect.center)
                screen.blit(button_text, text_rect)

                # Mostrar mensaje de resultado
                result_text = font.render(self.result_message, True, (0, 128, 0) if "Ganaste" in self.result_message else (255, 0, 0))
                screen.blit(result_text, (550, self.board.screen_height + 25))  # Ajuste horizontal para el mensaje

                pygame.display.update()
                needs_redraw = False

            clock.tick(60)

        pygame.quit()
