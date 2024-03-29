# https://www.lintcode.com/problem/edit-distance/description
# 区间型DP要从最大状态开始想，类似分治。从小到大的DP用循环，从大到小的DP用记忆化搜索

class Solution:    
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
            
        # DP[i][j]: the minimim steps to covert word1[0:i+1] to word2[0:j+1]    
        DP = [[0] * len(word1) for i in word2]
        
        # row
        tmp = 0
        flag = True
        for i in range(len(word2)):
            if word2[i] != word1[0]:
                tmp += 1
                DP[i][0] = tmp
            else:
                if flag:
                    flag = False
                else:
                    tmp += 1
                DP[i][0] = tmp

        # col
        tmp = 0
        flag = True
        for j in range(len(word1)):
            if word1[j] != word2[0]:
                tmp += 1
                DP[0][j] = tmp
            else:
                if flag:
                    flag = False
                else:
                    tmp += 1
                DP[0][j] = tmp



        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if word1[j] != word2[i]:
                    # delete: DP[i-1][j]
                    # insert: DP[i][j-1]
                    # replace: DP[i-1][j-1]
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])+1
                else:
                    DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1])
                    

        return DP[-1][-1]
