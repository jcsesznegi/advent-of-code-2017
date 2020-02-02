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

    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def getChildNodes(self, parent):
        children = []
        for edge in self.edges:
            if edge[0] == parent.name:
                children.append(self.getNode(edge[1]))
        return children 

    def getTowerWeight(self, node):
        children = self.getChildNodes(node)

        childrenWeight = 0
        for child in children:
            childrenWeight += self.getTowerWeight(child)

        return node.weight + childrenWeight

    def findUnbalancedChildInfo(self, node):
        children = self.getChildNodes(node)

        towerWeights = []
        for child in children:
            towerWeights.append(self.getTowerWeight(child))

        uniqueIndex, uniqueWeight, otherWeight = -1, 0, 0
        for index, towerWeight in enumerate(towerWeights):
            if towerWeights.count(towerWeight) == 1:
                uniqueIndex = index
                uniqueWeight = towerWeight
            else:
                otherWeight = towerWeight

        return (uniqueIndex, uniqueWeight, otherWeight)

    def findUnbalancedNodeAdjustedWeight(self, node):
        unbalancedChildInfo = self.findUnbalancedChildInfo(node)
        uniqueIndex = unbalancedChildInfo[0]
        uniqueWeight = unbalancedChildInfo[1]
        otherWeight = unbalancedChildInfo[2]

        children = self.getChildNodes(node)

        if uniqueIndex >= 0:
            unbalancedChild = children[uniqueIndex]
            nextUnbalancedChildInfo = self.findUnbalancedChildInfo(unbalancedChild)
            nextUniqueIndex = nextUnbalancedChildInfo[0]

            if nextUniqueIndex >= 0:
                return self.findUnbalancedNodeAdjustedWeight(unbalancedChild)
                
            difference = otherWeight - uniqueWeight;
            return children[uniqueIndex].weight + difference

        for child in children:
            adjustedWeight = self.findUnbalancedNodeAdjustedWeight(child)
            if adjustedWeight:
                break

        return adjustedWeight

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
            weight = int(matches.group(2))

        graph.addNode(name, weight)

        if len(parts) > 1:
            edges = parts[1].split(', ')
            graph.addEdges(name, edges)

        line = f.readline().rstrip()

    base = graph.getBaseNode()
    adjustedWeight = graph.findUnbalancedNodeAdjustedWeight(base)

    print(adjustedWeight)

if __name__ == '__main__':
   main()
