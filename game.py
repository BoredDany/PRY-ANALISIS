import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla y colores
WIDTH, HEIGHT = 600, 650  # Aumentar la altura para incluir el botón
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El juego Hashiwokakero")

# Leer archivo y generar nodos
def leer_archivo(filename):
    with open(filename, 'r') as file:
        dimensions = list(map(int, file.readline().split(',')))
        matrix = [list(map(int, line.strip())) for line in file]
    return dimensions, matrix

# Función para dibujar nodos
def dibujar_nodos(matrix, node_positions, conexiones):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:
                pygame.draw.circle(screen, BLACK, node_positions[(x, y)], 20)
                # Mostrar el número del nodo
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, WHITE)
                screen.blit(text, (node_positions[(x, y)][0] - 10, node_positions[(x, y)][1] - 10))

# Generar las posiciones de los nodos (en este caso, espaciar automáticamente)
def generar_posiciones(dimensions, matrix):
    node_positions = {}
    x_spacing = WIDTH // dimensions[0]
    y_spacing = (HEIGHT - 50) // dimensions[1]  # Ajustar para incluir el botón

    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:
                node_positions[(x, y)] = (x * x_spacing + x_spacing // 2, y * y_spacing + y_spacing // 2)

    return node_positions

# Función para conectar nodos
def conectar_nodos(connections):
    radius = 20  # Radio del círculo del nodo
    for node1, node2 in connections:
        if connections.count((node1, node2)) + connections.count((node2, node1)) == 2:
            
            if node1[0] == node2[0]:  # Conexión vertical
                offset = 5
                if node1[1] < node2[1]:
                    pygame.draw.line(screen, RED, (node1[0] - offset, node1[1] + radius), (node2[0] - offset, node2[1] - radius), 5)
                    pygame.draw.line(screen, RED, (node1[0] + offset, node1[1] + radius), (node2[0] + offset, node2[1] - radius), 5)
                else:
                    pygame.draw.line(screen, RED, (node2[0] - offset, node2[1] + radius), (node1[0] - offset, node1[1] - radius), 5)
                    pygame.draw.line(screen, RED, (node2[0] + offset, node2[1] + radius), (node1[0] + offset, node1[1] - radius), 5)
            
            elif node1[1] == node2[1]:  # Conexión horizontal
                offset = 5
                if node1[0] < node2[0]:
                    pygame.draw.line(screen, RED, (node1[0] + radius, node1[1] - offset), (node2[0] - radius, node2[1] - offset), 5)
                    pygame.draw.line(screen, RED, (node1[0] + radius, node1[1] + offset), (node2[0] - radius, node2[1] + offset), 5)
                else:
                    pygame.draw.line(screen, RED, (node2[0] + radius, node2[1] - offset), (node1[0] - radius, node1[1] - offset), 5)
                    pygame.draw.line(screen, RED, (node2[0] + radius, node2[1] + offset), (node1[0] - radius, node1[1] + offset), 5)
        else:
            if node1[0] == node2[0]:  # Conexión vertical
                if node1[1] < node2[1]:
                    pygame.draw.line(screen, RED, (node1[0], node1[1] + radius), (node2[0], node2[1] - radius), 5)
                else:
                    pygame.draw.line(screen, RED, (node2[0], node2[1] + radius), (node1[0], node1[1] - radius), 5)
            
            elif node1[1] == node2[1]:  # Conexión horizontal
                if node1[0] < node2[0]:
                    pygame.draw.line(screen, RED, (node1[0] + radius, node1[1]), (node2[0] - radius, node2[1]), 5)
                else:
                    pygame.draw.line(screen, RED, (node2[0] + radius, node2[1]), (node1[0] - radius, node1[1]), 5)

# Verificar si una conexión es válida (horizontal o vertical)
def es_conexion_valida(node1, node2):
    return node1[0] == node2[0] or node1[1] == node2[1]

# Verificar si una conexión cruza con otra
def cruza_conexion(nueva_conexion, conexiones):
    for conexion in conexiones:
        if (nueva_conexion[0][0] == nueva_conexion[1][0] == conexion[0][0] == conexion[1][0] or
            nueva_conexion[0][1] == nueva_conexion[1][1] == conexion[0][1] == conexion[1][1]):
            continue
        if (min(nueva_conexion[0][0], nueva_conexion[1][0]) < max(conexion[0][0], conexion[1][0]) and
            max(nueva_conexion[0][0], nueva_conexion[1][0]) > min(conexion[0][0], conexion[1][0]) and
            min(nueva_conexion[0][1], nueva_conexion[1][1]) < max(conexion[0][1], conexion[1][1]) and
            max(nueva_conexion[0][1], nueva_conexion[1][1]) > min(conexion[0][1], conexion[1][1])):
            return True
    return False

# Contar conexiones de un nodo
def contar_conexiones(nodo, conexiones):
    return sum(1 for conexion in conexiones if nodo in conexion)

# Dibujar botón
def dibujar_boton():
    font = pygame.font.Font(None, 36)
    text = font.render("Verificar", True, WHITE)
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT - 40, 150, 30)
    pygame.draw.rect(screen, BLUE, button_rect)
    screen.blit(text, (WIDTH // 2 - 60, HEIGHT - 35))
    return button_rect

def verificar_conexiones(matrix, node_positions, conexiones):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:  # Solo nodos con valor > 0
                nodo_pos = node_positions[(x, y)]
                conexiones_actuales = contar_conexiones(nodo_pos, conexiones)
                if conexiones_actuales != value:
                    return False
    return True


def main():
    # Cargar datos desde archivo
    dimensions, matrix = leer_archivo("nodos.txt")
    node_positions = generar_posiciones(dimensions, matrix)

    # Lista de conexiones
    connections = []
    selected_node = None
    
    screen.fill(WHITE)

    # Dibujar nodos
    dibujar_nodos(matrix, node_positions, connections)
    button_rect = dibujar_boton()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Verificar si se ha hecho clic en el botón
                if button_rect.collidepoint(mouse_pos):
                    if verificar_conexiones(matrix, node_positions, connections):
                        print("¡Todas las conexiones son correctas!")
                    else:
                        print("Hay errores en las conexiones.")

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
                                dibujar_nodos(matrix, node_positions, connections)
                                conectar_nodos(connections)
                                button_rect = dibujar_boton()
                        break

        pygame.display.update()

# Ejecutar juego
main()