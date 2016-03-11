'''
Created on Nov 24, 2012

@author: mrfish
'''
import SimpleRLAgentContinuousTransMatrix.RL as RL
import ExtendedDiscreteTransitionMatrix
import math
import random
import numpy
import pickle



MIN_POSITION = -0.9
MAX_POSITION = 0.9


class BaseLevel():
    def __init__(self, numberOfActions, numberOfStates, nextLevel):
        
        self._probabilityMatrix = ExtendedDiscreteTransitionMatrix.ExtendedDiscreteTransitionMatrix(numberOfActions,numberOfStates)
        self._RL = RL.RL(numberOfStates) 
        self._nextLevel = nextLevel
        self._numberOfStates = numberOfStates
        
        self.prevSituation = 0
        self.action = 0
        
        self.currentSituation = 0
        
    def setNextLevel(self, nextLevel):
        self._nextLevel = nextLevel
        
        
    def getNumberOfStates(self):
        return self._numberOfStates
    
   
    def getReachableStates(self, currentNState):
        # can also self._probabilityMatrix[currentNState] be returned?
        return self._probabilityMatrix.getReachableStates(currentNState)
    
    def getCurrentState(self):
        return self.currentSituation
    
       
    def GotoRandomState(self, currentNState):
        ''' returns a random state that can be reached'''
        reachableNStates = self._probabilityMatrix.getReachableStates(currentNState)
        index = random.randint(0, reachableNStates.length())
        return reachableNStates[index]  
    
     
#    def getProbability(self, state, targetState):
#        probability = self._probabilityMatrix[state].getExtendedProbability(targetState)
#        return probability
    
        
    def updateTransition(self, prevState, action, currentState):
        self._probabilityMatrix[prevState].updateProbability(action, currentState)
    
        
    def getBestNextAction(self, currentNstate, reachableStates):
        ''' based on the current N state and the probabilities between reachable N-1
        states calculate the best next N-1 state. Chose N-1 so that N will be best''' 
        return self._probabilityMatrix[currentNstate].CalcBestAction(reachableStates)
        
 
           
    def writeToFile(self, filename):
        # 08072011:
        # Using plotting and pickle together leads to crashes of the script
        # My assumption is that pickle cannot save the object because replot
        # has opened another thread. Plot has to be closed first by calling
        # show() and then pressing Enter. 
        f = open(filename, 'wb')
        pickle.dump(self, f)
        f.close()