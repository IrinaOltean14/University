from collections import deque, defaultdict

from exceptions import GraphException

def read_graph_from_file(file_path):
    with open(file_path, "r") as file:
        line = file.readline()
        vertices, edges = line.split()
        graph = Graph(int(vertices))
        for line in range(int(edges)):
            vertex1, vertex2, cost = file.readline().split()
            graph.add_edge(int(vertex1), int(vertex2), int(cost))
    file.close()
    return graph

def write_graph_to_file(file_path, graph):
    with open(file_path, "w") as file:
        file.write(f"{graph.get_number_of_vertices()} {graph.get_number_of_edges()}\n")
        for vertex1 in graph.parse_vertices():
            for vertex2 in graph.parse_the_outbound_edges(vertex1):
                file.write(f"{vertex1} {vertex2} {graph.get_cost(vertex1, vertex2)}\n")
    file.close()

class Graph:
    def __init__(self, nb_of_vertices):
        self._nb_of_vertices = nb_of_vertices
        self._nb_edges = 0
        self._out_neighbours = {}
        self._in_neighbours = {}
        self._costs = {}
        for index in range(nb_of_vertices):
            self._out_neighbours[index] = []
            self._in_neighbours[index] = []

    def get_cost(self, vertex1, vertex2):
        return self._costs[(vertex1, vertex2)]

    def check_if_vertex_in_graph(self, vertex):
        if vertex not in self._out_neighbours.keys():
            return False
        return True

    def remove_vertex(self, vertex):
        self._nb_of_vertices-=1
        if not self.check_if_vertex_in_graph(vertex):
            raise GraphException("Vertex not in graph")
        self._out_neighbours.pop(vertex)
        self._in_neighbours.pop(vertex)
        for vertex1 in self._out_neighbours.keys():
            if vertex in self._out_neighbours[vertex1]:
                self._out_neighbours[vertex1].remove(vertex)
            if vertex in self._in_neighbours[vertex1]:
                self._in_neighbours[vertex1].remove(vertex)
        ok = 1
        while ok:
            ok = 0
            for (v1, v2) in self._costs.keys():
                if v1 == vertex or v2 == vertex:
                    self._costs.pop((v1,v2))
                    ok = 1
                    break

    def add_vertex(self):
        self._nb_of_vertices+=1
        self._out_neighbours[self._nb_of_vertices-1] = []
        self._in_neighbours[self._nb_of_vertices-1] = []

    def get_the_in_degree_and_out_degree(self, vertex):
        if not self.check_if_vertex_in_graph(vertex):
            raise GraphException("Vertex is not in graph")
        return [len(self._in_neighbours[vertex]), len(self._out_neighbours[vertex])]

    def check_if_edge_already_in_graph(self, vertex1, vertex2):
        if vertex1 not in self._out_neighbours.keys() or vertex2 not in self._out_neighbours.keys():
            raise GraphException("One of the vertices is not in the graph")
        if vertex2 in self._out_neighbours[vertex1]:
            return True
        return False

    def add_edge(self, vertice1, vertice2, cost):
        if not self.check_if_vertex_in_graph(vertice1) or not self.check_if_vertex_in_graph(vertice2):
            raise GraphException("Vertex not in graph")
        self._nb_edges+=1
        self._out_neighbours[vertice1].append(vertice2)
        self._in_neighbours[vertice2].append(vertice1)
        self._costs[(vertice1, vertice2)] = cost

    def remove_edge(self, vertex1, vertex2):
        self._out_neighbours[vertex1].remove(vertex2)
        self._in_neighbours[vertex2].remove(vertex1)
        self._costs.pop((vertex1, vertex2))

    def print_graph(self):
        for vertice1 in self._out_neighbours.keys():
            for vertice2 in self._out_neighbours[vertice1]:
                yield [vertice1, vertice2, self._costs[(vertice1, vertice2)]]

    def get_number_of_vertices(self):
        return self._nb_of_vertices

    def get_number_of_edges(self):
        return self._nb_edges

    def parse_vertices(self):
        for vertex in self._out_neighbours.keys():
            yield vertex

    def parse_the_outbound_edges(self, vertex1):
        if not self.check_if_vertex_in_graph(vertex1):
            raise GraphException("Vertex is not in graph")
        for vertex2 in self._out_neighbours[vertex1]:
            yield vertex2

    def parse_the_inbound_edges(self, vertex1):
        if not self.check_if_vertex_in_graph(vertex1):
            raise GraphException("Vertex is not in graph")
        for vertex2 in self._in_neighbours[vertex1]:
            yield vertex2

    def modify_cost(self, vertex1, vertex2, new_cost):
        if not self.check_if_vertex_in_graph(vertex1):
            raise GraphException("Vertex is not in graph")
        if not self.check_if_vertex_in_graph(vertex2):
            raise GraphException("Vertex is not in graph")
        if vertex2 not in self._out_neighbours[vertex1]:
            raise GraphException("Invalid edge")
        self._costs[(vertex1, vertex2)] = new_cost

    def BFS(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while len(queue)!=0:
            current_vertex = queue.pop(0)
            for neighbour in self._out_neighbours[current_vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def BFS_transversal_graph(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while len(queue)!=0:
            current_vertex = queue.pop(0)
            for neighbour in self._out_neighbours.keys():
                if current_vertex in self._out_neighbours[neighbour] and neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def find_strongly_connected_components(self):
        visited = []
        strongly_components = []
        for vertex in self._out_neighbours.keys():
            if vertex not in visited:
                current_component = [vertex]
                visited.append(vertex)
                visited_BFS = self.BFS(vertex)
                visited_BFS_transversal = self.BFS_transversal_graph(vertex)
                for vertex1 in self._out_neighbours.keys():
                    if vertex1 != vertex and vertex1 in visited_BFS and vertex1 in visited_BFS_transversal:
                        visited.append(vertex1)
                        current_component.append(vertex1)
                strongly_components.append(current_component)
        return strongly_components

    def efficient_topological_sort_predecessor_counting(self):
        sorted_vertices = []
        queue = deque()
        count = defaultdict(int)

        # Calculate in-degrees for each vertex
        for vertex in self._in_neighbours.keys():
            count[vertex] = len(self._in_neighbours[vertex])
            if count[vertex] == 0:
                queue.append(vertex)

        while queue:
            element = queue.popleft()
            sorted_vertices.append(element)
            for vertex in self._out_neighbours[element]:
                count[vertex] -= 1
                if count[vertex] == 0:
                    queue.append(vertex)

        if len(sorted_vertices) != self._nb_of_vertices:
            return []

        return sorted_vertices

    def topological_sort_predecessor_counting(self):
        sorted_vertices = []
        queue = []
        count = []
        for vertex in self._in_neighbours.keys():
            count.append(len(self._in_neighbours[vertex]))
            if len(self._in_neighbours[vertex]) == 0:
                queue.append(vertex)
        #print(queue)
        #print(count)

        while len(queue) != 0:
            element = queue.pop(0)
            sorted_vertices.append(element)
            for vertex in self._out_neighbours[element]:
                #print("Iteration: ")
                #print(element, vertex)
                count[vertex] = count[vertex] - 1
                if count[vertex] == 0:
                    queue.append(vertex)
                #print(queue)
                #print(count)
                #print(sorted_vertices)

        if len(sorted_vertices) != self._nb_of_vertices:
            return []

        return sorted_vertices

    def find_highest_cost_path(self, source, destination):
        sorted_vertices = self.topological_sort_predecessor_counting()
        if len(sorted_vertices) == 0:
            return -1

        max_cost = [-999999999]*self._nb_of_vertices
        max_cost[source] = 0
        predecessor = []
        for vertex in self._out_neighbours.keys():
            predecessor.append((-1))

        for vertex in sorted_vertices:
            for neighbor in self._out_neighbours[vertex]:
                cost = self.get_cost(vertex, neighbor)
                if max_cost[vertex]+cost>max_cost[neighbor]:
                        #max_cost[neighbor] = max(max_cost[neighbor], max_cost[vertex]+cost)
                        max_cost[neighbor] = max_cost[vertex]+cost
                        predecessor[neighbor] = vertex

        path = [destination]
        current_vertex = destination
        while current_vertex != source:
            current_vertex = predecessor[current_vertex]
            path.append(current_vertex)

        return max_cost[destination], path
