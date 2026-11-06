from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for row in range(1, 10):
            if row > 1:
                # empty line before row 4 and row 7, newline otherwise
                if (row - 1) % 3 == 0:
                    s += "\n\n"
                else:
                    s += "\n"
            for column in range(1, 10):
                if column > 1:
                    # two blank spaces before columns 4 and 7, one space otherwise
                    if (column - 1) % 3 == 0:
                        s += "  "
                    else:
                        s += " "
                s += str(self.sudoku[(row, column)])
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        # loop over the shown symbols of the model
        for symbol in model.symbols(shown=True):
            # only handle sudoku(Row, Col, Value) atoms
            if symbol.name != "sudoku" or len(symbol.arguments) != 3:
                continue
            # convert each clingo Number to a Python int
            row, col, value = symbol.arguments
            sudoku[(row.number, col.number)] = value.number
        return cls(sudoku)
