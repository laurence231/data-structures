import unittest
import graphs


class graphsTestCases(unittest.TestCase):

    def testAddNodes(self):
        self.assertEqual(graph_test.getNodes(), ['A','B','C','D','E'])

    def testAddEdges(self):
        self.assertEqual(graph_test.getEdges(), {('A', 'B'): 4, ('A', 'C'): 2, ('B', 'C'): 3, ('C', 'B'): 1, ('B', 'D'): 2, ('B', 'E'): 3, ('C', 'D'): 4, ('C', 'E'): 5, ('E', 'D'): 1})

    def testDijkstra(self):
        route_taken = graph_test.Dijkstra_algorithm("A")
        self.assertEqual(route_taken, [('A', 'C'), ('C', 'B'), ('B', 'D'), ('B', 'E')])

if __name__ == '__main__':
    graph_test = graphs.Graph()
    graph_test.addNode("A")
    graph_test.addNode("B")
    graph_test.addNode("C")
    graph_test.addNode("D")
    graph_test.addNode("E")
    graph_test.addEdge("A", "B", 4)
    graph_test.addEdge("A", "C", 2)
    graph_test.addEdge("B", "C", 3)
    graph_test.addEdge("C", "B", 1)
    graph_test.addEdge("B", "D", 2)
    graph_test.addEdge("B", "E", 3)
    graph_test.addEdge("C", "D", 4)
    graph_test.addEdge("C", "E", 5)
    graph_test.addEdge("E", "D", 1)
    unittest.main()