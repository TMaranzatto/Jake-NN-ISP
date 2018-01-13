import random
import math
class simplePerceptron:
    #trying to get the hang of the interactions between neurons...
    #perceptrons may help with this
    #this perceptron will be trained to see if a number is above or below a line defined by f(x)
    def __init__(self, n):
        self.weights = [random.uniform(-1,1) for _ in range(n)]
        self.constant = 0.01
        
    def activate(self, number):
        if number > 0:
            return 1
        else:
            return -1
        
    def feedforward(self, inputs):
        summ = 0
        for i in range(len(self.weights)):
            summ += inputs[i] * self.weights[i]

        return self.activate(summ)

    def train(self, inputs, desired):
        guess = feedforward(inputs)
        error = desired - guess
        for i in range(len(self.weights)):
            self.weights[i] += constant * error * inputs[i]

class Trainer:
    def __init__(self, x, y, a):
        self.inputs = [x, y, 1]
        self.answer = a

##################################################################

class Op(object):
    def feedforward(self):
        raise NotImplementedError("you need to implement this")
    
class sumOp(Op):
    def __init__(self, someOps):
        #someOps is the set of Ops inputing to here, should be sigmoid Ops or input Ops
        #c is this neurons bias

        #we randomize this neurons weights and bias
        self.inputs = someOps
        self.weights = [random.uniform(-1,1) for _ in range(len(someOps))]
        self.bias = random.uniform(-1,1)

    def feedforward(self):
        #takes in a vector of inputs v, multiplies each element by the set weight, and adds bias
        v = [self.inputs(i).feedforward() for i in range(len(self.inputs))]
        u = self.constant + sum([a*b for a,b in zip(self.weights, v)])
        return u

    def backprop(self, inputs, desired):
        return None

class sigmoidOp(Op):
    def __init__(self, singleOp):
        self.input = singleOp

    def g(x):
        #sigmoid function
        return 1/(1+math.pow(math.e, x * -1))

    def dg(x):
        #derivitive of sigmoid
        return g(x) * (1 - g(x))
                        
    def feedforward(self):
        #returns the previous nodes output through sigmoid
        return g(singleOp.feedforward())

    def geterror(self, datapoint):
        #assume inputs are already initialized
        #datapoint is a Trainer type
        output = self.feedforward()
        target = datapoint.desired
        return .5 * math.pow(abs(output - target), 2)


                 
class inputOps(Op):
    def __init__(self):
        #inn is a single value
        self.value = None

    def setData(self, file):
        doSomethingWithFile = 0
        #placeholder

    def feedforward(self):
        #as this is an input node, we only need to return value
        return self.value

class Trainer:
    def __init__(self, inputs, desired):
        self.inputs = inputs
        self.desired = desired

def backprop(trainingdata, inputneurons):
    




