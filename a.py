n = int(input())
k = int(input())
a = [-1] * n
count = 0

def good(x, pos, k):
    if pos == 0:
        return True
    pred = a[pos - 1]
    # if abs(x - pred) <= k:
    #     return True
    # else:
    #     return False
    return abs(x - pred) <= k

def f(pos, n, k):
    if pos == n:
        global count
        count += 1
       # print(*a)
        return
    for i in range(1, n+1):
        if good(i, pos, k) and i not in a:
           a[pos] = i
           f(pos+1, n, k)
           a[pos] = -1


# вызов в основной программе
f(0, n, k)
print(count)
