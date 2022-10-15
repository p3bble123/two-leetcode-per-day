class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child, cookie, happy = 0, 0, 0
        g = sorted(g)
        s = sorted(s)

        while True:
            if child >= len(g) or cookie >= len(s):
                break

            if g[child] <= s[cookie]:
                child += 1
                happy += 1
            cookie += 1

        return happy