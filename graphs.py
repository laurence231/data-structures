class Graph:
    def __init__(self, nodes=[], edges={}):
        self.nodes = nodes
        self.edges = edges

    def getNodes(self):
        print(self.nodes)
        return self.nodes

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
        for node_pair in self.edges:
            print(node_pair[0], "-"*5,self.edges[node_pair],"-"*5, node_pair[1])

    def possibleEdges(self, origin_node):
        possible_routes = {}
        for node_pair in self.edges:
            if node_pair[0] == origin_node:   #if the origin node is the origin in the dictionary of node-edge pairs
                weight = self.edges[node_pair]
                possible_routes[node_pair] = weight
        return possible_routes

    def traverseMinEdge(self, possible_routes):
        print(possible_routes)
        key_min = min(possible_routes, key=(lambda k: possible_routes[k]))
        print(key_min)



        # weight = self.edges[node_pair]
        # weight_sum += weight
        # destination_node = node_pair[1]
        # print('destination_node: ', destination_node, 'weight: ', weight)
        # print('weight sum: ', weight_sum, 'path followed: ', path_followed)
        # path_followed.append(node_pair)
        # origin_node = destination_node
        # # self.traverseEdge(origin_node, weight_sum, node_pair)


if __name__ == "__main__":
    graph_test = Graph()
    graph_test.addNode("A")
    graph_test.addNode("B")
    graph_test.addNode("C")
    graph_test.addEdge("A", "B", 3)
    graph_test.addEdge("B", "C", 4)
    graph_test.addEdge("A", "C", 100)
    graph_test.getEdges()
    poss_route = graph_test.possibleEdges("A")
    graph_test.traverseMinEdge(poss_route)

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