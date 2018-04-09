from common.calculator import calculator
from xutils.xutils import sum_n, sum_n_smart



operations = ['Quit', 'Sum N', 'Interest', ]
exit = True
while exit:
    print('\n\nList of operations:')
    index =0
    for op in operations:
        print ('%d. %s' % (index, op))
        index = index +1

    oper = int(input('\nOperation ? '))

    if oper == 0:
        exit = False
        print('\nBye!')
    else:
        if len(operations) <= oper:
            print('\nInvalid Operation: %d!' % (oper))
        else:
            print ('%s Calculator:' % (operations[oper]))
            if oper == 1:
                n = int(input('N ?'))
                total = sum_n(n)
                print('\nSum = %d' %total)
            elif oper == 2:
                amount = float(input('Principal amount ? '))
                roi = float(input('Rate of Interest ? '))
                yrs = int(input('Duration (no. of years) ? '))
                
                total = calculator(amount, roi, yrs)
                interest = total - amount
                print('\nInterest = %0.2f' %interest)
            else:
                pass
