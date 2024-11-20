from heapq import heappush, heappop

class AutoSolver:
    def __init__(self, game):
        self.game = game
        self.solutions = []
    
    
    def solve(self):
        game = self.game

        # Obtener todos los nodos organizados de mayor a menor por conexiones faltantes
        nodes_to_connect = sorted(game.vertices, key=lambda node: node.num - game.count_connections(node), reverse=True)
        possible_edges = self.generate_valid_connections()

        while nodes_to_connect:
            # Iterar sobre la lista buscando el nodo con conexiones faltantes igual a vecinos disponibles
            for node in nodes_to_connect:
                connections_needed = node.num - game.count_connections(node)
                valid_neighbors = self.get_node_valid_connections(node, possible_edges)
                
                print("NODE:", node.display())
                print("NEED:", connections_needed)
                print("NEGHSSS:", len(valid_neighbors))
                for a, b in valid_neighbors:
                    print(a.display(), b.display())
                
                # Si el número de conexiones faltantes coincide con los vecinos disponibles
                if connections_needed == len(valid_neighbors) or connections_needed == len(valid_neighbors)/2:
                    
                    if connections_needed == len(valid_neighbors)/2:
                        valid_neighbors = self.get_unique_connections(valid_neighbors)
                    
                    # Hacer conexiones con cada vecino válido
                    for n1, n2 in valid_neighbors:
                        game.add_edge(n1, n2)

                        # Actualizar las conexiones posibles eliminando las usadas
                        possible_edges = [
                            (e1, e2) for e1, e2 in possible_edges
                            if not ((e1 == n1 and e2 == n2) or (e1 == n2 and e2 == n1))
                        ]

                    # Eliminar el nodo resuelto de la lista
                    nodes_to_connect.remove(node)

                    # No es necesario reordenar la lista completa; se asume que el nodo procesado ya no afecta el orden
                    break
            else:
                # Si ningún nodo puede resolverse, terminar el bucle
                print("No se encontraron más soluciones posibles.")
                break

        # Verificar si el juego está resuelto
        if game.won():
            print("¡Solución encontrada!")
            game.display()
        else:
            print("No se encontró solución.")



    def get_unique_connections(self, valid_neighbors):
        unique_connections = set()

        for node1, node2 in valid_neighbors:
            # Ordenar cada par de nodos para asegurar que no importe el orden
            connection = tuple(sorted([node1, node2], key=lambda node: (node.x, node.y)))
            unique_connections.add(connection)  # Usar un set para eliminar duplicados

        # Convertir de nuevo el set a una lista
        return [tuple(connection) for connection in unique_connections]

        
    
    def get_neighbors_count(self, node, possible_edges):
        neighbors = set()
        for n1, n2 in possible_edges:
            if n1 == node:
                neighbors.add(n2)
            elif n2 == node:
                neighbors.add(n1)
        return len(neighbors)
        
    def get_node_valid_connections(self, node, edges):
        # Retorna las conexiones validas
        valid_neighbors = []
        for node1, node2 in edges:
            if node1 == node and self.game.count_connections(node2) < node2.num and self.game.valid_connection(node1, node2, self.game.edges):
                valid_neighbors.append((node1, node2))
            elif node2 == node and self.game.count_connections(node1) < node1.num and self.game.valid_connection(node1, node2, self.game.edges):
                valid_neighbors.append((node1, node2))
        return valid_neighbors

    def generate_valid_connections(self):
        # Genera todas las conexiones posibles inicialmente
        valid_connections = []
        for node1 in self.game.vertices:
            for node2 in self.game.vertices:
                # Verificar que node1 y node2 sean nodos diferentes
                if node1 != node2:
                    # Verificar si la conexión entre node1 y node2 es válida
                    if self.game.valid_connection(node1, node2, self.game.edges):
                        valid_connections.append((node1, node2))  # Conexión de node1 a node2
        return valid_connections
