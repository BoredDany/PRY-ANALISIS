import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla y colores
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conectar Nodos")

# Leer archivo y generar nodos
def leer_archivo(filename):
    with open(filename, 'r') as file:
        dimensions = list(map(int, file.readline().split(',')))
        matrix = [list(map(int, line.strip())) for line in file]
    return dimensions, matrix

# Función para dibujar nodos
def dibujar_nodos(matrix, node_positions):
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
    y_spacing = HEIGHT // dimensions[1]

    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:
                node_positions[(x, y)] = (x * x_spacing + x_spacing // 2, y * y_spacing + y_spacing // 2)

    return node_positions

# Función para conectar nodos
def conectar_nodos(connections):
    for node1, node2 in connections:
        pygame.draw.line(screen, RED, node1, node2, 5)

def main():
    # Cargar datos desde archivo
    dimensions, matrix = leer_archivo("nodos.txt")
    node_positions = generar_posiciones(dimensions, matrix)

    # Lista de conexiones
    connections = []
    selected_node = None

    while True:
        screen.fill(WHITE)

        # Dibujar nodos
        dibujar_nodos(matrix, node_positions)

        # Dibujar conexiones
        conectar_nodos(connections)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Determinar si se ha hecho clic en algún nodo
                for node, position in node_positions.items():
                    distance = ((mouse_pos[0] - position[0]) ** 2 + (mouse_pos[1] - position[1]) ** 2) ** 0.5
                    if distance < 20:  # Si está dentro del nodo
                        if selected_node is None:
                            selected_node = position
                        else:
                            # Añadir o remover conexión
                            if (selected_node, position) in connections or (position, selected_node) in connections:
                                connections.remove((selected_node, position))
                            else:
                                connections.append((selected_node, position))
                            selected_node = None
                        break

        pygame.display.update()

# Ejecutar juego
main()
