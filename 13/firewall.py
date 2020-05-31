
class Firewall:
    def __init__(self, depths, ranges, delay=0):
        self.firewall = self.setFirewall(depths, ranges)
        self.currentTime = 0
        self.currentDepth = -1
        self.totalSeverity = 0
        self.delay = delay
        self.isCaught = False

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
            self.isCaught = True
            self.totalSeverity += currentRange * self.currentDepth

    def runOnce(self):
        if self.currentTime >= self.delay:
            self.currentDepth += 1
            self.updateSeverity()
        self.currentTime += 1

    def run(self):
        while self.currentDepth < len(self.firewall) - 1:
            self.runOnce()
