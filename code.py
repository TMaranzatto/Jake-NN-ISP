import random
class simplePerceptron:
    #trying to get the hang of the interactions between neurons...
    #perceptrons may help with this
    #this perceptron will be trained to see if a number is above or below a line
    def __init__(self, n):
        self.weights = [random.uniform(-1,1) for _ in range(n)]
        self.constant = 0.01
        print(self.weights)
        
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
    x = [] #placeholder

p = simplePerceptron(3)
point = [10, -2, 1]
result = p.feedforward(point)
print(result)
#class sumOps:
    
#class activationOps:
