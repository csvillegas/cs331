# Main Matrix Multiplication Test Program
import time
from matrix import Matrix

def main():
    matrixMultiplicationTest("standard")
    matrixMultiplicationTest("divide & conquer")
    matrixMultiplicationTest("strassen")

# Test Algorithms
def matrixMultiplicationTest(algorithm):
    print(algorithm.upper())
    count = 1
    while count < 15:
        n = pow(2, count)
        A = Matrix(n)
        B = Matrix(n)
        print("Solved Matrix mutiplication of n =", n, " in:")
        options[algorithm](A, B)
        count += 1

# Algorithms
def standardAlgorithm(A, B):
    start_time = time.time()
    A * B
    print(time.time() - start_time, "seconds\n")

def divconAlgorithm(A, B):
    start_time = time.time()
    divideConquer(A, B)
    print(time.time() - start_time, "seconds\n")

def strassenAlgorithm(A, B):
    start_time = time.time()
    strassen(A, B)
    print(time.time() - start_time, "seconds\n")

options = {"standard": standardAlgorithm,
           "divide & conquer": divconAlgorithm,
           "strassen": strassenAlgorithm}

def divideConquer(A, B):
    # Base case (end recursion)
    if A.size == 2:
        return A * B
    # Divide A and B into 4 submatrices
    QA = A.quarter()
    QB = B.quarter()
    # Recursive calls to solve quarter matrices of result matrix C
    C1 = divideConquer(QA[0], QB[0]) + divideConquer(QA[1], QB[2])
    C2 = divideConquer(QA[0], QB[1]) + divideConquer(QA[1], QB[3])
    C3 = divideConquer(QA[2], QB[0]) + divideConquer(QA[3], QB[2])
    C4 = divideConquer(QA[2], QB[1]) + divideConquer(QA[3], QB[3])
    # Copy quarter matrices into result matrix C
    return combineQuarters(C1, C2, C3, C4)

def strassen(A, B):
    # Base case (end recursion)
    if A.size == 2:
        return A * B
    # Divide A and B into 4 submatrices
    QA = A.quarter()
    QB = B.quarter()
    # Recursive calls and additions to solve quarter matrices of result matrix C
    P = strassen(QA[0]+QA[3], QB[0]+QB[3])
    Q = strassen(QA[2]+QA[3], QB[0])
    R = strassen(QA[0], QB[1]-QB[3])
    S = strassen(QA[3], QB[2]-QB[0])
    T = strassen(QA[0]+QA[1], QB[3])
    U = strassen(QA[2]-QA[0], QB[0]+QB[1])
    V = strassen(QA[1]-QA[3], QB[2]+QB[3])
    C1 = P+S-T+V
    C2 = R+T
    C3 = Q+S
    C4 = P+R-Q+U
    # Copy quarter matrices into result matrix C
    return combineQuarters(C1, C2, C3, C4)

def combineQuarters(Q1, Q2, Q3, Q4):
    n = Q1.size
    C = Matrix(2*n, 0)
    for i in range(n):
        for j in range(n):
            C.matrix[i][j] = Q1.matrix[i][j]
            C.matrix[i][j + n] = Q2.matrix[i][j]
            C.matrix[i + n][j] = Q3.matrix[i][j]
            C.matrix[i + n][j + n] = Q4.matrix[i][j]
    return C

main()