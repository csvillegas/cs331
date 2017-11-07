# matrix class
from random import randint

class Matrix:
    # Initialize n*n matrix with random values -or- all values are val
    def __init__(self, n, val=None):
        self.matrix = []
        self.size = n
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                if val is None:
                    self.matrix[i].append(randint(0, 9))
                else:
                    self.matrix[i].append(val)

    # Splits matrix into 4 submatrices and returns them in a list
    def quarter(self):
        half = self.size // 2
        quarters = [Matrix(half, 0), Matrix(half, 0), Matrix(half, 0), Matrix(half, 0)]
        for i in range(half):
            for j in range(half):
                quarters[0].matrix[i][j] = self.matrix[i][j]
                quarters[1].matrix[i][j] = self.matrix[i][j + half]
                quarters[2].matrix[i][j] = self.matrix[i + half][j]
                quarters[3].matrix[i][j] = self.matrix[i + half][j + half]
        return quarters

    # Matrix Addition
    def __add__(self, other):
        result = Matrix(self.size, 0)
        for i in range(self.size):
            for j in range(self.size):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    # Matrix Subtraction
    def __sub__(self, other):
        result = Matrix(self.size, 0)
        for i in range(self.size):
            for j in range(self.size):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result

    # Matrix Multiplication (standard algorithm)
    def __mul__(self, other):
        result = Matrix(self.size, 0)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def printMatrix(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix]), '\n')