'''
Created on Nov 28, 2012

@author: mrfish

28/02/2014
Sieht sehr gut aus. Lernt V-Werte.
'''

import random
import SimpleDiscreteRobotEnvironment.BaseLevel as BaseLevel

GOAL_STATE = 40
TERMINALSTATE =  49
REWARD = 1


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
        
        action = self.getBestNextAction(currentNState, self._RL.getVStates())
        
        print "action: ", action, "    in stateRepresentation: ", currentNState
        
        self.probRandomState -= 0.00006
        if action == -1 or random.uniform(0,1) < self.probRandomState:
            action = self.environment.getRandomAction()
            print "SimpleAgent: RandomAction: ", action, "     self.probRandomState: ", self.probRandomState
                
        self.environment.executeAction(action)     
        
        prevNState = currentNState
        
        currentNState = self.environment.getCurrentState()
                   
        self._RL.Update(prevNState, currentNState, 0)    
        self.updateTransition(prevNState, action, currentNState ) 
        
        if currentNState == GOAL_STATE:
            self._RL.Update(GOAL_STATE, TERMINALSTATE, REWARD)
            self.goalReached = True
           

    
                

                    