class Vertex:
    def __init__(self, children: list, initial: bool|None=None, index: int|None=None):
        self.children = children
        self.color = "W"
        self.d = 0
        self.f = 0
        self.initial = initial

    def __repr__(self):
        return (f"Children: {self.children}\n"
                f"Color: {self.color}\n"
                f"Discovery: {self.d}\n"
                f"Finish: {self.f}")
    
    def copy(self):
        vertex = Vertex([])
        vertex.children = self.children.copy()
        vertex.color = self.color
        vertex.d = self.d
        vertex.f = self.f
        vertex.initial = self.initial
        return vertex