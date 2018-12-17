import random

class Minesweeper:
    def __init__(self):
        self.row_size = int(input("Enter a row size: "))
        self.column_size = int(input("Enter a column size: "))
        self.matrix = [[0] * self.column_size for k in range(self.row_size)]
        self.start_game()

    def create_matrix(self):
        hint = [0, 1, "*"]
        random_hint = random.choice(hint)
        for row in range(self.row_size):
            for column in range(self.column_size):
                random_hint = random.choice(hint)
                self.matrix[row][column] = random_hint
        self.display_matrix(self.matrix)

    def display_matrix(self, matrix):
        for row in matrix:
            for column in row:
                print(column, end="\t")
            print()
        print()

    def set_corners(self, first_side, second_side, current_position):
        counter = 0
        if current_position == "*":
            counter = "*"
        elif (first_side == 1 and second_side == 1) or (first_side == "*" and second_side == "*"):
            counter = 2
        elif (first_side == 1 and second_side == "*") or (first_side == "*" and second_side == 1):
            counter = 2
        elif (first_side == 0 and second_side == "*") or (first_side == 0 and second_side == 1):
            counter = 1
        elif (first_side == "*" and second_side == 0) or (first_side == 1 and second_side == 0):
            counter = 1
        else:
            counter = 0
        return counter

    def set_side_rows(self, left, right, bottom, current_position):
        counter = 0
        if current_position == "*":
            counter = "*"
        elif (left == 1 and right == 1 and bottom == 1) or (left == 1 and right == "*" and bottom == 1):
            counter = 3
        elif (left == 1 and right == "*" and bottom == "*") or (left == 1 and right == 1 and bottom == "*"):
            counter = 3
        elif (left == "*" and right == "*" and bottom == "*") or (left == "*" and right == 1 and bottom == "*"):
            counter = 3
        elif (left == "*" and right == 1 and bottom == 1) or (left == "*" and right == "*" and bottom == 1):
            counter = 3
        elif (left == 1 and right == 1 and bottom == 0) or (left == 0 and right == 1 and bottom == 1):
            counter = 2
        elif (left == "*" and right == "*" and bottom == 0) or (left == "*" and right == 0 and bottom == "*"):
            counter = 2
        elif (left == 0 and right == "*" and bottom == "*") or (left == "*" and right == 1 and bottom == 0):
            counter = 2
        elif (left == "*" and right == 0 and bottom == 1) or (left == 1 and right == "*" and bottom == 0):
            counter = 2
        elif (left == 1 and right == 0 and bottom == "*") or (left == 1 and right == 0 and bottom == 1):
            counter = 2
        elif (left == 0 and right == 1 and bottom == "*") or (left == 0 and right == "*" and bottom == 1):
            counter = 2
        elif (left == 1 or left == "*") or (right == 1 or right == "*") or (bottom == 1 or bottom == "*"):
            counter = 1
        else:
            counter = 0
        return counter

    def get_side_columns(self, top_side, any_side, bottom_side, current_position):
        counter = 0
        if current_position == "*":
            counter = "*"
        elif (top_side == "*" and any_side == "*" and bottom_side == "*") or (top_side == 1 and any_side == "*" and bottom_side == "*"):
            counter = 3
        elif (top_side == "*" and any_side == 1 and bottom_side == "*") or (top_side == "*" and any_side == "*" and bottom_side == 1):
            counter = 3
        elif (top_side == 1 and any_side == 1 and bottom_side == 1) or (top_side == "*" and any_side == 1 and bottom_side == 1):
            counter = 3
        elif (top_side == 1 and any_side == "*" and bottom_side == 1) or (top_side == 1 and any_side == 1 and bottom_side == "*"):
            counter = 3
        elif (top_side == 0 and any_side == "*" and bottom_side == "*") or (top_side == "*" and any_side == 0 and bottom_side == "*"):
            counter = 2
        elif (top_side == "*" and any_side == "*" and bottom_side == 0) or (top_side == 0 and any_side == 1 and bottom_side == 1):
            counter = 2
        elif (top_side == 1 and any_side == 0 and bottom_side == 1) or (top_side == 1 and any_side == 1 and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and any_side == 1 and bottom_side == "*") or (top_side == 1 and any_side == 0 and bottom_side == "*"):
            counter = 2
        elif (top_side == 1 and any_side == "*" and bottom_side == 0) or (top_side == 0 and any_side == "*" and bottom_side == 1):
            counter = 2
        elif (top_side == "*" and any_side == 0 and bottom_side == 1) or (top_side == "*" and any_side == 1 and bottom_side == 0):
            counter = 2
        elif (top_side == "*" and any_side == 0 and bottom_side == 0) or (top_side == 0 and any_side == "*" and bottom_side == 0):
            counter = 1
        elif (top_side == 0 and any_side == 0 and bottom_side == "*") or (top_side == 1 and any_side == 0 and bottom_side == 0):
            counter = 1
        elif (top_side == 0 and any_side == 1 and bottom_side == 0) or (top_side == 0 and any_side == 0 and bottom_side == 1):
            counter = 1
        else:
            counter = 0
        return counter

    def set_side_columns(self, row, column, first_side, second_side, current_position):
        if row == self.row_size - 1:
            return self.set_corners(first_side, second_side, current_position)
        else:
            bottom_side = self.matrix[row+1][column]
            return self.get_side_columns(first_side, second_side, bottom_side, current_position)

    def set_middle_rows(self, top_side, left_side, right_side, bottom_side, current_position):
        counter = 0
        if current_position == "*":
            counter = "*"
        elif (top_side == "*" and left_side == "*" and right_side == "*" and bottom_side == "*") or (top_side == 1 and left_side == "*" and right_side == "*" and bottom_side == "*"):
            counter = 4
        elif (top_side == "*" and left_side == 1 and right_side == "*" and bottom_side == "*") or (top_side == "*" and left_side == "*" and right_side == 1 and bottom_side == "*"):
            counter = 4
        elif (top_side == "*" and left_side == "*" and right_side == "*" and bottom_side == 1) or (top_side == 1 and left_side == 1 and right_side == 1 and bottom_side == 1):
            counter = 4
        elif (top_side == "*" and left_side == 1 and right_side == 1 and bottom_side == 1) or (top_side == 1 and left_side == "*" and right_side == 1 and bottom_side == 1):
            counter = 4
        elif (top_side == 1 and left_side == 1 and right_side == "*" and bottom_side == 1) or (top_side == 1 and left_side == 1 and right_side == 1 and bottom_side == "*"):
            counter = 4
        elif (top_side == 1 and left_side == 1 and right_side == "*" and bottom_side == "*") or (top_side == "*" and left_side == "*" and right_side == 1 and bottom_side == 1):
            counter = 4
        elif (top_side == "*" and left_side == 1 and right_side == "*" and bottom_side == 1) or (top_side == 1 and left_side == "*" and right_side == 1 and bottom_side == "*"):
            counter = 4
        elif (top_side == "*" and left_side == 1 and right_side == 1 and bottom_side == "*") or (top_side == 1 and left_side == "*" and right_side == "*" and bottom_side == 1):
            counter = 4
        elif (top_side == 0 and left_side == "*" and right_side == "*" and bottom_side == "*") or (top_side == "*" and left_side == 0 and right_side == "*" and bottom_side == "*"):
            counter = 3
        elif (top_side == "*" and left_side == "*" and right_side == 0 and bottom_side == "*") or (top_side == "*" and left_side == "*" and right_side == "*" and bottom_side == 0):
            counter = 3
        elif (top_side == 0 and left_side == 1 and right_side == 1 and bottom_side == 1) or (top_side == 1 and left_side == 0 and right_side == 1 and bottom_side == 1):
            counter = 3
        elif (top_side == 1 and left_side == 1 and right_side == 0 and bottom_side == 1) or (top_side == 1 and left_side == 1 and right_side == 1 and bottom_side == 0):
            counter = 3
        elif (top_side == 0 and left_side == "*" and right_side == 1 and bottom_side == 1) or (top_side == 0 and left_side == 1 and right_side == "*" and bottom_side == 1):
            counter = 3
        elif (top_side == 0 and left_side == 1 and right_side == 1 and bottom_side == "*") or (top_side == 0 and left_side == 1 and right_side == "*" and bottom_side == "*"):
            counter = 3
        elif (top_side == 0 and left_side == "*" and right_side == 1 and bottom_side == "*") or (top_side == 0 and left_side == "*" and right_side == "*" and bottom_side == 1):
            counter = 3
        elif (top_side == "*" and left_side == 0 and right_side == "*" and bottom_side == 1) or (top_side == "*" and left_side == 0 and right_side == 1 and bottom_side == 1):
            counter = 3
        elif (top_side == "*" and left_side == 0 and right_side == 1 and bottom_side == "*") or (top_side == 1 and left_side == 0 and right_side == 1 and bottom_side == "*"):
            counter = 3
        elif (top_side == 1 and left_side == 0 and right_side == "*" and bottom_side == "*") or (top_side == 1 and left_side == 0 and right_side == "*" and bottom_side == 1):
            counter = 3
        elif (top_side == "*" and left_side == "*" and right_side == 0 and bottom_side == 1) or (top_side == "*" and left_side == 1 and right_side == 0 and bottom_side == "*"):
            counter = 3
        elif (top_side == "*" and left_side == 1 and right_side == 0 and bottom_side == 1) or (top_side == 1 and left_side == 1 and right_side == 0 and bottom_side == "*"):
            counter = 3
        elif (top_side == 1 and left_side == "*" and right_side == 0 and bottom_side == 1) or (top_side == 1 and left_side == "*" and right_side == 0 and bottom_side == "*"):
            counter = 3
        elif (top_side == "*" and left_side == 1 and right_side == 1 and bottom_side == 0) or (top_side == "*" and left_side == "*" and right_side == 1 and bottom_side == 0):
            counter = 3
        elif (top_side == "*" and left_side == 1 and right_side == "*" and bottom_side == 0) or (top_side == 1 and left_side == "*" and right_side == "*" and bottom_side == 0):
            counter = 3
        elif (top_side == 1 and left_side == 1 and right_side == "*" and bottom_side == 0) or (top_side == 1 and left_side == "*" and right_side == 1 and bottom_side == 0):
            counter = 3
        elif (top_side == "*" and left_side == "*" and right_side == 0 and bottom_side == 0) or (top_side == 1 and left_side == 1 and right_side == 0 and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and left_side == 0 and right_side == "*" and bottom_side == "*") or (top_side == 0 and left_side == 0 and right_side == 1 and bottom_side == 1):
            counter = 2
        elif (top_side == 0 and left_side == "*" and right_side == 0 and bottom_side == "*") or (top_side == 0 and left_side == 1 and right_side == 0 and bottom_side == 1):
            counter = 2
        elif (top_side == "*" and left_side == 0 and right_side == "*" and bottom_side == 0) or (top_side == 1 and left_side == 0 and right_side == 1 and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and left_side == "*" and right_side == 0 and bottom_side == "*") or (top_side == 0 and left_side == 1 and right_side == 0 and bottom_side == 1):
            counter = 2
        elif (top_side == "*" and left_side == 0 and right_side == 0 and bottom_side == "*") or (top_side == 1 and left_side == 0 and right_side == 0 and bottom_side == 1):
            counter = 2
        elif (top_side == 0 and left_side == "*" and right_side == "*" and bottom_side == 0) or (top_side == 0 and left_side == 1 and right_side == 1 and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and left_side == 0 and right_side == "*" and bottom_side == 1) or (top_side == 0 and left_side == 0 and right_side == 1 and bottom_side == "*"):
            counter = 2
        elif (top_side == "*" and left_side == 1 and right_side == 0 and bottom_side == 0) or (top_side == 1 and left_side == "*" and right_side == 0 and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and left_side == "*" and right_side == 0 and bottom_side == 1) or (top_side == 0 and left_side == 1 and right_side == 0 and bottom_side == "*"):
            counter = 2
        elif (top_side == "*" and left_side == 0 and right_side == 1 and bottom_side == 0) or (top_side == 1 and left_side == 0 and right_side == "*" and bottom_side == 0):
            counter = 2
        elif (top_side == 0 and left_side == "*" and right_side == 1 and bottom_side == 0) or (top_side == 0 and left_side == 1 and right_side == "*" and bottom_side == 0):
            counter = 2
        elif (top_side == "*" and left_side == 0 and right_side == 0 and bottom_side == 1) or (top_side == 1 and left_side == 0 and right_side == 0 and bottom_side == "*"):
            counter = 2
        elif (top_side == "*" and left_side == 0 and right_side == 0 and bottom_side == 0) or (top_side == 0 and left_side == "*" and right_side == 0 and bottom_side == 0):
            counter = 1
        elif (top_side == 0 and left_side == 0 and right_side == "*" and bottom_side == 0) or (top_side == 0 and left_side == 0 and right_side == 0 and bottom_side == "*"):
            counter = 1
        elif (top_side == 1 and left_side == 0 and right_side == 0 and bottom_side == 0) or (top_side == 0 and left_side == 1 and right_side == 0 and bottom_side == 0):
            counter = 1
        elif (top_side == 0 and left_side == 0 and right_side == 1 and bottom_side == 0) or (top_side == 0 and left_side == 0 and right_side == 0 and bottom_side == 1):
            counter = 1
        else:
            counter = 0
        return counter

    def start_game(self):
        self.create_matrix()
        total_hint = []
        for row in range(self.row_size):
            another_matrix = []
            for column in range(self.column_size):
                current_position = self.matrix[row][column]
                # upper-left
                if row == 0 and column == 0:
                    right = self.matrix[row][column+1]
                    bottom = self.matrix[row+1][column]
                    another_matrix.append(self.set_corners(right, bottom, current_position))
                # first-row
                elif row == 0 and column != self.column_size - 1:
                    left = self.matrix[row][column-1]
                    right = self.matrix[row][column+1]
                    bottom = self.matrix[row+1][column]
                    another_matrix.append(self.set_side_rows(left, right, bottom, current_position))
                # upper-right
                elif row == 0 and column == self.column_size - 1:
                    left = self.matrix[row][column-1]
                    bottom = self.matrix[row+1][column]
                    another_matrix.append(self.set_corners(left, bottom, current_position))
                # first column
                elif row != 0 and column == 0:
                    top = self.matrix[row-1][column]
                    right = self.matrix[row][column+1]
                    another_matrix.append(self.set_side_columns(row, column, top, right, current_position))
                # last column
                elif row != 0 and column == self.column_size - 1:
                    top = self.matrix[row-1][column]
                    left = self.matrix[row][column-1]
                    another_matrix.append(self.set_side_columns(row, column, top, left, current_position))
                # last-row
                elif row == self.row_size -1 and column != 0:
                    left = self.matrix[row][column-1]
                    right = self.matrix[row][column+1]
                    top = self.matrix[row-1][column]
                    another_matrix.append(self.set_side_rows(left, right, top, current_position))
                # middle
                else:
                    top = self.matrix[row-1][column]
                    left = self.matrix[row][column-1]
                    right = self.matrix[row][column+1]
                    bottom = self.matrix[row+1][column]
                    another_matrix.append(self.set_middle_rows(top, left, right, bottom, current_position))
            total_hint.append(another_matrix)
        self.display_matrix(total_hint)


game = Minesweeper()
