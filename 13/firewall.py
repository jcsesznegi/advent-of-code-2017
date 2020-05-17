
class Firewall:
    def __init__(self, depths, ranges):
        self.firewall = self.setFirewall(depths, ranges)
        self.currentTime = 0
        self.currentDepth = -1
        self.totalSeverity = 0

    def setFirewall(self, depths, ranges):
        firewall = [None] * (max(depths) + 1)
        for index, depth in enumerate(depths):
            firewall[depth] = ranges[index]
        return firewall

    def updateSeverity(self):
        if not self.firewall[self.currentDepth]:
            return

        currentRange = self.firewall[self.currentDepth]
        if self.currentTime % ((currentRange - 1) * 2) == 0:
            self.totalSeverity += currentRange * self.currentDepth

    def runOnce(self):
        self.currentDepth += 1
        self.updateSeverity()
        self.currentTime += 1

    def run(self):
        while self.currentTime < len(self.firewall):
            self.runOnce()
