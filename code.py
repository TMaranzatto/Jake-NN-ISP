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
        self.bias = 1
        self.value = 0

    def feedforward(self):
        #takes in a vector of inputs v, multiplies each element by the set weight, and adds bias
        v = []
        for i in self.inputs:
            v.append(i.feedforward())
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
        sensbias = sens
        #sensWeights = []
        sensinputVals = []
        for i in range(len(self.weights)):
            #changing the weights respectively
            sensWeight = sens * self.inputs[i].value
            #finding the sensitivity to the input vals
            sensinputVals.append(sens * self.weights[i])
            self.weights[i] -= learningrate * sensWeight
        #easy enough
        self.bias -= sensbias * learningrate
        #calls backprop on previous things
        for i in range(len(self.inputs)):
            self.inputs[i].backprop(sensinputVals[i], learningrate)
            

class sigmoidOp(Op):
    def __init__(self, singleOp):
        self.input = singleOp
        self.value = 0

    def g(self, x):
        #sigmoid function
        return 1/(1+ (math.e) ** (x * -1))

    def dg(self, x):
        #derivitive of sigmoid
        return self.g(x) * (1 - self.g(x))
    
    def feedforward(self):
        #returns the previous nodes output through sigmoid
        self.value = self.g(self.input.feedforward())
        return self.value
    
    def getsens(self, datapoint):
        #assume inputs are already initialized
        #datapoint is a Trainer type
        #simplified for XOR one output
        self.feedforward()
        target = datapoint.desired
        return target - self.value

    
    def backprop(self, sens, learningrate):
        sens = sens * self.dg(self.value)
        self.input.backprop(sens, learningrate)
    
                 
class inputOp(Op):
    def __init__(self):
        self.value = 0

    def setData(self, number):
        self.value = number
        #for XOR

    def feedforward(self):
        #as this is an input node, we only need to return value
        return self.value

    def backprop(self, sensitivity, learningrate):
        pass

class Trainer:
    def __init__(self, x, y, a):
        self.inputs = [x, y]
        self.desired = a

#here we set up an xor network:
        
#setting up data
data00 = Trainer(0,0,0)
data01 = Trainer(0,1,1)
data10 = Trainer(1,0,1)
data11 = Trainer(1,1,0)

#setting up network connections.  i1/i2.value = 0
i1 = inputOp()
i2 = inputOp()
s1 = sumOp([i1, i2])
s2 = sumOp([i1,i2])
p1 = sigmoidOp(s1)
p2 = sigmoidOp(s2)
s3 = sumOp([p1, p2])
p3 = sigmoidOp(s3)

#now we get the sensitivity to the network:
print(p3.feedforward())
#this isnt close to what we want, so we train...

#now we loop and train 4,000 times
#this loop is gonna be ugly... could clean it up later
for i in range(1000):
    #data = 0,0
    i1.setData(0)
    i2.setData(0)
    sens = p3.getsens(data00)
    p3.backprop(sens, 0.01)

    #data = 0,1
    i1.setData(0)
    i2.setData(1)
    sens = p3.getsens(data01)
    p3.backprop(sens, 0.01)

    #data = 1,0
    i1.setData(1)
    i2.setData(0)
    sens = p3.getsens(data10)
    p3.backprop(sens, 0.01)

    #data = 1,1
    i1.setData(1)
    i2.setData(1)
    sens = p3.getsens(data11)
    p3.backprop(sens, 0.01)

#lets test this with different inputs...
i1.setData(0)
i2.setData(0)
print('data = 0,0 output = ' + str(p3.feedforward()))
i1.setData(0)
i2.setData(1)
print('data = 0,1 output = ' + str(p3.feedforward()))
i1.setData(1)
i2.setData(0)
print('data = 1,0 output = ' + str(p3.feedforward()))
i1.setData(1)
i2.setData(1)
print('data = 1,1 output = ' + str(p3.feedforward()))






