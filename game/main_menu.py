import pygame
from game.button import Button
from game.game_screen import game_screen
from game.development_screen import development_screen

def main_menu(screen):
    pygame.init()
    font = pygame.font.Font(None, 36)
    
    def start_game():
        game_screen(screen)

    def show_development():
        development_screen(screen)
    
    # Crear botones
    buttons = [
        Button(200, 200, 200, 50, "JUGAR", font, (0, 0, 255), start_game),
        Button(200, 300, 200, 50, "MAQUINA JUEGA", font, (255, 0, 0), show_development)
    ]

    running = True
    while running:
        screen.fill((0, 0, 0))  # Fondo negro
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                button.handle_event(event)
        
        # Dibujar botones
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()

    pygame.quit()
