def backtracking(t):
    global result
    if len(lst)==n//2:
        lst2 = []
        for i in range(n):
            if i not in lst: lst2.append(i)
        start = 0
        link = 0
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i!=j :
                    start += s[lst[i]][lst[j]]
                    link += s[lst2[i]][lst2[j]]
        a = abs(start - link)
        result = min(result, a)
        # print("start:", start, "link:", link, "result:", result)
        return
    for i in range(t, n):
        if i not in lst:
            lst.append(i)
            backtracking(i)
            lst.pop()

n = int(input())
s = [list(map(int, input().split()))for _ in range(n)]
result = 2000
lst=[]
backtracking(0)
print(result)