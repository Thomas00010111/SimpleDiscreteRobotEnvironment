'''
Created on Jun 29, 2013

@author: mrfish
'''
import unittest
import SimpleRLAgentContinuousTransMatrix.RL as RL
import SimpleEnvironment
import numpy

class TestRl(unittest.TestCase):


    def setUp(self):
        NumberOfStates = 5
        self.RL = RL.RL(NumberOfStates)
        
    def test_getRewardedTransitions(self):
        fromState = 3
        toState = 3
        self.assertEqual(self.RL.getRewardedTransitions(fromState, toState), 0)
        
    def test_validPosition(self):
        self.environment = SimpleEnvironment.SimpleEnvironement()
        self.environment.Maze = numpy.array([[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 2, 0],
                                 [0, 0, 0, 0, 0]])
        self.assertTrue(self.environment.isPositionValid(0, 0))
        self.assertTrue(self.environment.isPositionValid(5, 0))
        self.assertFalse(self.environment.isPositionValid(6, 0))
        self.assertTrue(self.environment.isPositionValid(0, 4))
        self.assertFalse(self.environment.isPositionValid(0, 5))
        self.assertFalse(self.environment.isPositionValid(-1, 0))
        self.assertFalse(self.environment.isPositionValid(0, -1))
        
        
    def test_RobotMoving(self):
        self.environment = SimpleEnvironment.SimpleEnvironement()
        self.environment.TransitionProbability = 1.0
        self.environment.executeAction(0)
        self.assertEqual(self.environment.x, 1)
        self.environment.executeAction(3)
        self.assertEqual(self.environment.y, 1)
        self.environment.executeAction(1)
        self.assertEqual(self.environment.y, 0)
        self.environment.executeAction(2)
        self.assertEqual(self.environment.x, 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    