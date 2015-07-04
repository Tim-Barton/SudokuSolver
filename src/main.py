'''
Created on 1 Jul 2015

@author: sphinx
'''

from grid import Grid

def CopyGrid(src):
    dst = Grid()
    for row in range(1,10):
        for column in range(1,10):
            cell = src.getCell(row,column)
            if cell is None:
                return None
            dst.setCell(row,column,cell.Copy())
    return dst

def SolveGrid(grid):
    loopCount=1
    while not grid.isSolved():
        newGrid = CopyGrid(grid)
        #print("Loop " + str(loopCount) + " Start")
        #print(grid)
        #print(newGrid)
        for column in range(1,10):
            for row in range(1,10):
                newCell = newGrid.getCell(row, column)
                if len(newCell.values) is not 1:
                    #print(str(column) + ":" + str(row) + "-" + str(newCell))
                    columnCells = grid.getColumn(column)
                    for cell in columnCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
                    #print("Column: " + str(columnCells))
                    #print(str(column) + ":" + str(row) + "-" + str(newCell))
                    #wait = input()
                    rowCells = grid.getRow(row)
                    for cell in rowCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
                    #print("Row: " + str(rowCells))
                    #print(str(column) + ":" + str(row) + "-" + str(newCell))
                    #wait = input()
                    gridCells = grid.getLocalGrid(row, column)
                    for cell in gridCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
                    #print("Grid: " + str(gridCells))
                    #print(str(column) + ":" + str(row) + "-" + str(newCell))
                    #wait = input()
                    #print(str(column) + ":" + str(row) + "-" + str(newCell))
                    #print(str(column) + ":" + str(row) + "-" + str(newGrid.getCell(row, column)))
        #print("Loop " + str(loopCount) + " End")
        #print(grid)
        #print(newGrid)
        if grid == newGrid:
            print("This puzzle cannot be solved")
            break;
        else:
            grid = CopyGrid(newGrid)
        loopCount = loopCount+1
        #wait = input()
    return grid
    

if __name__ == '__main__':
    print("Starting Sudoku Solver")
    
    grid = Grid()
    
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
    
    for number in gridSetup:
        cell = grid.getCell(number[0], number[1])
        cell.setValues([number[2]])
        
    print("Starting Grid")
    print(grid)
    
    grid = SolveGrid(grid)
        
    print("Final Grid")
    print (grid)
    print("Finishing Sudoku Solver")