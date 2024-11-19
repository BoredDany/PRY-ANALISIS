import pygame
from model.Board import Board
from model.Node import Node
from model.Game import Game
from model.Player import Player
from persistence.FilePersistence import FilePersistence
from controller.PlayerController import PlayerController
from controller.MachineController import MachineController
from view.PlayerView import PlayerView  
from view.MachineView import MachineView


class Main:
    def __init__(self, filename):
        self.filename = filename
        self.player_name = ""
        self.input_active = False

    def run(self):
        # Configuración de pantalla
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Menu Principal")
        font = pygame.font.Font(None, 24)
        clock = pygame.time.Clock()

        # Elementos UI
        input_rect = pygame.Rect(300, 200, 200, 40)
        play_button = pygame.Rect(300, 300, 200, 50)
        ai_button = pygame.Rect(300, 400, 200, 50)

        running = True
        while running:
            screen.fill((255, 255, 255))

            # Dibujar elementos
            title = font.render("HASHI", True, (0, 0, 0))
            screen.blit(title, (300, 100))

            pygame.draw.rect(screen, (200, 200, 200), input_rect)
            name_text = font.render(self.player_name, True, (0, 0, 0))
            screen.blit(name_text, (input_rect.x + 10, input_rect.y + 5))

            pygame.draw.rect(screen, (0, 128, 255), play_button)
            play_text = font.render("Jugar", True, (255, 255, 255))
            screen.blit(play_text, (play_button.x + 50, play_button.y + 10))

            pygame.draw.rect(screen, (255, 0, 0), ai_button)
            ai_text = font.render("Juega la Máquina", True, (255, 255, 255))
            screen.blit(ai_text, (ai_button.x + 20, ai_button.y + 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if input_rect.collidepoint(mouse_pos):
                        self.input_active = True
                    else:
                        self.input_active = False

                    if play_button.collidepoint(mouse_pos) and self.player_name.strip():
                        self.start_player_view()
                    elif ai_button.collidepoint(mouse_pos):
                        self.start_ai_view()

                elif event.type == pygame.KEYDOWN and self.input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        self.player_name += event.unicode

            pygame.display.flip()
            clock.tick(60)

    def start_player_view(self):
        persistence = FilePersistence(self.filename)
        matrix, nodes = persistence.load()
        game = Game(len(matrix), len(matrix[0]), matrix, nodes)
        player = Player(self.player_name)
        board = Board()  
        board.node_positions = board.generar_posiciones(game.x, game.y, game.matrix)
        controller = PlayerController(game, board)
        player_view = PlayerView(game, board, controller, player)
        player_view.run()

    def start_ai_view(self):
        persistence = FilePersistence(self.filename)
        matrix, nodes = persistence.load()
        game = Game(len(matrix), len(matrix[0]), matrix, nodes)
        board = Board()
        board.node_positions = board.generar_posiciones(game.x, game.y, game.matrix)
        controller = MachineController(game)
        machine_view = MachineView(game, board, controller)
        machine_view.run()


if __name__ == "__main__":
    main = Main("C:/Users/danym/OneDrive/Documentos/PRY-ANALISIS/assets/files/nodes.txt")
    main.run()
