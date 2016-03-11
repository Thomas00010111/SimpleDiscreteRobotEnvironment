'''
Created on Nov 18, 2012

@author: mrfish
'''

import numpy

class RL:
    def __init__(self, numberOfStates):
        self.V = numpy.zeros((numberOfStates,1))
        self.alpha = 0.7
        self.gamma = 0.95
        print "self.alpha = ", self.alpha, "           self.gamma",self.gamma
        
        #save stateRepresentation transitions that were rewarded
        self.rewardedTransitions = numpy.zeros((numberOfStates,numberOfStates),dtype = int)
        
        
    def Update(self, prevState, currentState, reward):
        # Sutton, formula (6.2)
        self.V[prevState] = self.V[prevState] + self.alpha * (reward + self.gamma * self.V[currentState]-self.V[prevState])
        print "V:", self.V
        if reward != 0:
            self.rewardedTransitions[prevState][currentState] += 1 
            
    def UpdateGoalState(self, goalState, vValueVirtualState, reward):
        # the virtual stateRepresentation in which the agent "slides" is never updated,
        # thus always equal 0
        self.V[goalState] = self.V[goalState] + self.alpha * (reward + self.gamma * vValueVirtualState -self.V[goalState])
        #print "UpdateGoalState: V:", self.V
    
    def getVStates(self):
        return self.V
        

    def getV(self, stateRepresentation):
        return self.V[stateRepresentation]
    
    def setV(self, stateRepresentation, value):
        self.V[stateRepresentation] = value
        
    def getRewardedTransitions(self, fromState, toState):
        print "self.rewardedTransitions: ", self.rewardedTransitions
        return self.rewardedTransitions[fromState][toState]

        
    def saveVList(self, filename):
        # write V-values as columns

        filename = filename + '_V_log.csv'
        f = open(filename, 'w')
        print "RL: saving to :", filename
        
        for v in self.V:
            for item in v:
                f.write(str(item) + ";")
            f.write("\n")
        f.close()
            
        
        
        