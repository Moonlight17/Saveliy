s = input()
lst = s.split()
n = int(lst[0])
lst.pop(0)
mass = lst
for i in range(len(mass)):
    mass[i] = int(mass[i])
new_mass = []
for i in mass:
    mult = 1
    while i > 0:
        mult = mult * (i%10)
        i = i // 10
    new_mass.append(mult)
maximun_mass = []
result = {i: new_mass.count(i) for i in new_mass}
for i in result:
    maximun_mass.append(result[i])
print(max(maximun_mass))