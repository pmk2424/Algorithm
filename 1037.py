# 백준 1037 약수
n = int(input())
a = list(map(int,input().split()))

a_max = max(a)
a_min = min(a)

print(a_max*a_min)