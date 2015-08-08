'''
Created on 1 Jul 2015

@author: sphinx
'''



class Cell(object):
    '''
    classdocs
    '''
    def __eq__(self, cell):
        if isinstance(cell, Cell):
            if len(self.values) != len(cell.values):
                return False
            for value in self.values:
                if value not in cell.values:
                    return False
            return True
        return False
        
    def __repr__(self, *args, **kwargs):
        return self.values.__repr__( *args, **kwargs)
    
    def __str__(self, *args, **kwargs):
        retVal = ""
        retVal = retVal + "(" + str(self.row) + ":" + str(self.column) + ") ["
        for i in self.values:
            retVal = retVal + str(i) + ","
        retVal = retVal + "]"
        for i in range(1,10 - len(self.values)):
            retVal = retVal + "  "
        return retVal
    
    def CopyCell(self):
        newList = list()
        for value in self.values:
            newList.append(value)
        newCell = Cell(self.row, self.column)
        newCell.setValues(newList)
        return newCell
    
    def testAndAddToQueue(self):
        if self.msgQueue is not None and len(self.values) is 1:
            self.msgQueue.append([self.row,self.column,self.values[0]])
    
    def setQueue(self, msgQueue):
        self.msgQueue = msgQueue
        self.testAndAddToQueue()
    
    def setValues(self, values):
        self.values = values
        self.testAndAddToQueue()
        
    def removeValue(self,value):
        if len(self.values) > 1 and value in self.values:
            self.values.remove(value)
            self.testAndAddToQueue()


    def __init__(self,row,column):
        '''
        Constructor
        '''
        self.row = row
        self.column = column
        self.msgQueue = None
        self.values = [1,2,3,4,5,6,7,8,9]