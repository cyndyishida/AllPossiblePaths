import random
import copy

class Graph(object):
    class Edge(object):
        def __init__(self, source, destination, weight):
            """
            DO NOT EDIT!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: Vertex where this edge ends
            :param weight: Value associated with this edge
            """
            self.source = source
            self.destination = destination
            self.weight = weight
            self.explored = False

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

    class Path(object):
        def __init__(self, vertices=list(), weight=0):
            """
            DO NOT EDIT!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            :param weight: Total weight of the path
            """
            self.vertices = vertices
            self.weight = weight

        def __eq__(self, other):
            return self.vertices == other.vertices and self.weight == other.weight

        def __repr__(self):
            return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a vertex id to the path
            :param vertex: id of a vertex
            :return: None
            """
            self.vertices.append(vertex)

        def add_weight(self, weight):
            """
            Add weight to the path
            :param weight: weight
            :return: None
            """
            self.weight += weight

        def remove_vertex(self):
            """
            Remove the most recently added vertex from the path
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def remove(self, w):
            if not self.is_empty():
                self.vertices.pop()
                self.weight -= w

        def add(self, vid, w):
            self.vertices.append(vid)
            self.weight += w

        def is_empty(self):
            """
            Check if the path object is empty
            :return: True if empty, False otherwise
            """
            return len(self.vertices) == 0

    class Vertex(object):
        def __init__(self, number):
            """
            Class representing a vertex in the graph
            :param number: Unique id of this vertex
            """
            self.edges = []
            self.id = number
            self.visited = False

        def __repr__(self):
            return f"Vertex: {self.id}"

        __str__ = __repr__

        def add_edge(self, destination, weight):
            self.edges.append(Graph.Edge(self.id, destination, weight ))

        def degree(self):
            return len(self.edges)

        def get_edge(self, destination):
            found = False
            i = 0
            while not found and i < len(self.edges):
                if self.edges[i].destination == destination:
                    found = True
                else:
                    i += 1

            return self.edges[i] if found else None


        def clear(self):
            self.visited = False
            for edge in self.edges:
                edge.explored = False


        def get_edges(self):
            return self.edges

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: List of edges
        """
        random.seed(10)
        edges = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    edges.append([i, j, random.randint(-10, 50)])
        return edges

    def __init__(self, size=0, connectedness=0):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.construct_graph()

    def construct_graph(self):
        for source, dest, weight in self.generate_edges():
            self.adj_list[source] = self.adj_list.get(source, self.Vertex(source))
            self.adj_list[dest] = self.adj_list.get(dest, self.Vertex(dest))
            self.adj_list[source].add_edge(dest, weight)
        self.size = len(self.adj_list)

    def vertex_count(self):
        return self.size

    def vertices(self):
        return list(self.adj_list.values())

    def insert_edge(self, source, dest, weight):
        self.adj_list[source] = self.adj_list.get(source, self.Vertex(source))
        self.adj_list[dest] = self.adj_list.get(dest, self.Vertex(dest))
        self.adj_list[source].add_edge(dest, weight)



    def clear(self):
        for v in self.adj_list.values():
            v.clear()


    def preprocess(self,vertex):
        return list(edge for edge in vertex.get_edges() if not edge.explored)




    def find_valid_paths(self, source, dest, limit):
        # DFS
        stack = [self.Edge(None, source, 0)]
        paths = []
        path = self.Path()

        while stack:
            update = False
            edge= stack[-1]
            vertex = self.adj_list[edge.destination]

            if len(path.vertices) and path.vertices[-1] == vertex.id:
                update = True
            else:
                path.add(vertex.id, edge.weight)
                final = vertex.get_edge(dest)
                if final:
                    final.explored = True
                    path.add(dest , final.weight)
                    if path.weight <= limit:
                        paths.append(self.Path(path.vertices[:], path.weight))
                    path.remove(final.weight)

                children = self.preprocess(vertex)
                if children:
                    stack.extend(children)
                else:
                    update = True

            if update:
                edge.explored = True
                path.remove(edge.weight)
                stack.pop()
                vertex.clear()

        return paths



    def find_shortest_path(self, source, destination, limit):
        paths = self.find_valid_paths(source, destination, limit)
        return min(paths , key =lambda p: p.weight )

    def find_longest_path(self, source, destination, limit):
        paths = self.find_valid_paths(source, destination, limit)
        return max(paths , key =lambda p: p.weight )

    def find_most_vertices_path(self, source, destination, limit):
        paths = self.find_valid_paths(source, destination, limit)
        return max(paths , key =lambda p: len(p.vertices) )

    def find_least_vertices_path(self, source, destination, limit):
        paths = self.find_valid_paths(source, destination, limit)
        return min(paths , key =lambda p: len(p.vertices) )

    def check_path(self, path):
        summ = 0
        for i in range(len(path.vertices)-1):

            summ += self.adj_list[path.vertices[i]].get_edge(path.vertices[i +1]).weight
            print( self.adj_list[path.vertices[i]].get_edge(path.vertices[i +1]))


        return f" Real Weight: {summ}"