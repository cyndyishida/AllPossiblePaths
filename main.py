#from Graph import Graph
from SUGraph import Graph
from pprint import pprint
def test1():
    print("############## TEST 1 ##############")
    graph = Graph(5, 1)
    paths = graph.find_valid_paths(0, 4, 50)
    #print("\n".join(str(node) + str(node.get_edges()) for node in graph.adj_list.values() ))
    print("".join(map(str, sorted(paths, key= lambda p: p.weight ))))

    assert (sum(p.weight for p in paths) == 28 - 16 + 14 + 40 + 19)



    shortest = graph.find_shortest_path(0, 4, 50)
    longest = graph.find_longest_path(0, 4, 50)
    least = graph.find_least_vertices_path(0, 4, 50)
    most = graph.find_most_vertices_path(0, 4, 50)

    print(f"Shortest: {shortest}", end='')
    print(f"Longest: {longest}", end='')
    print(f"Least: {least}", end='')
    print(f"Most: {most}", end='')

    assert (shortest.weight == -16)
    assert (longest.weight == 40)
    assert (least.weight == 19)
    assert (most.weight == 28)


def test2():
    print("############## TEST 2 ##############")
    graph = Graph(25, 1)
    paths = graph.find_valid_paths(10, 3, 5000)
    print("".join(map(str, sorted(paths, key= lambda p: p.weight ))))
    assert (sum(p.weight for p in paths) == 0)
    print("Should be no output")


def test3():
    #print("\n".join(str(node) + str(node.get_edges()) for node in graph.adj_list.values() ))
    print("############## TEST 3 ##############")
    graph = Graph(100, 0.15)
    paths = graph.find_valid_paths(21, 78, 50)
    print("".join([str(path) for path in paths]))

    #assert (sum(p.weight for p in paths) == 298)

    #shortest = graph.find_shortest_path(21, 78, 50)
    #longest = graph.find_longest_path(21, 78, 50)
    #least = graph.find_least_vertices_path(21, 78, 50)
    #most = graph.find_most_vertices_path(21, 78, 50)

    #print(f"Shortest: {shortest}", end='')
    #print(f"Longest: {longest}", end='')
    #print(f"Least: {least}", end='')
    #print(f"Most: {most}", end='')

    #assert (shortest.weight == 1)
    #assert (longest.weight == 47)
    #assert (len(least.vertices) == 4)
    #assert (len(most.vertices) == 8)


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
