import sys

from src.common.calculator import calculator
from src.xutils.xutils import sum_n, sum_n_smart
from src.controller.person_controller import person_list, person_create
from src.controller.pet_controller import pet_list, pet_create, pet_feed, pet_cut_hair



operations = ['Quit', 'List persons', 'List pets', 'Add person', 'Add pet', 'Add pet to person', 'Delete pet form person', 
'Delete person', 'Delete pet', 'List pets for person', 'Cut hair', 'Feed']

persons = ['Juan', 'Miguel', 'Pedro']
for name in persons:
    person_create(name, name+'@email.com')

pets = ['Rambo', 'koky', 'Preto']
for name in pets:
    pet_create(name)

exit = True
while exit:

    try:
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
                print ('%s:' % (operations[oper]))
                if oper == 1:
                    person_list()
                elif oper == 2:
                    pet_list()
                elif oper == 3:
                    name = input('Name ? ')
                    email = input('Email ? ')
                    person_create(name, email)
                elif oper == 4:
                    name = input('Name ? ')
                    pet_create(name)
                elif oper == 5:
                    pass
                elif oper == 6:
                    pass
                elif oper == 7:
                    pass
                elif oper == 8:
                    pass
                elif oper == 9:
                    pass
                elif oper == 10:
                    name = input('Pet ? ')
                    pet_cut_hair(name)
                elif oper == 11:
                    name = input('Pet ? ')
                    pet_feed(name)
                else:
                    pass
    except Exception as e:
        print ('Unexpected error: %s' % (str(e)))


