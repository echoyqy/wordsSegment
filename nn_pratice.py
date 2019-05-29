class neuralNetwork:
    # initialise the neural network
    def __int__(self,inputnodes,hiddennodes,outputnodes,learning):
        # set number of nodes in each input, hidden, outputlayer
        self.inodes=inputnodes
        self.hnodes=hiddennodes
        self.onodes=outputnodes
    #     learning rate
        self.lr=learning
        pass

    # train net work
    def train(self):
        pass

    # query the neural nerwork
    def query(self):
        pass
inputnodes=3
hiddennodes=3
outputnodes=3
learning=0.01
n=neuralNetwork(inputnodes,hiddennodes,outputnodes,learning)