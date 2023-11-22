from random import randint
from exceptions import GraphException
from graph import Graph, read_graph_from_file, write_graph_to_file
from copy import deepcopy
import os


class UI:
    def __init__(self, graph):
        self._graph = graph
        self._copies = []

    @staticmethod
    def print_menu():
        print("\nCHOOSE YOUR OPTION\n"
              "1. Generate random graph\n"
              "2. Get number of vertices\n"
              "3. Parse (iterate) the set of vertices\n"
              "4. Check if edge belongs to the graph\n"
              "5. Get the in degree and out degree\n"
              "6. Parse the set ofedges of a vertex\n"
              "7. Modify the cost of an edge\n"
              "8. Remove edge\n"
              "9. Add edge\n"
              "10. Add vertex\n"
              "11. Remove vertex\n"
              "12. Make copy of the graph\n"
              "13. Update graph with the last copy made\n"
              "14. Read graph from file\n"
              "15. Write graph to file\n"
              "16. Print graph\n"
              "17. Find the connected components of an undirected graph using BFS\n"
              "18. Find biconnected components\n"
              "19. Check for hamiltonian cycle\n"
              "20. Exit")

    def start_app(self):
        while True:
            self.print_menu()
            option = input("Enter your option: ")
            if option == "1":
                self.generate_random_graph_ui()
            elif option == "2":
                print("The number of vertices is: " + str(self._graph.get_number_of_vertices()))
            elif option == "3":
                self.parse_vertices_ui()
            elif option == "4":
                self.check_if_edge_ui()
            elif option == "5":
                self.get_the_in_degree_and_out_degree_ui()
            elif option == "6":
                self.parse_the_edges_ui()
            elif option == "7":
                self.modify_cost()
            elif option == "8":
                self.remove_edge()
            elif option == "9":
                self.add_edge_ui()
            elif option == "10":
                self.add_vertex_ui()
            elif option == "11":
                self.remove_vertex()
            elif option == "12":
                self.make_copy()
            elif option == "13":
                self.update_graph_with_copy()
            elif option == "14":
                self.read_graph_from_file()
            elif option == "15":
                self.write_graph_to_file()
            elif option == "16":
                self.print_graph()
            elif option == "17":
                self.find_connected_components()
            elif option == "18":
                self.find_biconnected_components()
            elif option == "19":
                self.find_hamiltonian_cycle()
            elif option == "20":
                print("End of program")
                break
            else:
                print("Invalid command\n")

    def find_hamiltonian_cycle(self):
        in_path = [0]
        for vertex in range(self._graph.get_number_of_edges()):
            in_path.append(None)
        found = self._graph.hamiltonian(in_path,1)
        if found is not None:
            print("There is a Hamiltonian cycle")
            print(found)
        else:
            print("There is no Hamiltonian cycle")


    def find_biconnected_components(self):
        self._graph.find_biconnected_components()

    def find_connected_components(self):
        all_components = self._graph.find_connected_components()
        number_of_connected_components = 0
        for component in all_components:
            number_of_connected_components += 1
            print("The connected component with number " + str(number_of_connected_components) + " is: ")
            print(component)

    def write_graph_to_file(self):
        file = input("Please enter the file name: ")
        write_graph_to_file(file, self._graph)

    def read_graph_from_file(self):
        file = input("Please enter the file name: ")
        if os.path.isfile(file):
            print("Graph read successfully")
            self._graph = read_graph_from_file(file)
        else:
            print("The file does not exist")

    def update_graph_with_copy(self):
        if len(self._copies) == 0:
            print("There are no copies available")
        else:
            self._graph = self._copies[len(self._copies)-1]
            self._copies.remove(self._copies[len(self._copies)-1])
            print("Graph updated successfully")

    def make_copy(self):
        self._copies.append(deepcopy(self._graph))
        print("Copy made successfully")

    def print_graph(self):
        print(f"{self._graph.get_number_of_vertices()} vertices - {self._graph.get_number_of_edges()} edges")
        for [vertex1, vertex2, cost] in self._graph.print_graph():
            print(str(vertex1) + " " + str(vertex2) + " " + str(cost))

    def remove_vertex(self):
        try:
            vertex = int(input("Enter the vertex: "))
            self._graph.remove_vertex(vertex)
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def add_vertex_ui(self):
        self._graph.add_vertex()
        print("Vertex added successfully")

    def modify_cost(self):
        try:
            vertex1 = int(input("Enter the first vertex: "))
            vertex2 = int(input("Enter the second vertex: "))
            cost = int(input("Enter the new cost: "))
            self._graph.modify_cost(vertex1, vertex2, cost)
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def get_the_in_degree_and_out_degree_ui(self):
        try:
            vertex = int(input("Enter the vertex: "))
            degree = self._graph.get_degree(vertex)
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def check_if_edge_ui(self):
        try:
            vertex1 = int(input("Enter the first vertex: "))
            vertex2 = int(input("Enter the second vertex: "))
            if self._graph.check_if_edge_already_in_graph(vertex1, vertex2):
                print("The edge is in the graph")
            else:
                print("The edge is not in the graph")
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def remove_edge(self):
        try:
            vertex1 = int(input("Enter the first vertex: "))
            vertex2 = int(input("Enter the second vertex: "))
            if not self._graph.check_if_edge_already_in_graph(vertex1, vertex2):
                print("The edge is not in the graph")
            self._graph.remove_edge(vertex1, vertex2)
            print("Edge removed successfully")
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def add_edge_ui(self):
        try:
            vertex1 = int(input("Enter the first vertex: "))
            vertex2 = int(input("Enter the second vertex: "))
            cost = int(input("Enter the cost: "))
            self._graph.add_edge(vertex1, vertex2, cost)
            print("Edge added successfully")
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def parse_vertices_ui(self):
        for vertex in self._graph.parse_vertices():
            print(vertex)

    def parse_the_edges_ui(self):
        try:
            vertex = int(input("Enter the vertex: "))
            for vertex2 in self._graph.parse_edges(vertex):
                print(str(vertex) + " " + str(vertex2))
        except ValueError:
            print("Invalid input")
        except GraphException as error:
            print(error)

    def generate_random_graph_ui(self):
        try:
            vertices = int(input("Enter the number of vertices: "))
            edges = int(input("Enter the number of edges: "))
            self._graph = random_graph(vertices, edges)
            print("Random graph generated successfully")
            self.print_graph()
        except ValueError:
            print("Invalid input\n")
        except GraphException as error:
            print(error)


def random_graph(vertices, edges):
    if edges > vertices*(vertices-1)/2:
        raise GraphException("Invalid number of vertices and edges\n")
    graph = Graph(vertices)
    while edges > 0:
        try:
            graph.add_edge(randint(0, vertices-1), randint(0, vertices-1), randint(1,100))
            print(edges)
            edges -= 1
        except GraphException:
            pass
    return graph

