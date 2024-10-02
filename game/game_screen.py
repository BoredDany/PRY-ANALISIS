import pygame
from game.utils import leer_archivo, generar_posiciones, dibujar_nodos, conectar_nodos, es_conexion_valida, cruza_conexion, verificar_conexiones

WHITE = (255, 255, 255)

def game_screen(screen):
    running = True
    font = pygame.font.SysFont(None, 30)  # Fuente más pequeña para el botón
    message_font = pygame.font.SysFont(None, 30)  # Ajustar el tamaño de la fuente del mensaje
    message = ""
    
    # Cargar datos desde archivo
    dimensions, matrix = leer_archivo("assets/files/nodos.txt")
    node_positions = generar_posiciones(dimensions, matrix)

    # Ajustar las posiciones de los nodos para dejar espacio para el texto
    y_offset = 50  # Espacio adicional desde el borde superior
    for key in node_positions:
        node_positions[key] = (node_positions[key][0], node_positions[key][1] + y_offset)

    # Lista de conexiones
    connections = []
    selected_node = None

    # Definir el rectángulo del botón en la parte superior izquierda con tamaño pequeño
    button_width, button_height = 100, 40  # Tamaño reducido del botón
    button_x = 10  # Posición en la esquina superior izquierda (10 píxeles desde el borde izquierdo)
    button_y = 10  # 10 píxeles desde el borde superior
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    while running:
        try:
            screen.fill(WHITE)  # Fondo blanco
            
            # Dibujar nodos y conexiones
            dibujar_nodos(screen, matrix, node_positions, connections)
            conectar_nodos(screen, connections)

            # Dibujar el botón en la pantalla
            pygame.draw.rect(screen, (0, 0, 255), button_rect)  # Color del botón
            button_text = font.render('Verificar', True, (255, 255, 255))  # Texto más pequeño
            screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

            # Dibujar el mensaje al lado del botón
            if message:
                message_surface = message_font.render(message, True, (0, 0, 0))
                message_x = button_rect.x + button_width + 20  # 20 píxeles de margen desde el borde derecho del botón
                message_y = button_rect.y + (button_height - message_surface.get_height()) // 2  # Centrar verticalmente el mensaje respecto al botón
                screen.blit(message_surface, (message_x, message_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Verificar si se ha hecho clic en el botón
                    if button_rect.collidepoint(mouse_pos):
                        if verificar_conexiones(matrix, node_positions, connections):
                            message = "¡Todas las conexiones son correctas!"
                        else:
                            message = "Hay errores en las conexiones."

                    # Determinar si se ha hecho clic en algún nodo
                    for node, position in node_positions.items():
                        distance = ((mouse_pos[0] - position[0]) ** 2 + (mouse_pos[1] - position[1]) ** 2) ** 0.5
                        if distance < 20:  # Si está dentro del nodo
                            if selected_node is None:
                                selected_node = position
                            else:
                                nueva_conexion = (selected_node, position)
                                if (es_conexion_valida(selected_node, position) and
                                    not cruza_conexion(nueva_conexion, connections)):

                                    if connections.count((selected_node, position)) + connections.count((position, selected_node)) == 2:
                                        # Eliminar todas las conexiones entre los nodos seleccionados
                                        connections = [conn for conn in connections if conn != (selected_node, position) and conn != (position, selected_node)]
                                    else:
                                        connections.append((selected_node, position))

                                    selected_node = None

                                    # Redibujar la pantalla
                                    screen.fill(WHITE)
                                    dibujar_nodos(screen, matrix, node_positions, connections)
                                    conectar_nodos(screen, connections)
                            break

            pygame.display.update()

        except Exception as e:
            print(f"Error: {e}")

    # Volver al menú principal después de que el ciclo termine
    return
