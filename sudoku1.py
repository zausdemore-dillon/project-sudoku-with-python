import sys, clingo

class SudokuApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")   # load the encoding 
        for f in files:
            ctl.load(f)    # load files that are passed
        if not files:
            ctl.load("-")
        ctl.configuration.solve.models = '1'    # limit to one model
        ctl.ground()    # ground
        ctl.solve()     # solve


clingo.application.clingo_main(SudokuApp())