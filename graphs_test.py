import unittest
import graphs


class graphsTestCases(unittest.TestCase):

    def testAddNodes(self):
        self.assertEqual(graph_test.getNodes(), ['London', 'Birmingham', 'Leeds', 'Sheffield', 'Bradford', 'Liverpool', 'Manchester', 'Bristol'])

    def testAddEdges(self):
        self.assertEqual(graph_test.getEdges(), {('London', 'Birmingham'): 118, ('Birmingham', 'London'): 118, ('London', 'Leeds'): 200, ('Leeds', 'London'): 200, ('London', 'Sheffield'): 167, ('Sheffield', 'London'): 167, ('London', 'Bradford'): 207, ('Bradford', 'London'): 207, ('London', 'Liverpool'): 211, ('Liverpool', 'London'): 211, ('London', 'Manchester'): 199, ('Manchester', 'London'): 199, ('London', 'Bristol'): 119, ('Bristol', 'London'): 119, ('Birmingham', 'Leeds'): 124, ('Leeds', 'Birmingham'): 124, ('Birmingham', 'Sheffield'): 90, ('Sheffield', 'Birmingham'): 90, ('Birmingham', 'Bradford'): 129, ('Bradford', 'Birmingham'): 129, ('Birmingham', 'Liverpool'): 98, ('Liverpool', 'Birmingham'): 98, ('Birmingham', 'Manchester'): 86, ('Manchester', 'Birmingham'): 86, ('Birmingham', 'Bristol'): 88, ('Bristol', 'Birmingham'): 88, ('Leeds', 'Sheffield'): 40, ('Sheffield', 'Leeds'): 40, ('Leeds', 'Bradford'): 10, ('Bradford', 'Leeds'): 10, ('Leeds', 'Liverpool'): 72, ('Liverpool', 'Leeds'): 72, ('Leeds', 'Manchester'): 44, ('Manchester', 'Leeds'): 44, ('Leeds', 'Bristol'): 208, ('Bristol', 'Leeds'): 208, ('Sheffield', 'Bradford'): 48, ('Bradford', 'Sheffield'): 48, ('Sheffield', 'Liverpool'): 78, ('Liverpool', 'Sheffield'): 78, ('Sheffield', 'Manchester'): 78, ('Manchester', 'Sheffield'): 78, ('Sheffield', 'Bristol'): 180, ('Bristol', 'Sheffield'): 180, ('Bradford', 'Liverpool'): 67, ('Liverpool', 'Bradford'): 67, ('Bradford', 'Manchester'): 39, ('Manchester', 'Bradford'): 39, ('Bradford', 'Bristol'): 165, ('Bristol', 'Bradford'): 165, ('Liverpool', 'Manchester'): 34, ('Manchester', 'Liverpool'): 34, ('Liverpool', 'Bristol'): 181, ('Bristol', 'Liverpool'): 181, ('Manchester', 'Bristol'): 168, ('Bristol', 'Manchester'): 168})
    def testDijkstra(self):
        route_taken = graph_test.Dijkstra_algorithm("London")
        self.assertEqual(route_taken, {'London': 0, 'Birmingham': 118, 'Leeds': 200, 'Sheffield': 167, 'Bradford': 207, 'Liverpool': 211, 'Manchester': 199, 'Bristol': 119})


    def testTravellingSalesman(self):
        route_taken = graph_test.travellingSalesmanNN("London")
        self.assertEqual(route_taken[0], [('London', 'Birmingham'), ('Birmingham', 'Manchester'), ('Manchester', 'Liverpool'), ('Liverpool', 'Bradford'), ('Bradford', 'Leeds'), ('Leeds', 'Sheffield'), ('Sheffield', 'Bristol')])
        self.assertEqual(route_taken[1], 535)

if __name__ == '__main__':
    graph_test = graphs.Graph()
    graph_test.addNode("London")
    graph_test.addNode("Birmingham")
    graph_test.addNode("Leeds")
    graph_test.addNode("Sheffield")
    graph_test.addNode("Bradford")
    graph_test.addNode("Liverpool")
    graph_test.addNode("Manchester")
    graph_test.addNode("Bristol")


    graph_test.addEdge("London", "Birmingham", 118)
    graph_test.addEdge("London", "Leeds", 200)
    graph_test.addEdge("London", "Sheffield", 167)
    graph_test.addEdge("London", "Bradford", 207)
    graph_test.addEdge("London", "Liverpool", 211)
    graph_test.addEdge("London", "Manchester", 199)
    graph_test.addEdge("London", "Bristol", 119)

    graph_test.addEdge("Birmingham", "Leeds", 124)
    graph_test.addEdge("Birmingham", "Sheffield", 90)
    graph_test.addEdge("Birmingham", "Bradford", 129)
    graph_test.addEdge("Birmingham", "Liverpool", 98)
    graph_test.addEdge("Birmingham", "Manchester", 86)
    graph_test.addEdge("Birmingham", "Bristol", 88)

    graph_test.addEdge("Leeds", "Sheffield", 40)
    graph_test.addEdge("Leeds", "Bradford", 10)
    graph_test.addEdge("Leeds", "Liverpool", 72)
    graph_test.addEdge("Leeds", "Manchester", 44)
    graph_test.addEdge("Leeds", "Bristol", 208)

    graph_test.addEdge("Sheffield", "Bradford", 48)
    graph_test.addEdge("Sheffield", "Liverpool", 78)
    graph_test.addEdge("Sheffield", "Manchester", 78)
    graph_test.addEdge("Sheffield", "Bristol", 180)

    graph_test.addEdge("Bradford","Liverpool", 67)
    graph_test.addEdge("Bradford", "Manchester", 39)
    graph_test.addEdge("Bradford", "Bristol", 165)

    graph_test.addEdge("Liverpool", "Manchester", 34)
    graph_test.addEdge("Liverpool", "Bristol", 181)

    graph_test.addEdge("Manchester", "Bristol", 168)

    unittest.main()