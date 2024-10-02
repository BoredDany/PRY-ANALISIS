import pygame

def development_screen(screen):
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        screen.fill((255, 255, 255))  # Fondo blanco
        text_surface = font.render("PRÓXIMO DESARROLLO", True, (0, 0, 0))
        screen.blit(text_surface, (screen.get_width() // 2 - 100, screen.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

    pygame.quit()
