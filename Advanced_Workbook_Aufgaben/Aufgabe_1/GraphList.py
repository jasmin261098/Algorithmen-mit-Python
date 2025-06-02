class GraphList:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = {i: [] for i in range(size)}

    def add_connection(self, a, b):
        self.adjacency_list[a].append(b)
        self.adjacency_list[b].append(a)
    
    def remove_connection(self, a, b):
        if a in self.adjacency_list[b]:
            self.adjacency_list[b].remove(a)
        if b in self.adjacency_list[a]:
            self.adjacency_list[a].remove(b)
    
    def has_path(self, start, end):
        visited = set()
        return self._depth_first_search(start, end, visited)
    
    def _depth_first_search(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        for neighbor in self.adjacency_list[current]:
            if neighbor not in visited:
                if self._depth_first_search(neighbor, target, visited):
                    return True
        return False
    
#Test
if __name__ == "__main__":
    g = GraphList(5)
    g.add_connection(0, 1)
    g.add_connection(1, 2)
    print(g.has_path(0, 2)) #True
    print(g.has_path(0, 4)) #False