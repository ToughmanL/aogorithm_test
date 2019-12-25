

# def lcs_length(x, y):#最长公共子序列
#     m = len(x)
#     n = len(y)
#     c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if x[i - 1] == y[j - 1]:  # i，j位置上的字符匹配的时候，来自于左上方
#                 c[i][j] = c[i - 1][j - 1] + 1
#             else:
#                 c[i][j] = max(c[i - 1][j], c[i][j - 1])
#
#     # 逐行打印
#     for _ in c:
#         print(_)
#     return c[m][n]
#
#
# class solution():
#     def solvecombination(self, array, n):
#         self.helper(array, n, [])
#
#     def helper(self, array, n, solution):
#         if len(solution) == n:
#             print(solution)
#             return
#         for i in range(len(array)):
#             newarray = array[i + 1:]  # 创建新的课程列表，更新列表，即选过的课程不能再选
#             newsolution = solution + [array[i]]  # 将科目加入新的列表组合
#             self.helper(newarray, n, newsolution)
# # solution().solvecombination(["A", "B", "C", "D"], 2)
#
# def checkDifferent(iniString):
#     # write code here
#     if len(iniString) > 256:
#         return False
#     else:
#         asc = [0 for _ in range(256)]
#         for ch in iniString:
#             asc[ord(ch) - ord('0')] += 1
#         for i in asc:
#             if i > 1:
#                 return False
#         return True
# # re=checkDifferent('sdgghdsa')
# # print(re)

def zipString(iniString):
    # write code here
    result=iniString[0]
    count=1
    for i in range(1,len(iniString)):
        if iniString[i]==iniString[i-1]:
            count+=1
        else:
            result+=count
            result+=iniString[i]
            count=1
    result+=str(count)
    if len(result)>len(iniString):
        return iniString
    else:
        return result

def transformImage(self, mat, n):
    # write code here
    if not mat or n <= 0:
        return mat
    start = 0
    end = n - 1
    while start < end:
        tmp = mat[start]
        mat[start] = mat[end]
        mat[end] = tmp
        start += 1
        end -= 1
    for i in range(n):
        for j in range(i, n):
            tmp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = tmp
    return mat