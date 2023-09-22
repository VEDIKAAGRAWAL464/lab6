num=int(input("enter the number:"))
i=1
total=0
while i<=num:
    total+=(1/2)**i
    i+=1
print("the sum of the series is:",total)