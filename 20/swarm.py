
class Swarm:
    def __init__(self, positions, velocities, accelerations):
        self.positions = positions
        self.velocities = velocities
        self.accelerations = accelerations
        self.destroyedIndexes = []

    def getManhattanDistance(self, index):
        position = self.positions[index]

        return abs(position[0]) + abs(position[1]) + abs(position[2])

    def getClosestParticleIndex(self):
        closestIndex = None;
        closestDistance = None;

        for index, _ in enumerate(self.positions):
            distance = self.getManhattanDistance(index)
            if not closestDistance or distance < closestDistance:
                closestIndex = index
                closestDistance = distance

        return closestIndex

    def getRemainingParticleCount(self):
        return len(self.positions) - len(self.destroyedIndexes)

    def run(self, times):
        i = 0
        while i < times:
            for index, _ in enumerate(self.velocities):
                self.velocities[index][0] += self.accelerations[index][0]
                self.velocities[index][1] += self.accelerations[index][1]
                self.velocities[index][2] += self.accelerations[index][2]

            for index, _ in enumerate(self.positions):
                self.positions[index][0] += self.velocities[index][0]
                self.positions[index][1] += self.velocities[index][1]
                self.positions[index][2] += self.velocities[index][2]

            positionStrings = []
            for index, position in enumerate(self.positions):
                positionStrings.append('{}_{}_{}'.format(
                    self.positions[index][0],
                    self.positions[index][1],
                    self.positions[index][2]))

            for index, position in enumerate(self.positions):
                if index in self.destroyedIndexes:
                    continue

                positionString = positionStrings[index]
                matchedIndexes = []
                for index2, positionString2 in enumerate(positionStrings):
                    if (index2 != index
                        and positionString2 == positionString):
                        matchedIndexes.append(index2)

                if len(matchedIndexes) > 0:
                    self.destroyedIndexes.append(index)
                    self.destroyedIndexes.extend(matchedIndexes)

            i += 1
