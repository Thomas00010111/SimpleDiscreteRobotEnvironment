'''
Created on Nov 28, 2012

@author: mrfish

28/02/2014
Sieht sehr gut aus. Lernt V-Werte.
'''

import random
import SimpleRLAgentContinuousTransMatrix.BaseLevel as BaseLevel
import sys

GOAL_STATE = 6
PREV_GOAL_STATE = GOAL_STATE - 1
TERMINALSTATE = GOAL_STATE + 1


class SimpleAgent(BaseLevel.BaseLevel):
    def __init__(self, environment):
        BaseLevel.BaseLevel.__init__(self, environment.getNumberOfActions(), environment.getNumberOfStates(), environment)
        self.targetState = 0
        self.environment = environment
        self.probRandomState = 1.0
        self.goalReached = False
        
    
    def reset(self):
        self.environment.restart()
        self.goalReached = False  
      

    def Update(self):
        print "--------------------------------------------"

        currentNState = self.environment.getCurrentState()
        
        # we need a matrix on this level to know which action leads where
        #reachableStates = self.environment.getReachableStates()
        
        # 2) get probability that on n-1 level reachableStNUMBER_OF_STATESates is reached
        #probabilities =  self.environment.getProbabilitiesToReach(reachableStates)
        
           
        # 4) which is the best reachableStates  we can reach with the possible actions?
        action = self.getBestNextAction(currentNState, self._RL.getVStates())
        
        print "action: ", action, "    in stateRepresentation: ", currentNState
        
        self.probRandomState -= 0.00002
        if action == -1 or random.uniform(0,1) < self.probRandomState:
            action = self.environment.GotoRandomState(currentNState)
            print "SimpleAgent: RandomAction: ", action, "     self.probRandomState: ", self.probRandomState
        
        if self.probRandomState <= 0.0:
            print "Exit: self.probRandomState: ", self.probRandomState
            sys.exit()
                
#        prob = self.getProbability(curretargetStatentNState, action)
#        print "prob: ", prob
        
        self.environment.executeAction(action)     
        
        prevNState = currentNState
        
        currentNState = self.environment.getCurrentState()
        
        #reward = self.getReward(currentNState)
   
        #print "prevNState: ",prevNState,"   reward: ",reward, "   currentNState: ", currentNState
                   
        self._RL.Update(prevNState, currentNState, 0)    
        self.updateTransition(prevNState, action, currentNState ) 
        
        if currentNState == GOAL_STATE:
            self._RL.Update(currentNState, TERMINALSTATE, 1)
            self.goalReached = True
           

        
    def getReward(self, stateRepresentation):
        if stateRepresentation == GOAL_STATE:
            self.goalReached = True
            reward = 1
        else:
            reward = 0
        print "SimpleAgent: Reward: ", reward    
        return reward
    
           
    
    def getRandomAction(self):
        randAction = random.randint(0, self.environment.getNumberOfStates() -1)            
        print "SimpleAgent: getBestNextAction: Random maxAction = ", randAction
        return randAction
                

                    