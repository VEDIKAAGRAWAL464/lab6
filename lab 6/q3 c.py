x = int(input("Enter x: "))
epsilon = float(input("Enter epsilon: "))
n = 2
sum1 = 1

def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1

while True:
    sum2 = 0
    for i in range(1,n+1):
        if i == 1:
            sum2 += -1
        else:
            sum2 += (i%2 == 1 and 1 or -1) * (((x ** (2*i - 2))) / fact(2*i - 2))
    if abs(sum2 - sum1) < epsilon:
        break
    else:
        print(abs(sum2-sum1), sum1, sum2)
        sum1 = sum2

        n += 1

print(sum1,n)
