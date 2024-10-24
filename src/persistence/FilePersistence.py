from model.Node import Node

class FilePersistence:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        
        # Parse dimensions
        dimensions = list(map(int, lines[0].strip().split(',')))
        x, y = dimensions[0], dimensions[1]

        # Initialize matrix
        matrix = [[0 for _ in range(y)] for _ in range(x)]

        # Initialize list of nodes
        nodes = []

        # Parse matrix and nodes
        for i in range(1, len(lines)):
            row = list(map(int, lines[i].strip()))
            for j in range(len(row)):
                matrix[i-1][j] = row[j]  # Use i-1 to correctly index the matrix
                if row[j] > 0:
                    nodes.append(Node(i-1, j, row[j]))  # Use i-1 to correctly index the nodes
        
        return matrix, nodes
