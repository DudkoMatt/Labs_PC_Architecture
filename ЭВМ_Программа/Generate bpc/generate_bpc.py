n = int(input("Enter number of lines: "))
k = int(input("Enter first address in hexdecimal: "), 16)
f = int(input("Enter address of first command in hexdecimal: "), 16)
print("Enter commands in hexdecimal each on new line:")

a = []

out = open("out.bpc", "w")

for i in range(n):
    a.append(input().replace(" ", "").replace("+", ""))

print("CMD CK {:0>3X}".format(f), file=out)

for i in range(n):
    print("{:0>3X} {:s}".format(k + i, a[i]), file=out)
