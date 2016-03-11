'''
Created on Nov 28, 2012

@author: mrfish

The idea of this Agent and Environment is to make a step closer to
the Torcs environment.
- The environment is probabilistic
- with a certain probability the agent stays in the current state
- Restart when terminal state is reached
'''

NUMBER_OF_ACTIONS = 7 + 1   # 7 states + terminal state
GOAL_STATE = 6              # at least 7 states
NUMBER_OF_STATES = GOAL_STATE + 1 + 1 #Goal State =6 means 7 states plus terminal 


import ProbabilisticEnvironment.SimpleAgent_web as SimpleAgent
import random
import sys


class SimpleEnvironement:
    def __init__(self):
        ''' matrix with i rows j columns
        i: current state
        j: resulting state if action is executed
        
                        resulting state
                           [[2, 1, 3],
         current state      [3, 3, 3],
                            [2, 1, 3]]
        
        e.g. Executing action 1 in state 2 results in state 1
      
        '''
        self.ProbGotoRandomState = 0.1

        self.EnvironmentMatrix = [[1, 1, 1, 1, 1, 1, 1, 1],
                                  [2, 2, 2, 1, 1, 1, 1, 1],
                                  [3, 3, 3, 1, 1, 1, 1, 1],
                                  [4, 4, 4, 4, 5, 0, 0, 1],
                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                  [4, 4, 4, 6, 6, 6, 6, 1],
                                  [1, 2, 3, 4, 5, 6, 7, 1],  # Goal State
                                  [0, 0, 0, 0, 0, 0, 0, 1]]  # Terminal State
        
        # probability that an action leads to target state
        self.ProbabilityMatrix = [[0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                                  [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]]
        
        self.prevState = 0
        #sys.stdout = open('SimpleRlAgentContinuous.txt', 'w')
        
    
#    def executeAction(self, action):
#        self.prevState = self.EnvironmentMatrix[self.prevState][action]
#        print "Agent is going to state: ", self.prevState
        
    def executeAction(self, action):
        if random.uniform(0,1) < self.ProbabilityMatrix[self.prevState][action]:
            self.prevState = self.EnvironmentMatrix[self.prevState][action]
        print "Agent is going to state: ", self.prevState
    
    def getCurrentState(self):
        return self.prevState
    
    def getNumberOfStates(self):
        return NUMBER_OF_STATES
    
    def getNumberOfActions(self):
        return NUMBER_OF_ACTIONS
    
    
    def GotoRandomState(self, currentNState):
        ''' returns a random state that can be reached'''
        index = random.randint(0, len(self.EnvironmentMatrix)-1 )     
        return self.EnvironmentMatrix[self.prevState][index] 
    
    
    def restart(self):
        self.prevState = 0
        
        
        
if __name__ == '__main__':
    myEnvironment = SimpleEnvironement()
    print myEnvironment.getCurrentState()
    
    mySimpleAgent = SimpleAgent.SimpleAgent(myEnvironment) 
    
    i = 0
    while i < 400:
        if  mySimpleAgent.goalReached:
            mySimpleAgent.reset()
            i += 1
            print "i: ", i            
        mySimpleAgent.Update()


            
            

            
