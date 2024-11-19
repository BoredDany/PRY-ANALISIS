class Game:
    def __init__(self, x, y, matrix, vertices):
        self.x = x
        self.y = y
        self.matrix = matrix
        self.vertices = vertices
        self.edges = []
        
    def add_edge(self, node1, node2):
        self.edges.append([node1, node2])
    
    def delete_edge(self, node1, node2):
        edge = [node1, node2]
        reverse_edge = [node2, node1]
        if edge in self.edges:
            self.edges.remove(edge)
        elif reverse_edge in self.edges:
            self.edges.remove(reverse_edge)
        else:
            print("Edge not found")
            
    def count_connections(self, node):
        count = 0
        for edge in self.edges:
            if node in edge: 
                count += 1
        return count
    
    def count_node_connections(self, node1, node2):
        count = 0
        for edge in self.edges:
            if node1 in edge and node2 in edge: 
                count += 1
        return count
    
    def island (self):
        visited = set()
        adjacency_list = {node: [] for node in self.vertices}

        # Construir lista de adyacencia 
        for edge in self.edges:
            node1, node2 = edge
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    stack.extend(neighbor for neighbor in adjacency_list[current] if neighbor not in visited)

        # Realizar DFS desde el primer nodo 
        dfs(self.vertices[0])

        # Verificar si hay nodos no visitados
        for node in self.vertices:
            if node not in visited:
                return True  # Hay islas
        return False  # No hay islas
    
    def valid_connection (self, node1, node2):
        if node1.num == 0 or node2.num == 0:
            return False
        
        if node1.__eq__(node2):
            return False
        
        if node1.x != node2.x and node1.y != node2.y:
            return False
        
        if self.count_node_connections(node1, node2) == 2:
            return False
        
        for edge in self.edges:
            n1, n2 = edge
            if self.do_edges_intersect(node1, node2, n1, n2):
                return False
        
        if self.connection_passes_over_node(node1, node2):
            return False
        
        return True
    
    def do_edges_intersect(self, n1, n2, m1, m2):
        # Asegurarse de que las aristas sean rectilíneas (horizontal o vertical)
        if n1.x == n2.x:  # Vertical
            if m1.y == m2.y:  # Horizontal
                # Verificar cruce entre las verticales y horizontales
                return (min(n1.y, n2.y) <= m1.y <= max(n1.y, n2.y) and
                        min(m1.x, m2.x) <= n1.x <= max(m1.x, m2.x))
        elif n1.y == n2.y:  # Horizontal
            if m1.x == m2.x:  # Vertical
                # Verificar cruce entre las horizontales y verticales
                return (min(n1.x, n2.x) <= m1.x <= max(n1.x, n2.x) and
                        min(m1.y, m2.y) <= n1.y <= max(m1.y, m2.y))
        return False
    
    
    def connection_passes_over_node(self, node1, node2):
        # Vertical: mantengo la columna
        if node1.y == node2.y:
            y = node1.y
            x1 = min(node1.x, node2.x) + 1
            x2 = max(node1.x, node2.x)
            for row in range(x1, x2):
                if self.matrix[row][y] != 0:  # Fila variable, columna fija
                    return True
                
        # Horizontal: mantengo la fila
        elif node1.x == node2.x:
            x = node1.x
            y1 = min(node1.y, node2.y) + 1
            y2 = max(node1.y, node2.y)
            for col in range(y1, y2):
                if self.matrix[x][col] != 0:  # Fila variable, columna fija
                    return True
                
        return False

    
    
    def won (self):
        for node in self.vertices:
            if node.num != count_connections(node):
                return False
            
        if self.island():
            return False
        
        return True
    
    
    def display(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)
        print("\nVertices:")
        vertex_nums = ', '.join(str(vertex.num) for vertex in self.vertices)
        print(vertex_nums)
        print("\nEdges:")
        for edge in self.edges:
            print(f"{edge[0].num} - {edge[1].num}")
            print("conexion: (", edge[0].x, ",", edge[0].y,"): ", edge[0].num, " con ", edge[1].x, ",", edge[1].y,"): ", edge[1].num)