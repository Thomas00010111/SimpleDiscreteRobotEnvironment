'''
Created on Nov 24, 2012

@author: mrfish
'''
import SimpleDiscreteRobotEnvironment.RL as RL
import SimpleDiscreteRobotEnvironment.ExtendedDiscreteTransitionMatrix as ExtendedDiscreteTransitionMatrix 


class BaseLevel():
    def __init__(self, numberOfActions, numberOfStates, nextLevel):
        
        self._probabilityMatrix = ExtendedDiscreteTransitionMatrix.ExtendedDiscreteTransitionMatrix(numberOfStates, numberOfActions)
        self._RL = RL.RL(numberOfStates) 
        self.action = 0
        
    def updateTransition(self, prevState, action, currentState):
        self._probabilityMatrix[prevState].updateProbability(action, currentState)
        
    def getBestNextAction(self, currentNstate, reachableStates):
        return self._probabilityMatrix[currentNstate].CalcBestAction(reachableStates)
        