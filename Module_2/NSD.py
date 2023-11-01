first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
gcd = 0
if first < second:
    gcd = first
else:
    gcd = second

while first%gcd or second%gcd:
    gcd = gcd - 1
    continue
print(gcd)
    