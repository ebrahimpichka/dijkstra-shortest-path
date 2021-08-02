import random

class Node():
    def __init__(self, id, previous_node=None, shortest_path_from_start=float('inf')):
        self.id = id
        self.neighbours = set()
        self.previous_node = previous_node
        self.shortest_path_from_start = shortest_path_from_start
        self.is_visited = False
    
class Graph:
    def __init__(self):
        self.nodes = set()
        self.visited = set()
        self.unvisited = set()
        # self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)
        self.unvisited.add(node)
    
    def add_edge(self, from_node_id, to_node_id, weight):
        for node_1 in self.nodes:
            for node_2 in self.nodes:
                if (node_1.id == from_node_id) and  (node_2.id == to_node_id):
                    node_1.neighbours.add((node_2,weight))
        


def solve(graph, source_node_id, target_node_id, trace=False):

    source = None
    for node in graph.nodes:
        if node.id == source_node_id:
            source = node
            source.shortest_path_from_start = 0
    if source == None:
        raise("There is no node with id = {source_node_id}")
    
    current_node = source

    while graph.unvisited != 0:
        if trace:
            print(f"visiting {current_node.id}")
        for neighbour, weight in current_node.neighbours:
            if not neighbour.is_visited:
                distance_from_source = current_node.shortest_path_from_start + weight
                # print(current_node.id,':',current_node.shortest_path_from_start,'+',weight)
                if distance_from_source < neighbour.shortest_path_from_start:
                    neighbour.shortest_path_from_start = distance_from_source
                    neighbour.previous_node = current_node
                    
                    if trace:
                        print(f"\tupdated {neighbour.id} to {distance_from_source}")
        
        if trace:
            print()

        current_node.is_visited = True
        graph.visited.add(current_node)
        graph.unvisited.remove(current_node)

        neighbours = [x for x in current_node.neighbours if not x[0].is_visited]
        neighbour_weights = [x[1] for x in neighbours]
        if len(neighbour_weights) != 0:
            index = neighbour_weights.index(min(neighbour_weights))
            current_node = neighbours[index][0]

            if trace:
                print(f"\t==> chose {current_node.id} with value {current_node.shortest_path_from_start}")
        else:
            if len(graph.unvisited) != 0:
                current_node = random.choice(list(graph.unvisited))
            else:
                break
    
    target = None
    for node in graph.nodes:
        if node.id == target_node_id:
            target = node

    path = []
    curr_node = target
    path.append
    while curr_node != source:
        path.append(curr_node.id)
        curr_node = curr_node.previous_node
    path.append(source_node_id)
    
    return(path, target.shortest_path_from_start)



if __name__ == '__main__':

    # input arguments
    source_node_id = 's'
    target_node_id = 'e'

    # constructing the directed grapgh
    graph = Graph()

    # problem set 1 (easy)
    # graph.add_node(Node(0))
    # graph.add_node(Node(1))
    # graph.add_node(Node(2))
    # graph.add_node(Node(3))
    # graph.add_node(Node(4))

    # graph.add_edge(from_node_id=0, to_node_id=1, weight=4)
    # graph.add_edge(from_node_id=0, to_node_id=2, weight=1)
    # graph.add_edge(from_node_id=2, to_node_id=1, weight=2)
    # graph.add_edge(from_node_id=2, to_node_id=3, weight=5)
    # graph.add_edge(from_node_id=1, to_node_id=3, weight=1)
    # graph.add_edge(from_node_id=3, to_node_id=4, weight=3)

    # problem set 2 (medium)
    graph.add_node(Node('s'))
    graph.add_node(Node('a'))
    graph.add_node(Node('c'))
    graph.add_node(Node('e'))
    graph.add_node(Node('b'))
    graph.add_node(Node('d'))

    graph.add_edge(from_node_id='s', to_node_id='a', weight=1)
    graph.add_edge(from_node_id='a', to_node_id='c', weight=2)
    graph.add_edge(from_node_id='c', to_node_id='e', weight=1)
    graph.add_edge(from_node_id='s', to_node_id='b', weight=5)
    graph.add_edge(from_node_id='b', to_node_id='d', weight=2)
    graph.add_edge(from_node_id='d', to_node_id='e', weight=2)
    graph.add_edge(from_node_id='a', to_node_id='b', weight=2)
    graph.add_edge(from_node_id='a', to_node_id='d', weight=1)
    graph.add_edge(from_node_id='c', to_node_id='d', weight=3)

    path, total_cost = solve(graph, source_node_id=source_node_id, target_node_id=target_node_id ,trace=True)
    path.reverse()

    print(f"Shortest path from node {source_node_id} to {target_node_id}:\n")
    print(" --> ".join(map(str,path)))

    print(f"\n\ntotal cost of the path: {total_cost}")
