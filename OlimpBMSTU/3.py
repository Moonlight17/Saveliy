s = input()
lst = s.split()
a = int(lst[0])
x = int(lst[1])
x = x + 1
b = ""

mass = []
new_mass = []


def per(n):
    b = ""
    x = n
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    for i in range(8):
        if (len(b) % 8 != 0):
            b = "0" + b
        else:
            break
    return b


for i in list(range(a, x)):
    b = per(i)
    mass.append(b)
for i in mass:
    if (int(i) % 2 == 0):
        new_data = i[:-3]
    else:
        new_data = i[2:] + i[:2]
    new_mass.append(new_data)

for i in range(len(new_mass)):
    new_mass[i] = int(new_mass[i], base=2)
print(min(new_mass))
