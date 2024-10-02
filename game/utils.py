import pygame

radio = 20

# Función para dibujar nodos
def dibujar_nodos(screen, matrix, node_positions, conexiones):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:
                pygame.draw.circle(screen, (0, 0, 0), node_positions[(x, y)], radio)
                # Mostrar el número del nodo
                font = pygame.font.Font(None, 32)
                text = font.render(str(value), True, (255, 255, 255))
                screen.blit(text, (node_positions[(x, y)][0] - 10, node_positions[(x, y)][1] - 10))

# Función para conectar nodos
def conectar_nodos(screen, connections):
    radius = radio  # Radio del círculo del nodo
    for node1, node2 in connections:
        if connections.count((node1, node2)) + connections.count((node2, node1)) == 2:
            if node1[0] == node2[0]:  # Conexión vertical
                offset = 5
                if node1[1] < node2[1]:
                    pygame.draw.line(screen, (255, 0, 0), (node1[0] - offset, node1[1] + radius), (node2[0] - offset, node2[1] - radius), 5)
                    pygame.draw.line(screen, (255, 0, 0), (node1[0] + offset, node1[1] + radius), (node2[0] + offset, node2[1] - radius), 5)
                else:
                    pygame.draw.line(screen, (255, 0, 0), (node2[0] - offset, node2[1] + radius), (node1[0] - offset, node1[1] - radius), 5)
                    pygame.draw.line(screen, (255, 0, 0), (node2[0] + offset, node2[1] + radius), (node1[0] + offset, node1[1] - radius), 5)
            elif node1[1] == node2[1]:  # Conexión horizontal
                offset = 5
                if node1[0] < node2[0]:
                    pygame.draw.line(screen, (255, 0, 0), (node1[0] + radius, node1[1] - offset), (node2[0] - radius, node2[1] - offset), 5)
                    pygame.draw.line(screen, (255, 0, 0), (node1[0] + radius, node1[1] + offset), (node2[0] - radius, node2[1] + offset), 5)
                else:
                    pygame.draw.line(screen, (255, 0, 0), (node2[0] + radius, node2[1] - offset), (node1[0] - radius, node1[1] - offset), 5)
                    pygame.draw.line(screen, (255, 0, 0), (node2[0] + radius, node2[1] + offset), (node1[0] - radius, node1[1] + offset), 5)
        else:
            if node1[0] == node2[0]:  # Conexión vertical
                if node1[1] < node2[1]:
                    pygame.draw.line(screen, (255, 0, 0), (node1[0], node1[1] + radius), (node2[0], node2[1] - radius), 5)
                else:
                    pygame.draw.line(screen, (255, 0, 0), (node2[0], node2[1] + radius), (node1[0], node1[1] - radius), 5)
            elif node1[1] == node2[1]:  # Conexión horizontal
                if node1[0] < node2[0]:
                    pygame.draw.line(screen, (255, 0, 0), (node1[0] + radius, node1[1]), (node2[0] - radius, node2[1]), 5)
                else:
                    pygame.draw.line(screen, (255, 0, 0), (node2[0] + radius, node2[1]), (node1[0] - radius, node1[1]), 5)
                    

# Contar conexiones de un nodo
def contar_conexiones(nodo, conexiones):
    return sum(1 for conexion in conexiones if nodo in conexion)


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


# Verificar si una conexión es válida (horizontal o vertical y no es con el mismo nodo)
def es_conexion_valida(node1, node2):
    return (node1[0] == node2[0] or node1[1] == node2[1]) and node1 != node2


def verificar_conexiones(matrix, node_positions, conexiones):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:  # Solo nodos con valor > 0
                nodo_pos = node_positions[(x, y)]
                conexiones_actuales = contar_conexiones(nodo_pos, conexiones)
                if conexiones_actuales != value:
                    return False
    return True


def leer_archivo(filename):
    with open(filename, 'r') as file:
        dimensions = list(map(int, file.readline().split(',')))
        matrix = [list(map(int, line.strip())) for line in file]
    return dimensions, matrix


def generar_posiciones(dimensions, matrix):
    node_positions = {}
    x_spacing = 600 // dimensions[0]
    y_spacing = (650 - 50) // dimensions[1]  # Ajustar para incluir el botón

    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value > 0:
                node_positions[(x, y)] = (x * x_spacing + x_spacing // 2, y * y_spacing + y_spacing // 2)

    return node_positions

