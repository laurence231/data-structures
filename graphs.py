from graphviz import Digraph

class Graph:
    def __init__(self, nodes=[], edges={}):
        self.nodes = nodes
        self.edges = edges

    def getNodes(self):
        print(self.nodes)
        return self.nodes

    def getNodesCOPY(self):
        nodes_copy = self.nodes
        return nodes_copy


    def getEdges(self):
        print(self.edges)
        return self.edges

    def addNode(self, node_name):
        self.nodes.append(node_name)

    def addEdge(self, node_1, node_2, weight):
        if node_1 and node_2 in self.getNodes():
            self.edges[(node_1, node_2)] = weight
        else:
            print("INVALID NODES! try again")

    def visualiseNodes(self):
        dot = Digraph(comment='test of a graph using graphviz')
        for node_name in self.nodes:
            dot.node(node_name)
        print(self.edges)
        edges = []
        for edge in self.edges:
            edges.append(edge[0]+edge[1])
        dot.edges(edges)
        print(dot.source)
        dot.render('test-output/round-table.gv', view=True)

    def Dijkstra_algorithm(self, starting_node):

        def possibleEdges(origin_node, possible_routes):
            for node_pair in self.edges:
                # print(node_pair[1], 'not in ', traversed, node_pair[1] not in traversed)
                if node_pair[0] in origin_node:   #if the origin node is the origin in the dictionary of node-edge pairs
                    weight = self.edges[node_pair]
                    possible_routes[node_pair] = weight
            if possible_routes and node_pair[1] not in traversed:
                print('here are poss routes ', possible_routes)
                traverseMinEdge(origin_node,possible_routes)
            else:
                print(self.nodes)
                print(traversed)

        def traverseMinEdge(origin_node, possible_routes):
            print(possible_routes, 'here are the possible routes!')
            key_min = min(possible_routes, key=(lambda k: possible_routes[k]))
            print(key_min, 'THIS IS THE EDGE CHOSEN')
            weight_of_min_edge = possible_routes[key_min]
            total_weight.append(weight_of_min_edge)
            origin_node.append(key_min[1])
            traversed.append(key_min[1])
            print(traversed, 'Traversed')
            possible_routes.pop(key_min)
            route_taken.append(key_min)
            possibleEdges(origin_node, possible_routes)

        traversed = [starting_node]
        total_weight = []
        route_taken = []
        possible_routes = {}
        possibleEdges(starting_node, possible_routes)
        print(route_taken)


if __name__ == "__main__":
    graph_test = Graph()
    graph_test.addNode("A")
    graph_test.addNode("B")
    graph_test.addNode("C")
    graph_test.addEdge("A", "B", 3)
    graph_test.addEdge("B", "C", 4)
    graph_test.addEdge("A", "C", 1)
    graph_test.getEdges()
    graph_test.visualiseNodes()


    #########################################################
    #
    #    Here is the  very primitive attempt at interaction
    #
    ##########################################################
    #
    # graph_test = Graph()
    # while True:
    #     user_input = input("add a NEW NODE (enter 1) or add a WEIGHTED EDGE (enter 2)??: ", )
    #     if user_input == 1:
    #         node_name = raw_input("what is the name for this node? (enter inbetween ""): ", )
    #         graph_test.addNode(node_name)
    #         graph_test.getNodes()
    #         graph_test.visualiseNodes()
    #     if user_input == 2:
    #         node_1 = raw_input("What is the origin node?: ", )
    #         node_2 = raw_input("What is the destination node?: ", )
    #         weighting = input("Enter the weighting you require: ", )
    #         graph_test.addEdge(node_1, node_2, weighting)
    #         graph_test.getEdges()
    #         graph_test.visualiseNodes()
    #     else:
    #         print('Didnt recognise your input! try again')