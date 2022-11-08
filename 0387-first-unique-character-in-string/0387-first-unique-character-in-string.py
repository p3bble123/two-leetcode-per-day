class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars, idx = {}, 0

        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = [i]
            else:
                chars[s[i]].append(i)

        values = list(chars.values())

        while idx < len(values):
            if len(values[idx]) > 1:
                values.pop(idx)
            else:
                idx += 1

        if len(values) == 0:
            return -1
        return values[0][0]