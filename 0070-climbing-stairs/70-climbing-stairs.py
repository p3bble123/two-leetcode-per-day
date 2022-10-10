class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}
        return self.climbOneTwo(0, n, visited)

    def climbOneTwo(self, current, n, visited):
        if current in visited:
            return visited[current]

        if current == n:
            return 1
        if current > n:
            return 0

        result = self.climbOneTwo(current + 1, n, visited) + self.climbOneTwo(current + 2, n, visited)
        # 현재 위치, 현재 위치에서 출발할 경우 경로수 기록
        visited[current] = result

        return result
