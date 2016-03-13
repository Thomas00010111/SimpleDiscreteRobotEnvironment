'''
Created on Nov 18, 2012

@author: mrfish
'''

import SimpleDiscreteRobotEnvironment.ProbTransitionMatrix as ProbTransitionMatrix

UNINITALLIZED = -1

class ExtendedDiscreteTransitionMatrix:
    '''
        A matrix which stores the actions that lead from one state to another
    '''  
    def __init__(self, noOfStates, noOfActions):
        self._noOfActions = noOfActions
        self._noOfStates = noOfStates
        self.transitionMatrices = []
        for i in range(0,noOfStates):
            m = ProbTransitionMatrix.ProbTransitionMatrix(noOfActions, noOfStates)
            self.transitionMatrices.append(m)
                               
    def __getitem__(self, stateRepresentation):
        ''' Transition probabilities of a stateRepresentation can be accessed with 
        the [] operator, e.g. extendedDiscreteTransitionMatrix[stateRepresentation]'''
        assert(stateRepresentation < len(self.transitionMatrices)), "stateRepresentation: " + str(stateRepresentation) + "    len(self.transitionMatrices):" + str(len(self.transitionMatrices))
        return self.transitionMatrices[stateRepresentation]        
    
    def getNumberOfActions(self):
        return self._noOfActions
    
    def getNumberOfStates(self):
        return self._noOfStates
    
    def getClassName(self):
        return self.__class__.__name__
    
    def saveMatrizes(self, filename):
        for i in range(0,self._noOfStates):
            self.transitionMatrices[i].saveToFile(filename + str(i))
            
    def getReachableStates(self,currentState):
        return self.transitionMatrices[currentState].getReachableStates()
            
    def reset(self):
        [i.reset() for i in self.transitionMatrices]

        
        
    

       

        
            
    


                    
    
        