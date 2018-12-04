class Graph:
    def __init__(self, nodes=[], edges={}):
        self.nodes = nodes
        self.edges = edges

    def getNodes(self):
        print(self.nodes)
        return self.nodes

    def getEdges(self):
        for node in self.edges:
            print(node, self.edges[node])
        return self.edges

    def addNode(self, node_name):
        self.nodes.append(node_name)

    def addEdge(self, node_1, node_2, weight):
        if node_1 and node_2 in self.getNodes():
            self.edges[(node_1, node_2)] = weight
        else:
            print("INVALID NODES! try again")

    def visualiseNodes(self):
        for node_tuple in self.edges:
            print(node_tuple[0], "-"*5,self.edges[node_tuple],"-"*5, node_tuple[1])




if __name__ == "__main__":
    graph_test = Graph()
    while True:
        user_input = input("add a NEW NODE (enter 1) or add a WEIGHTED EDGE (enter 2)??: ", )
        if user_input == 1:
            node_name = raw_input("what is the name for this node? (enter inbetween ""): ", )
            graph_test.addNode(node_name)
            graph_test.getNodes()
            graph_test.visualiseNodes()
        if user_input == 2:
            node_1 = raw_input("What is the origin node?: ", )
            node_2 = raw_input("What is the destination node?: ", )
            weighting = input("Enter the weighting you require: ", )
            graph_test.addEdge(node_1, node_2, weighting)
            graph_test.getEdges()
            graph_test.visualiseNodes()
        else:
            print('Didnt recognise your input! try again')