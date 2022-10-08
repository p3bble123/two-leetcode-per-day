class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.removeLosers(0, k, [i+1 for i in range(n)])

        
    def removeLosers(self, curIdx, k, friends):
        # 한 명 밖에 없을 때 승자 반환
        if len(friends) == 1:
            return friends[0]

        # 현재 index에서 k만큼 센 다음 걸린 사람 제거
        curIdx = (curIdx + k - 1) % len(friends)
        del friends[curIdx]

        # 재귀
        self.removeLosers(curIdx, k, friends)
                 
        return friends[0]