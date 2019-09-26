#https://www.lintcode.com/problem/minimum-adjustment-cost/description

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if len(A) <= 1:
            return 0
        if target < 0:
            return -1
        
            
            
        
        # DP[i][j]: min cost for first i items when the i-th item == j
        # O(A*100*T)
        
        
        DP = [[float('Inf')] * (100+1) for i in A]
        
        # first row
        for j in range(len(DP[0])):
            DP[0][j] = abs(j - A[0])
            



        for i in range(1, len(A)):
            thisA = A[i]
            
            for j in range(len(DP[0])):
                thisB = j
                thisAdjustment = abs(thisA-thisB)
                
                for k in range(0, target+1):
                    if j-k < 0 and j + k >= len(DP[0]):
                        break
                        
                    lastAdjustment = float('Inf')
                    if j-k >= 0:
                        lastAdjustment = min(lastAdjustment, DP[i-1][j-k])
                    if j+k < len(DP[0]):
                        lastAdjustment = min(lastAdjustment, DP[i-1][j+k])
                        
                    DP[i][j] = min(DP[i][j], lastAdjustment+thisAdjustment)
                    
        return min(DP[-1])
                        
                        
                        
# 空间优化
class Solution1:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if len(A) <= 1:
            return 0
        if target < 0:
            return -1
        
            
            
        
        # DP[i][j]: min cost for first i items & the i-th item' val is j
        
        DP = [[float('Inf')] * (100+1) for i in range(2)]
        
        # first row
        for j in range(len(DP[0])):
            DP[0][j] = abs(j - A[0])
            

        for i in range(1, len(A)):
            thisA = A[i]     
            
            for j in range(len(DP[0])):
                # 空间优化时一定要注意每个值每一步都需要更新，不能用default value
                DP[i%2][j] = float('Inf')
                thisB = j
                thisAdjustment = abs(thisA-thisB)
                
                for k in range(target+1):
                    if j-k < 0 and j + k >= len(DP[0]):
                        break
                    
                    lastAdjustment = float('Inf')
                    if j-k >= 0:
                        lastAdjustment = min(lastAdjustment, DP[(i-1)%2][j-k])
                    if j+k < len(DP[0]):
                        lastAdjustment = min(lastAdjustment, DP[(i-1)%2][j+k])
                        
                    DP[i%2][j] = min(DP[i%2][j], lastAdjustment+thisAdjustment)
            

        return min(DP[i%2])
                    
                    
