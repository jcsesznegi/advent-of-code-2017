import os, re

f = open(os.path.join(os.path.dirname(__file__), '../input/7/part1.txt'), 'r')

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, name, weight):
        newNode = Node(name, weight)
        self.nodes.append(newNode)
         
    def addEdge(self, name, edge):
        newEdge = (name, edge)
        self.edges.append(newEdge)
       
    def addEdges(self, name, edges):
        for edge in edges:
            self.addEdge(name, edge)

    def getBaseNode(self):
        base = None
        for node in self.nodes:
            hasParent = False
            for edge in self.edges:
                if edge[1] == node.name:
                    hasParent = True
                    break
            if not hasParent:
                base = node
                break
        return base

def main():

    graph = Graph()

    line = f.readline().rstrip()
    while line:
        parts = line.split(" -> ")
        name = ''
        weight = 0
        edges = []
        matches = re.match(r'(\w+)\s\((.*)\)$', parts[0])

        if matches:
            name = matches.group(1) 
            weight = matches.group(2) 

        graph.addNode(name, weight)

        if len(parts) > 1:
            edges = parts[1].split(', ')
            graph.addEdges(name, edges)

        """
        print(name)
        print(weight)
        print(edges)
        print('------------')
        """

        line = f.readline().rstrip()

    base = graph.getBaseNode()
    print(base.name)

if __name__ == '__main__':
   main()
