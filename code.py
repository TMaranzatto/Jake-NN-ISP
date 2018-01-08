import random
import math
class simplePerceptron:
    #trying to get the hang of the interactions between neurons...
    #perceptrons may help with this
    #this perceptron will be trained to see if a number is above or below a line
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

        
class sumOpsActive:
    def __init__(self, a, c):
        #a is the number of weights needed.
        #it is the same as the number of neurons in the previous layer
        #c is the neurons bias
        self.weights = [random.uniform(-1,1) for _ in range(a)]
        self.constant = c

    def g(x):
        return 1/(1+math.pow(math.e, x * -1))
        
    def output(self, v):
        #takes in a vector of inputs v, multiplies each element by the set weight, and adds bias
        #then pumps this through g(x) which is standard logistic function
        u = self.constant + sum([sum(x) for x in zip(self.weights, v)])
        return g(u)
    
class inputOps:
    def __init__(self, inn):
        #inn is a single value
        self.value = inn

    def output(self)
        #as this is an input node, we only need to return value
        return self.value
    
# do we need a class outputOps:? I dont think so
class inputLayer:
    def __init__(self, n):
        #n is the number of input nodes
        #we initialize everything with a value of 0
        self.inputs = [inputOps(0) for x in range(n)]
        
        
class hiddenLayer:

class network:







