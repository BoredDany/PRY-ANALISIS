import pygame
from game.main_menu import main_menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 680))
    pygame.display.set_caption("El juego Hashiwokakero")

    main_menu(screen)

if __name__ == "__main__":
    main()
