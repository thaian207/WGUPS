# An Nguyen
# Student ID 000397742


from datetime import datetime
from truck import Truck

# For the entire program, the Big O is O(N^2) complexity.
# User Interface with menu. Big O is O(N) complexity.
class Main:
    t = Truck()
    t.loadtruck()

    print('-' * 40)
    print('**** WGUPS Delivery Service Project ****')
    print('-' * 40)
    print(' ')
    print('   1. Display All Packages')
    print('   2. Lookup Specific Package')
    print('   3. Print Total Miles')
    print('   4. Exit')
    print(' ')
    userinput = input(' Enter Your Selection From Menu: ')

    while True:
        try:
            if userinput == '1':
                inputtime = input('Please enter a time in format (HH:MM:SS): ')
                currenttime = datetime.strptime(inputtime, '%H:%M:%S')

                for package in range(1, 41):
                    print(t.hashtable.printformat(package, currenttime))

            elif userinput == '2':
                try:
                    inputpack = int(input('Enter Package Number: '))
                    inputtime= input('Enter Time (HH:MM:SS): ')
                    currenttime = datetime.strptime(inputtime, '%H:%M:%S')
                    print(t.hashtable.printformat(inputpack, currenttime))
                except:
                    print("***Invalid Input***")

            elif userinput == '3':
                print('Total: ' + str('{:7.2f}'.format(t.totaldistance)) + ' miles')
                break

            elif userinput == '4':
                print('')
                print('   Goodbye!')
                exit()
            else:
                print("***Invalid Input***")
                exit()
            break
        except:
            break


main = Main()
