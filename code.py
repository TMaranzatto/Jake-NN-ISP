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
        #we randomize this neurons weights and bias
        
        self.inputs = someOps
        self.value = 0
        #input values
        self.invals = None
        self.weights = [random.uniform(-5,5) for _ in range(len(someOps))]
        self.bias = 5
        
    def feedforward(self):
        #takes in a vector of inputs v, multiplies each element by the set weight, and adds bias
        self.invals = [op.feedforward() for op in self.inputs]
        self.value = self.bias + np.dot(self.weights, self.invals)
        return self.value
    

    def backprop(self, sens, learningrate):
        size = len(self.weights)
        sensinputVals = []
        self.bias -= sens * learningrate
        for i in range(size):
            sensWeight = sens * self.inputs[i].value
            sensinputVals.append(sens * self.weights[i])
            self.weights[i] -= learningrate * sensWeight

        #this could be a slowdown, but we need to seperate it
        for i in range(size):
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
        self.feedforward()
        return -(datapoint.desired - self.value)

    #different target function
    #    if target > .5:
    #        return -1 / (self.value)
    #    else:
    #        return 1 / (1 - self.value)
    
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

#helper functions
        
def listinputs(num):
    inputs = []
    for x in range(num):
        inputs.append(inputOp())
    return inputs

def setData(inputOps, datapoint):
    for x in range(len(inputOps)):
        inputOps[x].setData(datapoint.inputs[x])

#setting up data
data00 = Trainer(0,0,0)
data01 = Trainer(0,1,1)
data10 = Trainer(1,0,1)
data11 = Trainer(1,1,0)

learnRate = .5

#setting up network connections.  i1/i2.value = 0
inputs = listinputs(2)

s1 = sumOp(inputs)
s2 = sumOp(inputs)
p1 = sigmoidOp(s1)
p2 = sigmoidOp(s2)
s3 = sumOp([p1, p2])
p3 = sigmoidOp(s3)

#now we get the sensitivity to the network:
#print(p3.feedforward())
#this isnt close to what we want, so we train...

#now we loop and train 4,000 times
#this loop is gonna be ugly... could clean it up later
for i in range(10000):
    #data = 0,0
    setData(inputs, data00)
    sens = p3.getsens(data00)
    p3.backprop(sens, learnRate)

    #data = 0,1
    setData(inputs, data01)
    sens = p3.getsens(data01)
    p3.backprop(sens, learnRate)
 

    #data = 1,0
    setData(inputs, data10)
    sens = p3.getsens(data10)
    p3.backprop(sens, learnRate)
  
    #data = 1,1
    setData(inputs, data11)
    sens = p3.getsens(data11)
    p3.backprop(sens, learnRate)
  
#lets test this with different inputs...
setData(inputs, data00)
print('data = 0,0 output = ' + str(p3.feedforward()))
setData(inputs, data01)
p3.feedforward()
print('data = 0,1 output = ' + str(p3.feedforward()))
setData(inputs, data10)
print('data = 1,0 output = ' + str(p3.feedforward()))
setData(inputs, data11)
print('data = 1,1 output = ' + str(p3.feedforward()))






