def f(x, i, a):
    l = i + 1
    r = len(a) - 1
    ans = i
    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    return ans - i


def solve():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        u = f(r - a[i], i, a)
        v = f(l - a[i] - 1, i, a)
        ans += u - v
    print(ans)


T = int(input())
for _ in range(T):
    solve()
