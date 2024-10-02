import pygame
from game.main_menu import main_menu
from game.screen_features import WIDTH, HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("El juego Hashiwokakero")

    main_menu(screen)

if __name__ == "__main__":
    main()
