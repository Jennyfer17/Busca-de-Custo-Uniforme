class Node:

    def __init__(self, key):

        self.key, self.successors, self.weight_successors = key, [], {}

    def getKey(self):
        return self.key
    
    def getSuccessors(self):
        return self.successors
    
    def addSuccessors(self, node, weight):

        if node.getKey() not in self.weight_successors:
            self.successors.append(node)
            self.weight_successors[node.getKey()] = weight

    def getWeightSuccessors(self):
        return self.weight_successors
    
class Graph:

    def __init__(self):
        self.nodes = {}

    def addNode(self, key_node):
        if key_node in self.nodes:
            print('Error: Key %s already exists!'%key_node)
        else:
            node = Node(key_node)
            self.nodes[key_node] = node

    def connect(self, key_source, key_destination, weight):

        if key_source in self.nodes and key_destination in self.nodes:
            if key_source != key_destination:
                if weight > 0:
                    self.nodes[key_source].addSuccessor(self.nodes[key_destination])
                else:
                    print('Error: weight must be positive!')
            else:
                print('Error: Same keys!!')
        else:
            print('Error: key does not exists!!')

    def getWeightEdge(self, key_source, key_successor):
        if key_successor in self.nodes and key_successor in self.nodes:
            if key_source != key_successor:
                weight_successors = self.nodes[key_source].getWeightSuccesors()
                if key_successor in weight_successors:
                    return weight_successors[key_successor]
                else:
                    print('Error: succesor does not exists!!')
            else:
                print('Error: same keys!!')
        else:
            print('Error: key does not exists')

    def getSuccessors(self, key_node):
        if key_node in self.nodes:
            nodes = self.nodes[key_node].getSuccesors()
            keys_successors = [node.getKey() for node in nodes]
            return keys_successors
        else:
            print('Error: key does not exists!!')


    def getNodes(self):
        return self.nodes

            