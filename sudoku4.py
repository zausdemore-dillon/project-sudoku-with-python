import sys, clingo
from sudoku_board import Sudoku

class SudokuApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")   # load the encoding 
        for f in files:
            ctl.load(f)    # load files that are passed
        if not files:
            ctl.load("-")
        ctl.ground()    # ground
        ctl.solve()     # solve
    
    def print_model(self, model, printer):
        print(Sudoku.from_model(model))

clingo.application.clingo_main(SudokuApp())