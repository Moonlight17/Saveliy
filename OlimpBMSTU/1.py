s = str(input())
lst = s.split()
R = int(lst[0])
W = int(lst[1])
H = int(lst[2])
n = 1
if (W == H):
    if (((H * W / 4) * (n * 1 + ((n + 1) * (n + 1)))) <= (R * R)):  
        while ((H * W / 16) * (n * n + ((n + 1) * (n + 1)))) <= (R * R):
            n= n+1
    else:
        n = 0
else:
    if ((H * n / 2) * (H * n / 2) + (W * n / 2) * (W * n / 2)) <= (R * R):
        while ((H * n / 2) * (H * n / 2) + (W * n / 2) * (W * n / 2)) <= (R * R):
            n= n+1
    else:
        n = 0
print(n)