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
        return self.values.__str__(*args, **kwargs)
    
    def Copy(self):
        newList = list()
        for value in self.values:
            newList.append(value)
        newCell = Cell()
        newCell.setValues(newList)
        return newCell
    
    def setValues(self, values):
        self.values = values
        
    def removeValue(self,value):
        if len(self.values) > 1 and value in self.values:
            self.values.remove(value)


    def __init__(self):
        '''
        Constructor
        '''
        self.values = [1,2,3,4,5,6,7,8,9]