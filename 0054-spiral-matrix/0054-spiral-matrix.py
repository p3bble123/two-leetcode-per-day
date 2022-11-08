class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        if len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]

        matrixSize = len(matrix) * len(matrix[0])

        visited = set()
        visited.add((0, 0))

        row, col, = 0, 1
        spiral = [matrix[0][0]]

        while len(spiral) < matrixSize:
            row, col = self.goRight(matrix, visited, row, col, spiral)
            row, col = self.goDown(matrix, visited, row, col, spiral)
            row, col = self.goLeft(matrix, visited, row, col, spiral)
            row, col = self.goUp(matrix, visited, row, col, spiral)

        return spiral

    def goRight(self, matrix, visited, row, col, spiral):
        if (row, col) in visited:
            return row, col

        while True:
            spiral.append(matrix[row][col])
            visited.add((row, col))

            if col + 1 >= len(matrix[0]) or (row, col + 1) in visited:
                return row + 1, col

            col += 1

    def goDown(self, matrix, visited, row, col, spiral):
        if (row, col) in visited:
            return row, col

        while True:
            spiral.append(matrix[row][col])
            visited.add((row, col))

            if row + 1 >= len(matrix) or (row + 1, col) in visited:
                return row, col - 1

            row += 1

    def goLeft(self, matrix, visited, row, col, spiral):
        if (row, col) in visited:
            return row, col

        while True:
            spiral.append(matrix[row][col])
            visited.add((row, col))

            if col - 1 < 0 or (row, col - 1) in visited:
                return row - 1, col

            col -= 1

    def goUp(self, matrix, visited, row, col, spiral):
        if (row, col) in visited:
            return row, col

        while True:
            spiral.append(matrix[row][col])
            visited.add((row, col))

            if row - 1 < 0 or (row - 1, col) in visited:
                return row, col + 1

            row -= 1
