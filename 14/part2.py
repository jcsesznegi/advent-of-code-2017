
import os
from defragmenter import Defragmenter
from directedGraph import DirectedGraph

f = open(os.path.join(os.path.dirname(__file__), '../input/14/part1.txt'), 'r')

def main():
    keyString = f.readline().rstrip()
    defragmenter = Defragmenter(keyString)
    grid = defragmenter.getGrid()
    expandedGrid = [list(row) for row in grid]

    graph = DirectedGraph()
    for rowIdx, row in enumerate(expandedGrid):
        for columnIdx, column in enumerate(row):
            if column == '1':
                coordinate = (rowIdx, columnIdx)
                graph.addNode(coordinate)

                if (
                    rowIdx > 0
                    and expandedGrid[rowIdx - 1][columnIdx] == '1'
                    ):
                    graph.addEdge(coordinate, (rowIdx - 1, columnIdx))
                if (
                    columnIdx + 1 < 128
                    and expandedGrid[rowIdx][columnIdx + 1] == '1'
                    ):
                    graph.addEdge(coordinate, (rowIdx, columnIdx + 1))
                if (
                    rowIdx + 1 < 128
                    and expandedGrid[rowIdx + 1][columnIdx] == '1'
                    ):
                    graph.addEdge(coordinate, (rowIdx + 1, columnIdx))
                if (
                    columnIdx > 0
                    and expandedGrid[rowIdx][columnIdx - 1] == '1'
                    ):
                    graph.addEdge(coordinate, (rowIdx, columnIdx - 1))

    graph.findRegions()
    print(graph.getRegionCount())


if __name__ == '__main__':
       main()
