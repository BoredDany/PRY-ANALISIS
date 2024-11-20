class Node:
    def __init__(self, x: int, y: int, num: int):
        self.x = x
        self.y = y
        self.num = num
        self.conn = 0
        
    def add_conn(self):
        self.conn = self.conn + 1
        
    def __eq__(self, other):
        return isinstance(other, Node) and self.x == other.x and self.y == other.y and self.num == other.num
    
    def __lt__(self, other):
        return self.num < other.num
    
    def __hash__(self):
        return hash((self.x, self.y, self.num))  # Permite usar Node como clave en diccionarios o elementos de conjuntos

    def display(self):
        return f"Node(x={self.x}, y={self.y}, num={self.num})"