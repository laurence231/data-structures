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

    def Dijkstra_algorithm(self, starting_node):

        def possibleEdges(origin_node, possible_routes):
            for node_pair in self.edges:
                if node_pair[0] == origin_node:   #if the origin node is the origin in the dictionary of node-edge pairs
                    weight = self.edges[node_pair]
                    possible_routes[node_pair] = weight
            if possible_routes:
                print('here are poss routes ', possible_routes)
                traverseMinEdge(possible_routes)

        def traverseMinEdge(possible_routes):
            print(possible_routes, 'here are the possible routes!')
            key_min = min(possible_routes, key=(lambda k: possible_routes[k]))
            print(key_min, 'THIS IS THE EDGE CHOSEN')
            new_origin_node = key_min[1]
            possible_routes.pop(key_min)
            route_taken.append(key_min)
            possibleEdges(new_origin_node, possible_routes)

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
    graph_test.addEdge("A", "C", 100)
    graph_test.getEdges()
    graph_test.Dijkstra_algorithm("A")


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