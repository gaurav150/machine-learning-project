class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self,vertex1,vertex2):
            if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
                try:
                    self.adjacency_list[vertex1].remove(vertex2)
                    self.adjacency_list[vertex2].remove(vertex1)
                except ValueError:
                    pass

                return True
            return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list:
            for key in self.adjacency_list:
                if vertex in self.adjacency_list[key]:
                    self.adjacency_list[key].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
        