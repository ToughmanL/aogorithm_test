# import sys
# import bisect
#
# line=input()
# line=line.split(' ')
# N=int(line[0])
# M=int(line[1])
# diff_pay={}
# for line in range(N):
#     line=input()
#     line=line.split(' ')
#     if not line:
#         continue
#     diff_pay[int(line[0])]=int(line[1])
# arr=sorted(diff_pay.keys())
# for i in range(len(arr)-1):
#     if diff_pay[arr[i]]>diff_pay[arr[i+1]]:
#         diff_pay[arr[i+1]]=diff_pay[arr[i]]
# line=input()
# abi=map(int,line.split(' '))
# for i in abi:
#     ind=bisect.bisect(arr,i)
#     if ind==0:
#         print (0)
#     else:
#         print (diff_pay[arr[ind-1]])


line=input()
line=line.split(' ')
l=int(line[0])
r=int(line[1])
count=0
for i in range(l,r+1,1):
    if (i+1)*i/2%3==0:
        count+=1
print (count)



