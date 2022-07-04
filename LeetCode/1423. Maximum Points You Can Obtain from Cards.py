List = []
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        length = len(cardPoints)
        summ = 0
        ans = 0
        
        for i in range(length-k, length, 1):
            summ += cardPoints[i]
        ans = summ
        for i in range(length-k+1, length+1, 1):
            summ -= cardPoints[(i-1) % length]
            summ += cardPoints[(i+k-1) % length]
            ans = max(ans, summ)
        
        return ans