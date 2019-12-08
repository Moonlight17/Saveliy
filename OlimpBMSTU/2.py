s = input()
lst = s.split()
a = int(lst[0])
b = int(lst[1])
max = 0
c = list(range(a, b))
c.reverse()
new_mass = []
max_end = 0
for i in c:
    sum_num = 0
    for j in str(i):
        if(int(j) % 2 == 0):
            sum_num = sum_num + int(j)
    if ((sum_num % 3 == 0)and(sum_num!=0)):
        new_mass.append(i)
for i in new_mass:
    sum_all = 0
    for j in str(i):
        sum_all = sum_all + int(j)
    if (sum_all % 4 == 0):
        max_end = i
        break
print(max_end)