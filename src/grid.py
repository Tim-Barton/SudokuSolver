'''
Created on 1 Jul 2015

@author: sphinx
'''

from cell import Cell

class Grid(object):
    '''
    classdocs
    '''    
    
    
    def __str__(self, *args, **kwargs):
        return self.gridList.__str__(*args, **kwargs)
    
    def __eq__(self, grid):
        if isinstance(grid, Grid):
            for row in range(1,10):
                for column in range(1,10):
                    if not self.getCell(row, column) == grid.getCell(row,column):
                        return False
            return True
        return False
    
    def isSolved(self):
        for column in range(0,9):
            for row in range(0,9):
                if len(self.gridList[column][row].values) != 1:
                    return False
        return True
    
    def setCell(self,row, column, cell):
        if row > 10 and column > 10:
            return None
        self.gridList[column-1][row-1] = cell
        
    def getRow(self, row):
        newList= list()
        if row > 10:
            return None
        for i in range(0,9):
            newList.append(self.gridList[i][row-1])
        return newList

    
    def getColumn(self,column):
        return self.gridList[column-1]
    
    def getLocalGrid(self,row,column):
        localGridRow = int((row-1)/3)
        localGridColumn = int((column-1)/3)
        newList = list()
        rowRange = range(localGridRow*3, (localGridRow*3)+3)
        columnRange = range(localGridColumn*3, (localGridColumn*3)+3)
        for localRow in rowRange:
            for localColumn in columnRange:
                newList.append(self.gridList[localColumn][localRow])
        return newList

    def getCell(self,row,column):
        if row < 10 and column < 10:
            return self.gridList[column-1][row-1]
        return None
    
    def __init__(self):
        '''
        Constructor
        '''
        self.gridList = list()
        for i in range(0,9):
            column = list()
            for index in range(0,9):
                cell = Cell()
                column.append(cell)
            self.gridList.append(column)
        