n = int(input("enter the number of terms: "))
i = 1
count = 0
fac=1
for i in range(n):
    fac= fac*i
    y = 1/fac
    i += 1
    count += y
print(round(count,9))
