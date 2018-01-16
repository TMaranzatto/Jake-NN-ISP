import random
import math
import numpy as np

class Op(object):
    def feedforward(self):
        raise NotImplementedError("you need to implement this")

    def backprop(self, sensitivity, learningrate):
        raise NotImplementedError("you need to implement this")
    
class sumOp(Op):
    def __init__(self, someOps):
        #someOps is the set of Ops inputing to here, should be sigmoid Ops or input Ops
        #c is this neurons bias

        #we randomize this neurons weights and bias
        self.inputs = someOps
        self.weights = [random.uniform(-1,1) for _ in range(len(someOps))]
        self.bias = random.uniform(-1,1)
        self.value = 0

    def feedforward(self):
        #takes in a vector of inputs v, multiplies each element by the set weight, and adds bias
        v = [self.inputs(i).feedforward() for i in range(len(self.inputs))]
        u = self.bias + sum([a*b for a,b in zip(self.weights, v)])
        self.value = u
        return self.value

    def getouts(self):
        outputs = []
        for sigOp in outputs:
            outputs.append(sigOp.feedForward())
        return outputs
    
    def geterror(self, datapoint):
        total = 0
        for i in range(datapoint.desired):
            total += outputs[i].getError(datapoint, i)

        return total

    def backprop(self, sens, learningrate):
        ##not optimized but it should work
        sensbias = sens * 1
        sensWeights = []
        sensinputVals = []
        for i in range(len(self.weights)):
            sensWeights.append(sens * self.inputs[i].value)
            sensinputVals.append(sens * self.weights[i])
            
        self.bias -= sensbias * learningrate
        for i in range(len(self.weights)):
            w -= learningrate * sensWeights[i]

        for i in range(len(inputs)):
            inputs[i].backprop(sensinputVals[i], learningrate)
            

class sigmoidOp(Op):
    def __init__(self, singleOp):
        self.input = singleOp
        self.value = 0

    def g(x):
        #sigmoid function
        return 1/(1+math.pow(math.e, x * -1))

    def dg(x):
        #derivitive of sigmoid
        return g(x) * (1 - g(x))
    
    def feedforward(self):
        #returns the previous nodes output through sigmoid
        self.value = g(singleOp.feedforward())
        return self.value
    
    def getsens(self, datapoint, index):
        #assume inputs are already initialized
        #datapoint is a Trainer type
        output = self.feedforward()
        target = datapoint.desired[index]
        return .5 * (output - target)**2

    
    def backprop(self, sens, learningrate):
        sens = sens * dg(self.value)
        self.input.backprop(sens, learningrate)
    
                 
class inputOps(Op):
    def __init__(self):
        #inn is a single value
        self.value = 0

    def setData(self, file):
        doSomethingWithFile = 0
        #placeholder

    def feedforward(self):
        #as this is an input node, we only need to return value
        return self.value

    def backprop(self, sensitivity, learningrate):
        pass
    




