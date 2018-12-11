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
        if node_name not in self.nodes:
            self.nodes.append(node_name)

    def addEdgeSingle(self, node_1, node_2, weight):
        if node_1 and node_2 in self.nodes:
            self.edges[(node_1, node_2)] = weight
        else:
            print(' ')
            print("INVALID NODES! try again")
            print(' ')

    def addEdge(self, node_1, node_2, weight):
        if node_1 and node_2 in self.nodes and type(weight) == float or type(weight) == int:
            self.edges[(node_1, node_2)] = weight
            self.edges[(node_2, node_1)] = weight
        else:
            print(' ')
            print("Invalid nodes or weight. try again")
            print(' ')

    def visualiseNodes(self):
        dot = Digraph(comment='test of a graph using graphviz')
        for node_name in self.nodes:
            dot.node(node_name)
        print(self.edges)
        edges = []
        for edge in self.edges:
            print(edge[0], 'edges', edge[1])
            edges.append(edge[0]+edge[1])
        print("NOTE: THIS visualisation will only work for if every node name is a single letter e.g. \"A\"")
        dot.edges(edges)
        print(dot.source)
        dot.render('test-output/visualisation.gv', view=True)

    def Dijkstra_algorithm(self, starting_node):
        '''
        This function computes the length of the journey to each node from the user defined starting node.
        '''

        def possibleEdges(distance_to_node):
            '''
            This function returns a dictionary of available paths to take (possible_routes) with the key of the edge,
            and a corresponding value being the weight of the edge.
            Takes input of possible routes (does it need this?) and a dictionary of the distance_to_node
            (dictionary of total weight to reach output node from input node)
            '''
            possible_routes = {}
            for node_pair in self.edges:
                if node_pair[0] in traversed and node_pair[1] not in traversed:
                    weight = self.edges[node_pair]
                    if weight + distance_to_node[node_pair[0]] <= distance_to_node[node_pair[1]]:
                        distance_to_node[node_pair[1]] = weight + distance_to_node[node_pair[0]]
                        possible_routes[node_pair] = weight
            print(' ')
            print('here are the updated distances: ', distance_to_node)
            print(' ')
            if sorted(traversed) != sorted(self.nodes):
                traverseMinEdge(possible_routes, distance_to_node)
            else:
                print(' ')
                print(traversed, ' we are done traversing. Here are the distances to any node from selected starting '
                                 'node, according to Dijkstra\'s algorithm: ', distance_to_node)
                print(' ')

        def traverseMinEdge(possible_routes, distance_to_node):
            '''
            This function requires a dictionary of possible routes. It will pick the minimum route, traverse that route,
            then add the current traversed node to the list of viable starting points, which is used to build the
            possible_routes dictionary in possibleEdges().
            '''
            if len(possible_routes) != 0:
                print(possible_routes, ' are the possible routes')
                key_min = min(possible_routes, key=possible_routes.get)
                if key_min[1] not in traversed:
                    weight_of_min_edge = possible_routes[key_min]
                    print(key_min, 'THIS IS THE EDGE CHOSEN, with weight', weight_of_min_edge)
                    traversed.append(key_min[1])
                    print(traversed, 'Traversed')
                    print(' ')
                    print(' ')
                    possibleEdges(distance_to_node)
                else:
                    print('something broke!')
                    quit()
            else:
                print('possible edges was zero. Why?! is it finished?!')

        distance_to_node = {}
        for node in self.nodes:
            distance_to_node[node] = math.inf
        distance_to_node[starting_node] = 0
        traversed = [starting_node]
        possibleEdges(distance_to_node)
        return distance_to_node

    def travellingSalesmanNN(self, starting_node):
        '''
        THIS function returns the route that attempts to minimize the distance for a travelling salesman to visit every
        node in the graph, using the nearest neighbours approximation
        '''

        def possibleEdges(traversed, current_city):
            '''
            This function, given a valid input node, will compute the dictionary of possible routes that can be traversed
            by the salesman, given his current node. If he needs to retrace his steps as there are no valid nodes,
            he returns to the previous node, and has the weight of return travel added.
            '''
            possible_routes = {}
            for node_pair in self.edges:
                ###
                # test first if the CURRENT NODE has any nearest neighbours
                ###
                if node_pair[0] == current_city and node_pair[1] not in traversed:
                    weight = self.edges[node_pair]
                    possible_routes[node_pair] = weight
            ###
            #  otherwise, go back down the last path just taken, and add the weight.
            ###
            if len(possible_routes) == 0 and sorted(traversed) != sorted(self.nodes):
                print(' ')
                print('retracing our steps!')
                current_city_index = traversed.index(current_city)
                print('We are currently at current city: ', current_city)
                weight = self.edges[(traversed[current_city_index - 1], current_city)]
                total_weight.append(weight)
                route_taken.append((current_city, traversed[current_city_index-1]))
                possibleEdges(traversed, traversed[current_city_index-1])
            print(' ')
            print('here are the possible routes to choose from', possible_routes)
            if sorted(traversed) != sorted(self.nodes):
                traverseMinEdge(traversed, possible_routes)
            else:
                print(self.nodes)
                print(traversed, 'Here is the order of nodes traversed')

        def traverseMinEdge(traversed, possible_routes):
            '''
            Given an input of possible routes the salesman can traverse, the minimum weighted route is selected, and the
            salesman travels down that route. The destination node becomes the current node, and then new possible routes are calculated
            via possibleEdges()
            '''
            print(possible_routes)
            key_min = min(possible_routes, key=possible_routes.get)
            if key_min[1] not in traversed:
                weight_of_min_edge = possible_routes[key_min]
                print(key_min, ' is the minimum edge, with weight', weight_of_min_edge)
                total_weight.append(weight_of_min_edge)
                traversed.append(key_min[1])
                print(traversed, 'Traversed')
                possible_routes.pop(key_min)
                route_taken.append(key_min)
                current_city = key_min[1]
                print(total_weight,' = ', sum(total_weight), ' total weight so far')
                print(' ')
                possibleEdges(traversed, current_city)
            else:
                print('we have a problem!')
                quit()
        traversed = [starting_node]
        total_weight = []
        route_taken = []
        possibleEdges(traversed, starting_node)
        print(' ')
        print(route_taken, 'This is the route taken by the Travelling Salesman using the nearest neighbours algorithm, '
                           'with total accumulated weight of: ', sum(total_weight))
        print(' ')
        return route_taken, sum(total_weight)


def parseInput(answer, graph):
    '''
    Converts input from UI into graph operation
    :param answer: The dictionary with the chosen graph operation from the UI
    :param graph: the created graph (object) upon which to operate
    :return:
    '''
    if answer != {'Graph Building': []}:
        option_selected = list(answer.values())[0][0]
        if option_selected == 'Create a new node':
            node_name = input('What do you want to call this new node? (NOTE: must be single letter for now, if you want to use visualisation tool!): ',)
            graph.addNode(node_name)
        elif option_selected == 'Create new reversible weighted edge':
            edge_1 = input('First node: ' )
            edge_2 = input('Second node: ' )
            weight = int(input('What is the weight on this edge?: '))
            graph.addEdge(edge_1, edge_2, weight)
        elif option_selected == 'Create a NOT reversed weighted edge':
            edge_1 = input('First node: ' )
            edge_2 = input('Second node: ' )
            weight = int(input('What is the weight on this edge?: '))
            graph.addEdgeSingle(edge_1, edge_2, weight)
        elif option_selected == 'Visualise the graph':
            graph.visualiseNodes()
        elif option_selected == 'Apply Travelling salesman (Nearest Neighbours) algorithm':
            start_node = input('What starting node would you like?: ' ,)
            graph.travellingSalesmanNN(start_node)
        elif option_selected == 'Apply Dijkstra\'s algorithm':
            start_node = input('What starting node would you like?: ' ,)
            graph.Dijkstra_algorithm(start_node)
        elif option_selected == 'quit':
            quit()
    else:
        print(' ')
        print('You need to select an answer!')
        print(' ')

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
                {
                    'name': 'Create a new node'
                },
                {
                    'name': 'Create new reversible weighted edge'
                },
                {
                    'name': 'Create a NOT reversed weighted edge'
                },
                {
                    'name': 'Visualise the graph'
                },
                {
                    'name': 'Apply Travelling salesman (Nearest Neighbours) algorithm'
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
        print(' ')
        print('you must only select one option.')
        print(' ')

##############
#FOR UI functionality
########
if __name__ == "__main__":
    graph_test = Graph()
    while True:
        answers = userInterface()
        parseInput(answers, graph_test)
