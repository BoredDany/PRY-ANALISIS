class Node:
    def __init__(self, x: int, y: int, num: int):
        self.x = x
        self.y = y
        self.num = num

    def display(self):
        return f"Node(x={self.x}, y={self.y}, num={self.num})"