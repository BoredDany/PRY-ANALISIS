class Node:
    def __init__(self, x: int, y: int, num: int):
        self.x = x
        self.y = y
        self.num = num
        
    def __eq__(self, other):
        return isinstance(other, Node) and self.x == other.x and self.y == other.y and self.num == other.num

    def display(self):
        return f"Node(x={self.x}, y={self.y}, num={self.num})"