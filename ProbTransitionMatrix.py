

import numpy

UNINITALLIZED = -1

class ProbTransitionMatrix:
    '''
        A matrix which stores the actions that lead from one state to another
    '''
     
    def __init__(self, noOfActions, noOfStates):
        self._noOfStates = noOfStates
        self._noOfActions = noOfActions
        print "Init ", self.getClassName(), " self._noOfActions: ", self._noOfActions, "   self._noOfStates: ", self._noOfStates
        
        # probability to reach a stateRepresentation with a given action
        self._probabilityMatrix = numpy.empty((noOfActions,noOfStates), dtype = float)
        self._probabilityMatrix.fill(0.0)
        
        # count transitions to stateRepresentation s' with action a
        self._transitionMatrix = numpy.empty((noOfActions,noOfStates), dtype = int)
        self._transitionMatrix.fill(0)
                
    def reset(self):
        # probability to reach a stateRepresentation with a given action
        self._probabilityMatrix = numpy.empty(( self._noOfActions,self._noOfStates), dtype = float)
        self._probabilityMatrix.fill(0.0)
        # count transitions to stateRepresentation s' with action a
        self._transitionMatrix = numpy.empty(( self._noOfActions,self._noOfStates), dtype = int)
        self._transitionMatrix.fill(0)
        
    def __str__(self):
        strProbMatrix = str(self._probabilityMatrix.tolist()).replace("], [", "] \n [")
        strTransMatrix = str(self._transitionMatrix.tolist()).replace("], [", "] \n [")
        return "probabilityMatrix:\n" + strProbMatrix + "\n" + "transitionMatrix:\n" + strTransMatrix 
    
    def getProbabilityMatrixAsList(self):
        return self._probabilityMatrix.tolist()
    
    def getRowprobabilityMatrix(self, row):
        return self._probabilityMatrix[row]     
      
    def getNumberOfStates(self):
        return self._noOfStates
    
    def getNumberOfActions(self):
        return self._noOfActions
      
    def updateProbability(self, action, currentState):
        '''To answer the question how often an action lead from prevState to currentState '''
        print "updateProbability: action:" , action, "    currentState: ", currentState
        self._transitionMatrix[action][currentState] += 1
        sumRow = numpy.sum(self._transitionMatrix[action])
        self._probabilityMatrix[action] = self._transitionMatrix[action]/float(sumRow)

        
    def getProbability(self, action, stateRepresentation):
        return self._probabilityMatrix[action][stateRepresentation]

    def getSumActionCalled(self, action):
        return numpy.sum(self._transitionMatrix[action])

    def CalcBestAction(self, stateValues):
        states = self._probabilityMatrix.dot(stateValues)
        return states.argmax()
    
    
    def display(self):
        ''' print numpy array is not possible, there seems to be a bug in array2string function'''
        strProbMatrix = str(self._probabilityMatrix.tolist()).replace("], [", "] \n [")
        strTransMatrix = str(self._transitionMatrix.tolist()).replace("], [", "] \n [")
        print strProbMatrix
        print strTransMatrix

           
    
    def getClassName(self):
        return self.__class__.__name__
        
                      
        