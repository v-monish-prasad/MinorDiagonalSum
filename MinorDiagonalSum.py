def findMinorDiagonalSum(matrix, length):
    minorDiagonalSum = 0

    for i in range(length):
        minorDiagonalSum += matrix[i][length - i - 1]

    return minorDiagonalSum


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    length = len(matrix)

    print(findMinorDiagonalSum(matrix, length))
