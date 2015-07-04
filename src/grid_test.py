'''
Created on 4 Jul 2015

@author: sphinx
'''
import unittest
from grid import Grid
from cell import Cell


class Test(unittest.TestCase):


    def setUp(self):
        self.grid = Grid()
        for row in range(1,10):
            for column in range(1,10):
                cell = Cell()
                cell.setValues([row,column])
                self.grid.setCell(row, column, cell)
        print(self.grid)

    def tearDown(self):
        pass

    def testGetRow(self):
        for row in range(1,10):
            thisRow = self.grid.getRow(row)
            for cell in thisRow:
                self.assertEqual(cell.values[0], row, "Row Unequal")

    def testGetColumn(self):
        for column in range(1,10):
            thisColumn = self.grid.getColumn(column)
            for cell in thisColumn:
                self.assertEquals(cell.values[1], column, "Column Unequal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetColumn']
    unittest.main()