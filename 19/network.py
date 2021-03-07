from pprint import pprint
from enum import Enum

class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

class Network:
    def __init__(self, diagramRows):
        self.diagram = self.setDiagram(diagramRows)
        self.currentPosition = self.setCurrentPosition()
        self.currentDirection = Direction.DOWN
        self.route = []
        self.steps = 1

    def setDiagram(self, diagramRows):
        splitRows = []
        for diagramRow in diagramRows:
            splitRows.append(list(diagramRow))
        return splitRows

    def setCurrentPosition(self):
        startIndex = self.diagram[0].index('|')
        return (startIndex, 0)

    def getTraveledRoute(self):
        return ''.join(self.route)

    def getTraveledSteps(self):
        return self.steps

    def getForwardPosition(self):
        if self.currentDirection == Direction.UP:
            return (self.currentPosition[0], self.currentPosition[1] - 1)
        elif self.currentDirection == Direction.DOWN:
            return (self.currentPosition[0], self.currentPosition[1] + 1)
        elif self.currentDirection == Direction.LEFT:
            return (self.currentPosition[0] - 1, self.currentPosition[1])
        elif self.currentDirection == Direction.RIGHT:
            return (self.currentPosition[0] + 1, self.currentPosition[1])

    def getLeftPosition(self):
        if self.currentDirection == Direction.UP:
            return (self.currentPosition[0] - 1, self.currentPosition[1])
        elif self.currentDirection == Direction.DOWN:
            return (self.currentPosition[0] + 1, self.currentPosition[1])
        elif self.currentDirection == Direction.LEFT:
            return (self.currentPosition[0], self.currentPosition[1] + 1)
        elif self.currentDirection == Direction.RIGHT:
            return (self.currentPosition[0], self.currentPosition[1] - 1)

    def getRightPosition(self):
        if self.currentDirection == Direction.UP:
            return (self.currentPosition[0] + 1, self.currentPosition[1])
        elif self.currentDirection == Direction.DOWN:
            return (self.currentPosition[0] - 1, self.currentPosition[1])
        elif self.currentDirection == Direction.LEFT:
            return (self.currentPosition[0], self.currentPosition[1] - 1)
        elif self.currentDirection == Direction.RIGHT:
            return (self.currentPosition[0], self.currentPosition[1] + 1)

    def positionExists(self, position):
        return (position[1] > 0
            and position[1] < len(self.diagram)
            and position[0] > 0
            and position[0] < len(self.diagram[position[1]])
            and self.diagram[position[1]][position[0]] is not ' ')

    def changeDirectionLeft(self):
        if self.currentDirection == Direction.UP:
            self.currentDirection = Direction.LEFT
        elif self.currentDirection == Direction.DOWN:
            self.currentDirection = Direction.RIGHT
        elif self.currentDirection == Direction.LEFT:
            self.currentDirection = Direction.DOWN
        elif self.currentDirection == Direction.RIGHT:
            self.currentDirection = Direction.UP

    def changeDirectionRight(self):
        if self.currentDirection == Direction.UP:
            self.currentDirection = Direction.RIGHT
        elif self.currentDirection == Direction.DOWN:
            self.currentDirection = Direction.LEFT
        elif self.currentDirection == Direction.LEFT:
            self.currentDirection = Direction.UP
        elif self.currentDirection == Direction.RIGHT:
            self.currentDirection = Direction.DOWN

    def getNextPosition(self):
        nextPosition = self.getForwardPosition()
        if self.positionExists(nextPosition):
            return nextPosition

        nextPosition = self.getLeftPosition()
        if self.positionExists(nextPosition):
            self.changeDirectionLeft()
            return nextPosition

        nextPosition = self.getRightPosition()
        if self.positionExists(nextPosition):
            self.changeDirectionRight()
            return nextPosition

        return False

    def run(self):
        hasNextPosition = True

        while hasNextPosition:
            nextPosition = self.getNextPosition()

            if not nextPosition:
                hasNextPosition = False
            else:
                self.currentPosition = nextPosition
                self.steps += 1
                character = self.diagram[nextPosition[1]][nextPosition[0]]
                if character.isalpha():
                    self.route.append(character)
