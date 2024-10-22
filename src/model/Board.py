class Board:
    def __init__(self, x, y, matrix, vertices):
        self.x = x
        self.y = y
        self.matrix = matrix
        self.vertices = vertices
        self.edges = []
        
    def add_edge(self, node1, node2):
        self.edges.append([node1, node2])
        
    def display(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)
        print("\nVertices:")
        for vertex in self.vertices:
            print(vertex.value)
        print("\nEdges:")
        for edge in self.edges:
            print(f"{edge[0].value} - {edge[1].value}")