

def lcs_length(x, y):#最长公共子序列
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # i，j位置上的字符匹配的时候，来自于左上方
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    # 逐行打印
    for _ in c:
        print(_)
    return c[m][n]




class solution():
    def solvecombination(self, array, n):
        self.helper(array, n, [])

    def helper(self, array, n, solution):
        if len(solution) == n:
            print(solution)
            return
        for i in range(len(array)):
            newarray = array[i + 1:]  # 创建新的课程列表，更新列表，即选过的课程不能再选
            newsolution = solution + [array[i]]  # 将科目加入新的列表组合
            self.helper(newarray, n, newsolution)


solution().solvecombination(["A", "B", "C", "D"], 2)