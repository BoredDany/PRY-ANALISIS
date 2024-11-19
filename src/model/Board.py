import pygame
from model.Node import Node
class Board:
    def __init__(self):
        self.node_positions = []
        self.time = 0
        self.node_radius = 20
        self.line_color = (0, 0, 0)  # Negro
        self.node_color = (255, 0, 0)  # Rojo
        self.selected_color = (0, 255, 0)  # Verde
        self.background_color = (255, 255, 255)  # Blanco
        self.screen_width = 600
        self.screen_height = 680
        self.margin = 50
        
    def draw_nodes(self, screen, matrix):
        for y, row in enumerate(matrix):  # Recorre por filas
            for x, value in enumerate(row):  # Recorre cada columna en la fila
                if value > 0:
                    # Usa (fila, columna) como clave para obtener la posición del nodo
                    pygame.draw.circle(screen, (0, 0, 0), self.node_positions[(y, x)], self.node_radius)
                    
                    # Mostrar el número del nodo en el centro
                    font = pygame.font.Font(None, 32)
                    text = font.render(str(value), True, (255, 255, 255))
                    screen.blit(text, (self.node_positions[(y, x)][0] - 10, self.node_positions[(y, x)][1] - 10))


                
    def draw_connections(self, screen, connections):
        radius = self.node_radius
        for node1, node2 in connections:
            if connections.count((node1, node2)) + connections.count((node2, node1)) == 2:
                if node1.x == node2.x:  # Conexión vertical
                    offset = 5
                    if node1.y < node2.y:
                        pygame.draw.line(screen, (255, 0, 0), (node1.x - offset, node1.y + radius), (node2.x - offset, node2.y - radius), 5)
                        pygame.draw.line(screen, (255, 0, 0), (node1.x + offset, node1.y + radius), (node2.x + offset, node2.y - radius), 5)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (node2.x - offset, node2.y + radius), (node1.x - offset, node1.y - radius), 5)
                        pygame.draw.line(screen, (255, 0, 0), (node2.x + offset, node2.y + radius), (node1.x + offset, node1.y - radius), 5)
                elif node1.y == node2.y:  # Conexión horizontal
                    offset = 5
                    if node1.x < node2.x:
                        pygame.draw.line(screen, (255, 0, 0), (node1.x + radius, node1.y - offset), (node2.x - radius, node2.y - offset), 5)
                        pygame.draw.line(screen, (255, 0, 0), (node1.x + radius, node1.y + offset), (node2.x - radius, node2.y + offset), 5)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (node2.x + radius, node2.y - offset), (node1.x - radius, node1.y - offset), 5)
                        pygame.draw.line(screen, (255, 0, 0), (node2.x + radius, node2.y + offset), (node1.x - radius, node1.y + offset), 5)
            else:
                if node1.x == node2.x:  # Conexión vertical
                    if node1.y < node2.y:
                        pygame.draw.line(screen, (255, 0, 0), (node1.x, node1.y + radius), (node2.x, node2.y - radius), 5)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (node2.x, node2.y + radius), (node1.x, node1.y - radius), 5)
                elif node1.y == node2.y:  # Conexión horizontal
                    if node1.x < node2.x:
                        pygame.draw.line(screen, (255, 0, 0), (node1.x + radius, node1.y), (node2.x - radius, node2.y), 5)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (node2.x + radius, node2.y), (node1.x - radius, node1.y), 5)
                    
                    
    def generar_posiciones(self, tam_x, tam_y, matrix):
        node_positions = {}
        x_spacing = 600 // tam_x
        y_spacing = (650 - 50) // tam_y

        for y, row in enumerate(matrix):  # Recorre por filas (y representa la fila)
            for x, value in enumerate(row):  # Recorre cada columna en la fila
                if value > 0:
                    # La clave ahora es (fila, columna)
                    node_positions[(y, x)] = (x * x_spacing + x_spacing // 2, y * y_spacing + y_spacing // 2)

        return node_positions

    def connect_nodes(self, screen, node1, node2):
        if node1 in self.node_positions and node2 in self.node_positions:
            pygame.draw.line(screen, self.line_color,
                             self.node_positions[node1],
                             self.node_positions[node2], 2)

    def get_node(self, mouse_pos, matrix):
        for node, position in self.node_positions.items():
            distance = ((mouse_pos[0] - position[0]) ** 2 + (mouse_pos[1] - position[1]) ** 2) ** 0.5
            if distance < 20:  # Si está dentro del nodo
                i, j = node
                return Node(i, j, matrix[i][j])
        return None
    
    
    def display_board(self):
        self.game.display()