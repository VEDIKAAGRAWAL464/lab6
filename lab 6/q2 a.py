n = int(input("enter the number of terms: "))
i = 1
count = 0
for i in range(n):
    i += 1
    y = 1/i
    count += y
print(round(count,9))
