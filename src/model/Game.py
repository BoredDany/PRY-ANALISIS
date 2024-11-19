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
            
    def display(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)
        print("\nVertices:")
        vertex_nums = ', '.join(str(vertex.num) for vertex in self.vertices)
        print(vertex_nums)
        print("\nEdges:")
        for edge in self.edges:
            print(f"{edge[0].value} - {edge[1].value}")