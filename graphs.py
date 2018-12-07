from graphviz import Digraph
from PyInquirer import prompt,style_from_dict, Token, Separator
import math

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
        dot.render('test-output/visualisation.gv', view=True)

    def Dijkstra_algorithm(self, starting_node):

        distance_to_node = {}
        for node in self.nodes:
            distance_to_node[node] = math.inf
        distance_to_node[starting_node] = 0

        def possibleEdges(origin_node, distance_to_node)
            for node_pair in self.edges:
                if node_pair[0] in traversed and node_pair[1] not in traversed:
                    weight = self.edges[node_pair]
                    if weight < distance_to_node[node_pair[1]]:
                        distance_to_node[node_pair[1]] = weight
            print('here are the updated distances: ', distance_to_node)
            if sorted(traversed) != sorted(self.nodes):
                traverseMinEdge(origin_node, distance_to_node)
            else:
                print(traversed, ' we are done traversing. Here are the distances: ', distance_to_node)

        def traverseMinEdge(origin_node, distance_to_node):


        # def possibleEdges(origin_node, possible_routes):
        #     for node_pair in self.edges:
        #         if node_pair[0] in traversed and node_pair[1] not in traversed:
        #             weight = self.edges[node_pair]
        #             possible_routes[node_pair] = weight
        #     print('here are the possible routes to choose from', possible_routes)
        #     if sorted(traversed) != sorted(self.nodes):
        #         traverseMinEdge(origin_node,possible_routes)
        #     else:
        #         print(self.nodes)
        #         print(traversed, 'Here is the order of nodes traversed')
        #
        # def traverseMinEdge(origin_node, possible_routes):
        #     print(possible_routes)
        #     key_min = min(possible_routes, key=possible_routes.get)
        #     print(key_min, 'this is the minimum key')
        #     if key_min[1] not in traversed:
        #         weight_of_min_edge = possible_routes[key_min]
        #         print(key_min, 'THIS IS THE EDGE CHOSEN, with weight', weight_of_min_edge)
        #         total_weight.append(weight_of_min_edge)
        #         origin_node.append(key_min[1])
        #         traversed.append(key_min[1])
        #         print(traversed, 'Traversed')
        #         possible_routes.pop(key_min)
        #         route_taken.append(key_min)
        #         possible_routes = {}
        #         possibleEdges(origin_node, possible_routes)
        #     else:
        #         print('we have a problem!')
        #         quit()
        #
        # origin_node = [starting_node]
        # traversed = [starting_node]
        # total_weight = []
        # route_taken = []
        # possible_routes = {}
        # possibleEdges(origin_node, possible_routes)
        # print(route_taken, 'This is the route taken by Dijkstra\'s algorithm')
        # return route_taken


def parseInput(answer, graph):
    '''
    Converts input from UI into graph operation
    :param answer: The dictionary with the chosen graph operation from the UI
    :param graph: the created graph (object) upon which to operate
    :return:
    '''
    if answer != {'Graph Building': []}:
        if list(answer.values())[0][0] == 'Create a new node':
            node_name = input('What do you want to call this new node?: ',)
            graph.addNode(node_name)
        elif list(answer.values())[0][0] == 'Create new weighted edge':
            edge_1 = input('First node: ' )
            edge_2 = input('Second node: ' )
            weight = int(input('What is the weight on this edge?: '))
            graph.addEdge(edge_1, edge_2, weight)
        elif list(answer.values())[0][0] == 'Visualise the graph':
            graph.visualiseNodes()
        elif list(answer.values())[0][0] == 'Apply Dijkstra\'s algorithm':
            start_node = input('What starting node would you like?: ' ,)
            graph.Dijkstra_algorithm(start_node)
        elif list(answer.values())[0][0] == 'quit':
            quit()
    else:
        print('You need to select an answer!')

def userInterface():
    '''
    Uses PyInquirer to create a interactive UI
    :return: dictionary with chosen graph operation
    '''
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    questions = [
        {
            'type': 'checkbox',
            'message': 'Select Operation',
            'name': 'Graph Building',
            'choices': [
                # Separator('= The Meats ='),
                {
                    'name': 'Create a new node'
                },
                {
                    'name': 'Create new weighted edge'
                },
                {
                    'name': 'Visualise the graph'
                },
                {
                    'name': 'Apply Dijkstra\'s algorithm'
                },
                {
                    'name': 'quit'
                }
            ],
        }
    ]
    answers = prompt(questions, style=style)
    if len(answers) == 1:
        return answers
    else:
        print('you must only select one option.')

###############
# FOR UI functionality
#########
if __name__ == "__main__":
    graph_test = Graph()
    while True:
        answers = userInterface()
        parseInput(answers, graph_test)