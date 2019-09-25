https://www.lintcode.com/problem/interleaving-string/description

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if (len(s3) != len(s1)+len(s2)):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
            
            
            
            
        # row: S2
        # col: S1
        DP = [[False] * (len(s1)+1) for i in range(len(s2)+1)]
        
        # first row:
        for j in range(1, len(s1)+1):
            if s1[j-1] == s3[j-1]:
                DP[0][j] = True
            else:
                break
            
        # first col:
        for i in range(1, len(s2)+1):
            if s2[i-1] == s3[i-1]:
                DP[i][0] = True
            else:
                break
            
            
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if s1[j-1] == s3[i+j-1]:
                    DP[i][j] = (DP[i][j-1] or DP[i][j])
                if s2[i-1] == s3[i+j-1]:
                    DP[i][j] = (DP[i-1][j] or DP[i][j])

        return DP[-1][-1]
                
                
            
            
        
