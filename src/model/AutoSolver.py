from heapq import heappush, heappop

class AutoSolver:
    def __init__(self, game):
        self.game = game
        self.solutions = []
    
    
    def solve(self):
        game = self.game

        # Obtener todos los nodos organizados de mayor a menor por conexiones faltantes
        nodes_to_connect = sorted(game.vertices, key=lambda node: node.num - game.count_connections(node), reverse=True)

        while nodes_to_connect:
            # Iterar sobre la lista buscando el nodo con conexiones faltantes igual a vecinos disponibles
            for node in nodes_to_connect:
                connections_needed = node.num - game.count_connections(node)
                print("NODO: ", node.display())
                valid_neighbors = self.get_valid_neighbors(node)
                print("VECINOS")
                for v in valid_neighbors:
                    print("VECI: ", node.display())

                # Si el número de conexiones faltantes coincide con los vecinos disponibles
                if connections_needed == len(valid_neighbors) * 2:
                    # Hacer conexiones dobles con cada vecino válido
                    for neighbor in valid_neighbors:
                        game.add_edge(node, neighbor)  # Conexión en un sentido
                        game.add_edge(neighbor, node)  # Conexión en el otro sentido

                    # Eliminar el nodo resuelto de la lista
                    nodes_to_connect.remove(node)

                    # Actualizar la lista y las conexiones
                    nodes_to_connect = sorted(
                        nodes_to_connect, key=lambda n: n.num - game.count_connections(n), reverse=True
                    )
                    break
                elif connections_needed == len(valid_neighbors):
                    # Hacer conexiones simples con cada vecino válido
                    for neighbor in valid_neighbors:
                        game.add_edge(node, neighbor)

                    # Eliminar el nodo resuelto de la lista
                    nodes_to_connect.remove(node)

                    # Actualizar la lista y las conexiones
                    nodes_to_connect = sorted(
                        nodes_to_connect, key=lambda n: n.num - game.count_connections(n), reverse=True
                    )
                    break
            else:
                # Si no se puede resolver ningún nodo, salir del bucle
                print("No se encontraron más soluciones posibles.")
                break

        # Verificar si el juego está resuelto
        if game.won():
            print("¡Solución encontrada!")
            game.display()
        else:
            print("No se encontró solución.")

    def get_valid_neighbors(self, node):
        """
        Retorna una lista de vecinos válidos para un nodo dado.
        Un vecino válido es aquel que no viola las restricciones de conexión.
        """
        valid_neighbors = []
        for neighbor in self.game.vertices:
            if neighbor != node and self.game.valid_connection(node, neighbor, self.game.edges) and self.game.count_connections(node) < node.num:
                valid_neighbors.append(neighbor)
        return valid_neighbors


    
    
    def generate_valid_connections(self):
        valid_connections = []
        for node1 in self.game.vertices:
            for node2 in self.game.vertices:
                # Verificar que node1 y node2 sean nodos diferentes
                if node1 != node2:
                    # Verificar si la conexión entre node1 y node2 es válida
                    if self.game.valid_connection(node1, node2, self.game.edges):
                        valid_connections.append((node1, node2))  # Conexión de node1 a node2
        return valid_connections