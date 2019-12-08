# s = input()
# lst = s.split()
# n = int(lst[0])
# k = int(lst[1])
# m = int(lst[2])
n = 3
k = 1
m = 1


start = 10 ** n - 1
end = 10 ** (n - 1) - 1
print(*range(start, end, -2))



# print(int("115", base=9))
# print(int("11021", base=3))




def per_3(n):
    b = ""
    x = n
    while n > 0:
        b = str(n % 3) + b
        n = n // 3

    return b

def per_9(n):
    b = ""
    x = n
    while n > 0:
        b = str(n % 9) + b
        n = n // 9

    return b

b = per_3(95)
a = per_9(95)