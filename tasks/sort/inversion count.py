def merge(a, b):
    c = 0
    n, m = len(a), len(b)
    i, j = 0, 0
    l = []
    while i < n and j < m:
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            c += n-i
            l.append(b[j])
            j += 1
    if i < n:
        l += a[i:]
    else:
        l += b[j:]
    return l, c
c = 0
def merge_sort(l):
    global c
    if len(l) <= 1:
        return l
    ll, c1 = merge(merge_sort(l[:len(l) // 2]), merge_sort(l[len(l) // 2:]))
    c += c1
    return ll
# print(merge_sort([1, 3, 2, 4, 5, 2, 10, 1]))
# print(c)
#



# def quick_sort(l):
#     if len(l) <= 1:
#         return l
#     mx = l[len(l) // 2]
#     le, m, r = [], [], []
#     for i in l:
#         if mx < i:
#             r.append(i)
#         elif mx == i:
#             m.append(i)
#         else:
#             le.append(i)
#     return quick_sort(le) + m + quick_sort(r)
# print(quick_sort([10, 7, 8, 9, 1, 5]))
#
#
#
#
#




# s = 'RGB'
# for _ in range(int(input())):
#     # 3 3 3
#     # RGBGBRBRGRGB
#     # 2 4 5
#     # R B G B G B G B G B R
#     # 2 5 5
#     # R B G B G B G B G B G R
#     # 3 5 5
#     # R B G B G B G R G B G B R
#     # 3 5 5
#     # b g b g r g b g b r b r g
#     # 2 4 5
#     # b g b g b r b g
#     # 2 4 6
#     # b g b g
#     # 4 6 8
#     # b g b g r g b g r g b g r g b g b r
#     r, g, b = map(int, input().split())
#     m1, m2, m3 = sorted([r, g, b])
#     c = [r, g, b]
#     maxs = ''
#     if m3 > m1+m2+1:
#         s1 = s[c.index(m3)]
#         curs = s1
#         m11 = c.index(m1)
#         m22 = c.index(m2)
#         m33 = c.index(m3)
#         c[m11] -= 1
#         for i in range(m1+m2):
#
#     for i in range(3):
#         if c[i] == 0:
#             continue
#         for j in range(3):
#             if c[j] == 0:
#                 continue
#             if i == j:
#                 continue
#             curs = s[i] + s[j]
#             newc = c[:]
#             newc[i] -= 1
#             newc[j] -= 1
#             while True:
#                 n = curs[-1]
#                 if len(curs) >= 3:
#                     n3 = s[-3]
#                 else:
#                     n3 = 1000
#                 maxk = [-1, 0]
#                 for k in range(3):
#                     myk = s[k]
#                     if newc[k] != 0 and myk != n3 and myk != n:
#                         if maxk[1] < newc[k]:
#                             maxk = [k, newc[k]]
#                 if maxk[0] == -1:
#                     break
#                 curs += s[maxk[0]]
#                 newc[maxk[0]] -= 1
#             if len(curs) > len(maxs):
#                 maxs = curs
#     if c.count(0) == 2:
#         maxs = s[c.index(max(c))]
#     print(maxs)
