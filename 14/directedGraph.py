
class DirectedGraph:
    def __init__(self):
        self.graph = {}
        self.visited = []
        self.regionCount = 0

    def addNode(self, coordinate):
        self.graph[coordinate] = []

    def addEdge(self, coordinate, edge):
        self.graph[coordinate].append(edge)

    def getRegionCount(self):
        return self.regionCount

    def markNodesAsVisited(self, coordinate):
        if coordinate not in self.visited:
            self.visited.append(coordinate)
            for edge in self.graph[coordinate]:
                self.markNodesAsVisited(edge)

    def findRegions(self):
        for coordinate, edges in self.graph.items():
            if coordinate not in self.visited:
                self.regionCount += 1
                self.markNodesAsVisited(coordinate)
