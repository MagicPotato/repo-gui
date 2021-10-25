proceed = int(input('Enter proceed: '))
cost = int(input('Enter cost: '))
if proceed > cost:
    print('The company works with profit.')
    profit = proceed - cost
    rent = profit / proceed
    empl = int(input('Enter the number of employees '))
    for_1_empl = profit / empl
    print(f'For one emploeer: {for_1_empl}')
elif proseed == cost:
    print('The company works at zero.')
else:
    print('The company operates at a loss.')
