'''
Longest Common Subsequence
'''

from util import *

# ===top down===
class LCSTopDown:
    def __init__(self, s1, s2):
        self.memo = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        self.s1 = s1
        self.s2 = s2

    def lcs(self, i=0, j=0):

        # print("in=",(i, j))
        if i > len(self.s1) - 1 or j > len(self.s2) - 1:
            return 0

        if self.memo[i][j] > 0:
            # print("memout=",(i, j))
            return self.memo[i][j]

        if self.s1[i] == self.s2[j]:
            self.memo[i][j] = 1 + self.lcs(i + 1, j + 1)
        else:
            self.memo[i][j] = max(self.lcs(i+1, j), self.lcs(i, j+1))

        # print("out=",(i, j))
        return self.memo[i][j]

    def get_final_str(self):
        dp = self.memo
        row = 0
        col = 0
        res = ""
        while row < len(self.s1) and col < len(self.s2):
            if dp[row][col] == dp[row + 1][col]:
                row += 1
            elif dp[row][col] == dp[row][col + 1]:
                col += 1
            elif dp[row][col] == dp[row + 1][col + 1] + 1:
                res += self.s1[row]
                row += 1
                col += 1
            else:
                raise Exception()


        return res


# ===bottom up===
def lcs(s1, s2):
    # initialize dp
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                # using diagonal value
                # res+=s1[i-1] - can't do it here, as abcdaf and bcbcf will have two matches of b
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # using up value or left value
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1], dp


def get_final_str(dp, s1, s2):
    row = len(s1)
    col = len(s2)
    res = ""
    while row > 0 and col > 0:

        if dp[row][col] == dp[row - 1][col]:
            row -= 1
        elif dp[row][col] == dp[row][col - 1]:
            col -= 1
        elif dp[row][col] == dp[row - 1][col - 1] + 1:
            res = s1[row - 1] + res
            row -= 1
            col -= 1
        else:
            raise Exception()

    return res


# ===bottom up (with string)===
def lcs_withstring(s1, s2):
    dp = [["" for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                    # using diagonal value + current value
                dp[i][j] = dp[i - 1][j - 1] + s1[i-1]
            else:
                # using max of up value or left value
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    cs = dp[-1][-1]
    return len(cs), cs,dp

if __name__ == '__main__':
    #===simple test===
    s1="abcd"
    s2="bd"
    print("bottom up lcs: ")
    length, dp = lcs(s1, s2)
    final_str = get_final_str(dp, s1, s2)
    print2DArray(dp)
    print((length, final_str))

    print("bottom up lcs (dp store string):")
    length, final_str, dp = lcs_withstring(s1, s2)
    print2DArray(dp)
    print((length, final_str))

    l = LCSTopDown(s1, s2)
    print("top down lcs:")
    res = l.lcs()
    print2DArray(l.memo)
    print((res, l.get_final_str()))


    #===more tests===
    for s1, s2 in [
        ("hello", "helo"),  # , # (3, 'bcf')
        ("hello","elo"), # (4, 'abcf')
        ("hello","hel"),
        ("",""), #(0, '')
        ("e",""), #(0, '')
        ("e","o"),# (3, 'abc')
    ]:
        print("String to resolve '{}', '{}'".format(s1, s2))
        length, dp = lcs(s1, s2)
        final_str = get_final_str(dp, s1, s2)
        print("bottom up lcs: ")
        print("dp=")
        print2DArray(dp)
        print((length, final_str))
        print()

        print("bottom up lcs (dp store string):")
        length, final_str, dp = lcs_withstring(s1, s2)
        print("dp=")
        print2DArray(dp)
        print((length, final_str))
        print()

        l = LCSTopDown(s1, s2)
        print("top down lcs:")
        print("dp=")
        res=l.lcs()
        print2DArray(l.memo)
        print((res, l.get_final_str()))

        print("=========================")
