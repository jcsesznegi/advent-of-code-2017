def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

class Tablet:
    def __init__(self, instructionStrings, tabletId, sendQueue, receiveQueue):
        self.instructions = self.setInstructions(instructionStrings)
        self.registers = self.setRegisters(tabletId)
        self.sendQueue = sendQueue
        self.receiveQueue = receiveQueue
        self.currentIndex = 0
        self.timesSent = 0

    def isWaiting(self):
        instruction = self.instructions[self.currentIndex]
        return instruction['instructionType'] == 'rcv' and self.receiveQueue.empty()

    def setInstructions(self, instructionStrings):
        instructions = []
        for instructionString in instructionStrings:
            parts = instructionString.split(' ')
            instructionType = parts[0]
            instruction = {'instructionType': instructionType}

            if (instructionType == 'snd'
                or instructionType == 'rcv'):
                instruction['register'] = parts[1]
            elif (instructionType == 'set'
                or instructionType == 'add'
                or instructionType == 'mul'
                or instructionType == 'mod'):
                instruction['register'] = parts[1]
                if is_digit(parts[2]):
                    instruction['value'] = int(parts[2])
                else:
                    instruction['register2'] = parts[2]
            elif instructionType == 'jgz':
                if is_digit(parts[1]):
                    instruction['value'] = int(parts[1])
                else:
                    instruction['register'] = parts[1]
                if is_digit(parts[2]):
                    instruction['offset'] = int(parts[2])
                else:
                    instruction['offsetRegister'] = parts[2]

            instructions.append(instruction)

        return instructions

    def setRegisters(self, tabletId):
        registers = {}
        for instruction in self.instructions:
            if ('register' in instruction
                and not instruction['register'] in registers):
                registers[instruction['register']] = 0
            elif ('register2' in instruction
                and not instruction['register2'] in registers):
                registers[instruction['register2']] = 0
        registers['p'] = tabletId
        return registers

    def getTimesSent(self):
        return self.timesSent

    def getValueOrRegister2(self, instruction):
        return self.registers[instruction['register2']] if 'register2' in instruction else instruction['value']

    def doSend(self, register):
        self.sendQueue.put(self.registers[register])
        self.timesSent += 1
        self.currentIndex += 1

    def doSet(self, instruction):
        value = self.getValueOrRegister2(instruction)
        self.registers[instruction['register']] = value
        self.currentIndex += 1

    def doAdd(self, instruction):
        value = self.getValueOrRegister2(instruction)
        self.registers[instruction['register']] += value
        self.currentIndex += 1

    def doMultiply(self, instruction):
        value = self.getValueOrRegister2(instruction)
        self.registers[instruction['register']] = self.registers[instruction['register']] * value
        self.currentIndex += 1

    def doModulus(self, instruction):
        value = self.getValueOrRegister2(instruction)
        self.registers[instruction['register']] = self.registers[instruction['register']] % value
        self.currentIndex += 1

    def doReceive(self, register):
        if self.receiveQueue.empty():
            return False
        value = self.receiveQueue.get()
        self.registers[register] = value
        self.currentIndex += 1
        return True

    def doJump(self, instruction):
        value = self.registers[instruction['register']] if 'register' in instruction else instruction['value']
        offset = self.registers[instruction['offsetRegister']] if 'offsetRegister' in instruction else instruction['offset']
        if value > 0:
            self.currentIndex += offset
        else:
            self.currentIndex += 1

    def run(self):
        while (self.currentIndex < len(self.instructions)):
            instruction = self.instructions[self.currentIndex]

            if instruction['instructionType'] == 'snd':
                self.doSend(instruction['register'])
            elif instruction['instructionType'] == 'set':
                self.doSet(instruction)
            elif instruction['instructionType'] == 'add':
                self.doAdd(instruction)
            elif instruction['instructionType'] == 'mul':
                self.doMultiply(instruction)
            elif instruction['instructionType'] == 'mod':
                self.doModulus(instruction)
            elif instruction['instructionType'] == 'rcv':
                result = self.doReceive(instruction['register'])
                if not result:
                    break
            elif instruction['instructionType'] == 'jgz':
                self.doJump(instruction)
