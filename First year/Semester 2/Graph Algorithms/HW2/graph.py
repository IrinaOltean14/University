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
        self._neighbours = {}
        self._costs = {}
        for index in range(nb_of_vertices):
            self._neighbours[index] = []

    def get_cost(self, vertex1, vertex2):
        return self._costs[(vertex1, vertex2)]

    def check_if_vertex_in_graph(self, vertex):
        if vertex not in self._neighbours.keys():
            return False
        return True

    def remove_vertex(self, vertex):
        if not self.check_if_vertex_in_graph(vertex):
            raise GraphException("Vertex not in graph")
        self._nb_of_vertices -= 1
        self._neighbours.pop(vertex)
        for vertex1 in self._neighbours.keys():
            if vertex in self._neighbours[vertex1]:
                self._neighbours[vertex1].remove(vertex)
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
        self._neighbours[self._nb_of_vertices-1] = []

    def get_degree(self, vertex):
        if not self.check_if_vertex_in_graph(vertex):
            raise GraphException("Vertex is not in graph")
        return len(self._neighbours)

    def check_if_edge_already_in_graph(self, vertex1, vertex2):
        if vertex1 not in self._neighbours.keys():
            raise GraphException("One of the vertices is not in the graph")
        if vertex2 in self._neighbours[vertex1]:
            return True
        return False

    def add_edge(self, vertex1, vertex2, cost):
        if not self.check_if_vertex_in_graph(vertex1) or not self.check_if_vertex_in_graph(vertex2):
            raise GraphException("Vertex not in graph")
        if vertex2 in self._neighbours[vertex1]:
            raise GraphException("Edge already exists")
        self._nb_edges += 1
        self._neighbours[vertex1].append(vertex2)
        self._neighbours[vertex2].append(vertex1)
        self._costs[(vertex1, vertex2)] = cost
        self._costs[(vertex2, vertex1)] = cost

    def remove_edge(self, vertex1, vertex2):
        self._neighbours[vertex2].remove(vertex1)
        self._neighbours[vertex1].remove(vertex2)
        self._costs.pop((vertex1, vertex2))
        self._costs.pop((vertex2, vertex1))

    def print_graph(self):
        edges = []
        for vertex1 in self._neighbours.keys():
            for vertex2 in self._neighbours[vertex1]:
                if [vertex2, vertex1] not in edges:
                    edges.append([vertex1, vertex2])
                    yield [vertex1, vertex2, self._costs[(vertex1, vertex2)]]

    def get_number_of_vertices(self):
        return self._nb_of_vertices

    def get_number_of_edges(self):
        return self._nb_edges

    def parse_vertices(self):
        for vertex in self._neighbours.keys():
            yield vertex

    def parse_edges(self, vertex1):
        if not self.check_if_vertex_in_graph(vertex1):
            raise GraphException("Vertex is not in graph")
        edges = []
        for vertex2 in self._neighbours[vertex1]:
            if [vertex2, vertex1] not in edges:
                edges.append([vertex1, vertex2])
                yield vertex2

    def modify_cost(self, vertex1, vertex2, new_cost):
        if not self.check_if_vertex_in_graph(vertex1):
            raise GraphException("Vertex is not in graph")
        if not self.check_if_vertex_in_graph(vertex2):
            raise GraphException("Vertex is not in graph")
        if vertex2 not in self._neighbours[vertex1]:
            raise GraphException("Invalid edge")
        self._costs[(vertex1, vertex2)] = new_cost

    def breadth_first_traversal(self, start_vertex, visited):
        queue = [start_vertex]
        visited.append(start_vertex)
        connected_component = [start_vertex]
        prev = {}
        dist = {}
        prev[start_vertex] = -1
        dist[start_vertex] = 0
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            for neighbour in self._neighbours[current_vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    prev[neighbour] = current_vertex
                    dist[neighbour] = dist[current_vertex] + 1
                    connected_component.append(neighbour)
        return connected_component

    def find_connected_components(self):
        visited = []
        all_components = []
        for vertex in self._neighbours.keys():
            if vertex not in visited:
                connected_component = self.breadth_first_traversal(vertex, visited)
                all_components.append(connected_component)
        return all_components

    def depth_first_search(self, visited, current_node, levels, max_level, father, components):
        visited.append(current_node)
        for neighbour in self._neighbours[current_node]:
            if neighbour != father:
                if neighbour in visited:
                    if max_level[current_node]>levels[neighbour]:
                        max_level[current_node]=levels[neighbour]
                if neighbour not in visited:
                    levels[neighbour] = levels[current_node]+1
                    max_level[neighbour] = levels[neighbour]
                    self.depth_first_search(visited, neighbour, levels, max_level,current_node, components)
                    if max_level[current_node] > max_level[neighbour]:
                        max_level[current_node] = max_level[neighbour]

                    if levels[current_node] <= max_level[neighbour]:
                        print(components)
                        print(visited)
                        print(current_node, neighbour)
                        current_component = []
                        node = visited.pop()
                        while node != neighbour:
                            current_component.append(node)
                            node = visited.pop()
                        current_component.append(node)
                        current_component.append(current_node)
                        current_component.sort()
                        visited.remove(current_node)
                        print(visited)
                        if current_component not in components:
                            components.append(current_component)

    def find_biconnected_components(self):
        visited=[]
        levels = {}
        max_level={}
        components = []
        for vertex in self._neighbours.keys():
            levels[vertex] = 0
            max_level[vertex]=0
        for vertex in self._neighbours.keys():
            if vertex not in visited:
                self.depth_first_search(visited, vertex, levels, max_level,-1, components)
        for c in components:
            print(c)

    def hamiltonian(self, path, pos):
        #print(path, pos)
        if pos == len(self._neighbours.keys()):
            if path[pos-1] in self._neighbours[path[0]]:
                path[pos] = path[0]
                return path
            else:
                return None

        for vertex in self._neighbours[path[pos-1]]:
            if vertex not in path:
                path[pos] = vertex

                found = self.hamiltonian(path, pos+1)
                if found is not None:
                    return found

                path[pos] = None

        return None

