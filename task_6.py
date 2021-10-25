a = int(input('Enter the result of the first day '))
b = int(input('Enter the required number of kilometers '))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
else:
    print(day)
