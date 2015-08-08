'''
Created on 1 Jul 2015

@author: sphinx
'''

from grid import Grid
from cell import Cell
import csv
import time

def SolveGridBruteForce(grid):
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

def SolveGridMsgQueue(inputGrid):
    grid = inputGrid.CopyGrid()
    msgQueue = list()
    grid.setQueue(msgQueue)
    for element in msgQueue:
        row = element[0]
        column = element[1]
        value = element[2]
        columnCells = grid.getColumn(column)
        for cell in columnCells:
            cell.removeValue(value);
        rowCells = grid.getRow(row)
        for cell in rowCells:
            cell.removeValue(value)
        gridCells = grid.getLocalGrid(row, column)
        for cell in gridCells:
            cell.removeValue(value)
    return grid

def ImportGrid(file):
    reader = csv.reader(file)
    grid = Grid()
    rowCount = 1
    for row in reader:
        for column in range(1,10):
            cell = Cell(rowCount,column)
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
    
    start = time.time()
    bruteForce = SolveGridBruteForce(grid)
    brute = time.time()
    queued = SolveGridMsgQueue(grid)
    queue = time.time()
          
    output = "Final Brute Force Grid in " + str(brute-start) + " secs"  
    print (output)
    print (bruteForce)
    output = "Final Message Queue Grid in " + str(queue-brute) + " secs"
    print (output)
    print (queued)
    
    if queued == bruteForce:
        print("Same result")
    print("Finishing Sudoku Solver")