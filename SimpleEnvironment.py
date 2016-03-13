'''
- The environment can be made probabilistic
- with a certain probability the agent stays in the current state
- Restart when terminal state is reached
'''

NUMBER_OF_ACTIONS = 4    # 7 states + terminal state

import SimpleDiscreteRobotEnvironment.SimpleAgent_web as SimpleAgent
import random
import numpy
import matplotlib.pyplot as plt


class SimpleEnvironement:
    def __init__(self):
        # start position
        self.x = 0
        self.y = 0
        
        self.TransitionProbability = 1.0 #stay at current position with (1-TransitionProbability)
        
        '''
        0: free space 
        1: wall/obstacle, outside walls are not necessary
        2: goal
        '''
        self.Maze = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 1, 1],
                                 [0, 0, 0, 0, 0, 2, 0],
                                 [0, 0, 0, 0, 0, 0, 0]])
        
        self.state = self.coordToState(self.x, self.y)
        #sys.stdout = open('SimpleRlAgentContinuous.txt', 'w')
        

    def isPositionValid(self, x, y):
        ''' check if position is valid, i.e. agent is outside of the maze and not moving through a wall.'''
        insideMaze = (x < self.Maze.shape[0]) and (x >=0) and (y < self.Maze.shape[1]) and (y>=0)
        if not insideMaze:
            return False
        return not self.Maze[x][y]==1
        
    def executeAction(self, action):
        ''' change x,y position of agent'''
        if random.uniform(0,1) < self.TransitionProbability:
            if action == 0 and self.isPositionValid(self.x+1, self.y):
                self.x+=1
            elif action == 1 and self.isPositionValid(self.x, self.y-1):
                self.y-=1
            elif action == 2 and self.isPositionValid(self.x-1, self.y):
                self.x-=1
            elif action == 3 and self.isPositionValid(self.x, self.y+1):
                self.y+=1
            else:
                print "Unknown Action or Action not valid!!"
        
        # print current position of robot        
        tempPositionRobotMaze = numpy.copy(self.Maze)
        tempPositionRobotMaze[self.x][self.y] = 3
        print "Position: \n", tempPositionRobotMaze
                
        self.state = self.coordToState(self.x, self.y)
    
    def coordToState(self, x, y):
        ''' 2d coordinate to 1d state discriptor'''
        return x*self.Maze.shape[1] + y
    
    def getCurrentState(self):
        return self.state
    
    def getNumberOfStates(self):
        return self.Maze.shape[0] * self.Maze.shape[1] + 1 # + Terminalstate 
    
    def getNumberOfActions(self):
        return NUMBER_OF_ACTIONS
    
    
    def getRandomAction(self):
        ''' returns a random action'''
        return random.randint(0, NUMBER_OF_ACTIONS-1)
    
    def restart(self):
        self.x = 0
        self.y = 0
        self.state = self.coordToState(self.x, self.y)
        
        
        
if __name__ == '__main__':
    myEnvironment = SimpleEnvironement()
    print myEnvironment.getCurrentState()
    
    mySimpleAgent = SimpleAgent.SimpleAgent(myEnvironment) 
    
    i = 0
    while mySimpleAgent.probRandomState >= 0.0:
        if  mySimpleAgent.goalReached:
            mySimpleAgent.reset()
            i += 1
            print "i: ", i            
        mySimpleAgent.Update()
        noStates = myEnvironment.Maze.shape[0] * myEnvironment.Maze.shape[1]
        v = numpy.reshape(mySimpleAgent._RL.getVStates()[0:noStates], myEnvironment.Maze.shape)
        print v
        
    plt.subplot(1, 1, 1)
    c = plt.pcolor(v)
    plt.show()

            
            

            

            
