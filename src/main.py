'''
Created on 1 Jul 2015

@author: sphinx
'''

from grid import Grid
from cell import Cell
import csv

def SolveGrid(grid):
    loopCount=1
    newGrid = grid.CopyGrid()
    while not grid.isSolved():
        for column in range(1,10):
            for row in range(1,10):
                newCell = newGrid.getCell(row, column)
                if len(newCell.values) is not 1:
                    columnCells = grid.getColumn(column)
                    for cell in columnCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
                    rowCells = grid.getRow(row)
                    for cell in rowCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
                    gridCells = grid.getLocalGrid(row, column)
                    for cell in gridCells:
                        if len(cell.values) is 1:
                            value = cell.values[0]
                            newCell.removeValue(value)
        if grid == newGrid:
            print("This puzzle cannot be solved")
            break;
        else:
            grid = newGrid.CopyGrid()
        loopCount = loopCount+1
    return grid

def ImportGrid(file):
    reader = csv.reader(file)
    grid = Grid()
    rowCount = 1
    for row in reader:
        for column in range(1,10):
            cell = Cell()
            value = row[column-1]
            if value is not "":
                cell.setValues([int(value)])
                grid.setCell(rowCount, column, cell)
        rowCount = rowCount + 1
    return grid
    

if __name__ == '__main__':
    print("Starting Sudoku Solver")
    
    file = open("../demo.csv")
    
    grid = ImportGrid(file)
    
    print("Starting Grid")
    print(grid)
    
    grid = SolveGrid(grid)
        
    print("Final Grid")
    print (grid)
    print("Finishing Sudoku Solver")