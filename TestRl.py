'''
Created on Jun 29, 2013

@author: mrfish
'''
import unittest
import SimpleRLAgentContinuousTransMatrix.RL as RL


class TestRl(unittest.TestCase):


    def setUp(self):
        NumberOfStates = 5
        self.RL = RL.RL(NumberOfStates)
        
    def test_getRewardedTransitions(self):
        fromState = 3
        toState = 3
        self.assertEqual(self.RL.getRewardedTransitions(fromState, toState), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    