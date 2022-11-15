class Solution:
    def romanToInt(self, s: str) -> int:

        # # clean solution
        # romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M': 1000}
        # romanAsInt = 0
        #
        # s = s.replace('IV', 'IIII').replace('IX', 'IIIIIIIII')
        # s = s.replace('XL', 'XXXX').replace('XC', 'XXXXXXXXX')
        # s = s.replace('CD','CCCC').replace('CM','CCCCCCCCC')
        #
        # for roman in s:
        #     romanAsInt += romanDic[roman]
        #
        # return romanAsInt

        # # better performance solution

        def romanToInt(self, s: str) -> int:

            idx, romanAsInt = 0, 0
            romanDic = {'I': 1, 'IV': 4, 'IX': 9,
                        'V': 5,
                        'X': 10, 'XL': 40, 'XC': 90,
                        'L': 50,
                        'C': 100, 'CD': 400, 'CM': 900,
                        'D': 500,
                        'M': 1000}

            while idx < len(s):
                if len(s[idx:]) > 1:
                    if s[idx] + s[idx + 1] in romanDic:
                        romanAsInt += romanDic[s[idx] + s[idx + 1]]
                        idx += 2
                        continue

                romanAsInt += romanDic[s[idx]]
                idx += 1

            return romanAsInt