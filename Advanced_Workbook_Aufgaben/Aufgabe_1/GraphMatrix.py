class GraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]
    
    def add_connection(self, a, b):
        self.matrix[a][b] = 1
        self.matrix[b][a] = 1
    
    def remove_connection(self, a, b):
        self.matrix[a][b] = 0
        self.matrix[b][a] = 0
    
    def has_path(self, start, end):
        visited = set()
        return self._depth_first_search(start, end, visited)
    
    def _depth_first_search(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        for i, is_connected in enumerate(self.matrix[current]):
            if is_connected and i not in visited:
                if self._depth_first_search(i, target, visited):
                    return True
                return False

#Test
if __name__ == "__main__":
    g = GraphMatrix(5)
    g.add_connection(0, 1)
    g.add_connection(1, 2)
    print(g.has_path(0, 2)) #True
    print(g.has_path(0, 4)) #False