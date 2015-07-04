'''
Created on 4 Jul 2015

@author: sphinx
'''
import unittest
from grid import Grid

#hard coded puzzle from sudoku.com.au (1st July 2015)
gridSetup = [ [1,1,8],
              [1,6,7],
              [1,7,9],
              [1,8,3],
              [2,1,4],
              [2,3,1],
              [2,4,5],
              [2,9,2],
              [3,3,2],
              [3,5,6],
              [3,6,1],
              [3,8,7],
              [4,5,7],
              [4,6,4],
              [4,7,2],
              [4,8,6],
              [4,9,7],
              [5,3,3],
              [5,7,5],
              [6,1,2],
              [6,2,4],
              [6,3,6],
              [6,4,9],
              [6,5,8],
              [7,2,5],
              [7,4,1],
              [7,5,9],
              [7,7,3],
              [8,1,1],
              [8,6,3],
              [8,7,8],
              [8,9,6],
              [9,2,9],
              [9,3,8],
              [9,4,4],
              [9,9,7]]


class Test(unittest.TestCase):

    def setUp(self):
        self.grid = Grid()        
        for number in gridSetup:
            cell = self.grid.getCell(number[0], number[1])
            cell.setValues([number[2]])


    def tearDown(self):
        pass


    def testSolveGrid(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSolveGrid']
    unittest.main()