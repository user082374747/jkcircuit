class LogicGate:
# creating the overarching class for all logic gates

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name
    # regular naming/labeling stuff that gets carried down the hierarchy

    def getOutput(self):
        print(self.getLabel())
        self.output = self.performGateLogic()
        return self.output
    # there is no such function for the overarching class as each gate will have their own operation 
    # defined here so it gets carried down

class BinaryGate(LogicGate):
# one of the two categories of logic gates
# takes 2 inputs (binary) and encompasses AND and OR

    def __init__(self,n):
        LogicGate.__init__(self, n)
        # initialising the class with the stuff from its parent

        self.pinA = None
        self.pinB = None
        # the two inputs

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
    # the functions that set 0 or 1 for both inputs 

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    # you can get input into a gate from two places: externally, as before, 
    # and from the output of a gate that is connected to that input line


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
        # python And does what an And gate does

class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1
        # same as And gate, but outputs reversed

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0
        # python Or does what an Or gate does

class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 0
        else:
            return 1
         # same as Or gate, but outputs reversed

class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==0:
            return 1
        elif a==0 and b==1:
            return 1
        else:
            return 0
        # the two possibilities that return true, everything else returns false

class XnorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)
    # inheriting everything from its parent

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==0:
            return 0
        elif a==0 and b==1:
            return 0
        else:
            return 1
        # same as XOR gate, but outputs reversed

class UnaryGate(LogicGate):
# the other category of logic gate
# takes 1 category (hence unary) and encompasses NOT

    def __init__(self,n):
        LogicGate.__init__(self,n)
        # just like the binarygate, inheriting things from logicgate

        self.pin = None
        # only 1 input to be set

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()
         # the function that sets this input (either 0 or 1)

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
    # same thing as in the binary gate


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)
        # inheriting everything from its parent

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1
    # if its true, make it false, vice versa

class Power(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)
        # inheriting from the parent due to similar logic
    
    def performGateLogic(self):
        return 1
    # the power source always return 1

class Switch(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)
        self.visited = False
        self.output = None
        # inheriting from the parent due to similar logic
    
    def performGateLogic(self):
        if self.visited == False:
            self.visited = True
            if self.getPin():
                self.output = 1
                return 1
            else:
                self.output = 0
                return 0
        else:
            return self.output
    # returns whatever the input is

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
    # takes two inputs, the from and to

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    # putting the setNextPin into action using the inputs of the from and the to

class JKFlipFlop(BinaryGate):
# the jk flipflop without the clock, 

    def __init__(self, n):
        BinaryGate.__init__(self, n)
        self.q = 0
        self.visited = False
        # takes two inputs, so initialises with the binary gate first

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter J input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter K input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
    # chucked the input stuff from the og binary gate in
    # and changed the text from A and B to J and K so it makes more sense
 
    def performGateLogic(self):
        if self.visited == False:
            self.visited = True
            print('false')
            j = self.getPinA()
            k = self.getPinB()
            if self.q == 0:
                if j == 0:
                    self.q = 0
                elif j == 1:
                    self.q = 1
            elif self.q == 1:
                if k == 0:
                    self.q = 1
                elif k == 1:
                    self.q = 0
            return self.q
        else:
            print('true')
            return self.q
    # the outputs according to the excitement table
    
def main():
    switch = Switch('s')
    power = Power('p')
    agate1 = AndGate('a1')
    agate2 = AndGate('a2')
    ngate1 = NotGate('n1')
    jk1 = JKFlipFlop('jk1')
    jk2 = JKFlipFlop('jk2')
    ngate2 = NotGate('n2')
    agate3 = AndGate('a3')
    c1 = Connector(switch, agate1)
    c2 = Connector(switch, ngate1)
    c3 = Connector(switch, agate2)
    c4 = Connector(jk2, agate1)
    c5 = Connector(agate1, jk1)
    c6 = Connector(ngate1, jk1)
    c7 = Connector(jk1, ngate2)
    c8 = Connector(ngate2, agate2)
    c9 = Connector(agate2, jk2)
    c10 = Connector(power, jk2)
    c11 = Connector(ngate2, agate3)
    c12 = Connector(jk2, agate3)
    print(agate3.getOutput())

main()

