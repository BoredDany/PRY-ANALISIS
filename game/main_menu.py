import pygame
from game.button import Button
from game.game_screen import game_screen
from game.development_screen import development_screen
from game.screen_features import WIDTH, HEIGHT, WHITE, BLACK, GREEN, RED

def main_menu(screen):
    pygame.init()
    font = pygame.font.Font(None, 30)
    
    def start_game():
        game_screen(screen)

    def show_development():
        development_screen(screen)
    
    # Crear botones
    button_width = 200
    button_height = 50
    buttons = [
        Button((WIDTH - button_width) // 2, HEIGHT // 2 + 20, button_width, button_height, "HUMANO JUEGA", font, GREEN, start_game),
        Button((WIDTH - button_width) // 2, HEIGHT // 2 + 90, button_width, button_height, "MAQUINA JUEGA", font, RED, show_development)
    ]

    running = True
    while running:
        screen.fill(WHITE)
        font_title = pygame.font.Font(None, 64)
        font_subtitle = pygame.font.Font(None, 36)

        # Título y subtítulo
        title = font_title.render("¡Bienvenidos!", True, BLACK)
        subtitle = font_subtitle.render("Selecciona tipo de jugador", True, BLACK)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 3))

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
