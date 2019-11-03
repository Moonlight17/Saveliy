#  int -> x*100
#  str -> "Hello x"
#  bool -> "it's not x"
# type()

a = 0
x = False

if (type(a) == int):
	print(a * 100)
elif (type(a) == str):
	print("Hello,", a)
elif (type(a) == bool):
	print("it's not", a)
else:
	print("WHAT is it???", type(a))

if (x):
	print("TRUE")
else:
	print("FALSE")

























a=-10
b=10
c=0
kol = 0

if (a > 0):
	kol = kol + 1
if (b > 0):
	kol = kol + 1
if (c >= 0):
	kol = kol + 1

print("kol =", kol)