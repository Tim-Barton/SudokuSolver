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

if __name__ == '__main__':
    print("Starting Sudoku Solver")
    
    grid = Grid()
    
    gridSetup = [ [1,1,8],
                  [1,5,7],
                  [1,6,9],
                  [1,7,3],
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
        
    print(grid)
    
    while not grid.isSolved():
        newGrid = CopyGrid(grid)
        for column in range(1,10):
            for row in range(1,10):
                newCell = newGrid.getCell(row, column)
                #print(str(column) + ":" + str(row) + "-" + str(newCell))
                columnCells = grid.getColumn(column)
                for cell in columnCells:
                    if len(cell.values) is 1:
                        value = cell.values[0]
                        newCell.removeValue(value)
                rowCells = grid.getColumn(column)
                for cell in rowCells:
                    if len(cell.values) is 1:
                        value = cell.values[0]
                        newCell.removeValue(value)
                gridCells = grid.getLocalGrid(row, column)
                for cell in gridCells:
                    if len(cell.values) is 1:
                        value = cell.values[0]
                        newCell.removeValue(value)
                #print(str(column) + ":" + str(row) + "-" + str(newCell))
                #print(str(column) + ":" + str(row) + "-" + str(newGrid.getCell(row, column)))
        if grid == newGrid:
            break;
        else:
            grid = CopyGrid(newGrid)
        print(grid)
        
    
    print (grid)
    print("Finishing Sudoku Solver")