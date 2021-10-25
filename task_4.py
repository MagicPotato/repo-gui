num = abs(int(input("Enter number ")))
max = num % 10
while num > 0:
    num = num // 10
    if num % 10 > max:
        max = num % 10
    if num > 9:
         continue
    else:
        print("Maximum is ", max)
    break

