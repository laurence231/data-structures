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
            print("invalid nodes!")

    def visualiseGraph(self):
        for node_tuple in self.edges:
            print(node_tuple[0], "-"*5,self.edges[node_tuple],"-"*5, node_tuple[1])




if __name__ == "__main__":
    graph_test = Graph()
    graph_test.addNode("A")
    graph_test.addNode("B")
    graph_test.getNodes()
    graph_test.addEdge("A", "B", 0.5)
    graph_test.getEdges()
    graph_test.addEdge("A", "D", 0.1)
    graph_test.visualiseGraph()