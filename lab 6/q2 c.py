n = int(input("enter the number of terms: "))
i = 1
x=1
count = 0
for i in range(n):
    i += 1
    y = (x**i)/i
    count += y
print(f"{count:.9f}")
