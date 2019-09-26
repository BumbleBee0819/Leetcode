# https://www.lintcode.com/problem/k-sum/description
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        if len(A) == 1:
            if target == A[0]:
                return 1
            else:
                return 0
                
        if target == 1:
            if k > 1:
                return 0
            if k ==1:
                if 1 in A:
                    return 1
                else:
                    return 0
        
        
        
        
        # no repeat
        # DP[i][j][k]: pick k items from first i items, which sum is j
        DP = [[[0] * (k+1) for i in range(target+1)] for j in A]
        
        
        for i in range(len(A)):
            DP[i][0][0] = 1
        
        
        
        DP[0][A[0]][1] = 1
            
            
            
        for i in range(1, len(A)):
            for j in range(1, target+1):
                for k in range(1, k+1):
                    # not pick this one
                    DP[i][j][k] += DP[i-1][j][k]
                    # pick this one
                    if j >= A[i]:
                        DP[i][j][k] += DP[i-1][j-A[i]][k-1]

        return DP[-1][-1][-1]
