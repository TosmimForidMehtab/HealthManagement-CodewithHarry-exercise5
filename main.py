import os


def getdate():
    import datetime
    return datetime.datetime.now()


def clean(name, extension):
    file_size = os.path.getsize(name + '-' + extension + '.txt')
    if file_size == 0:
        print("Log is empty")
    else:
        fyle = open(name + '-' + extension + '.txt', 'r+')
        fyle.truncate(0)
        print("All logs cleared.")
        fyle.close()


try:
    def log(k):
        if k == 1:  # For harry
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                value = input("Type...\n")
                with open('harry-ex.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
            elif c == 2:
                value = input("Type...\n")
                with open('harry-food.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
        elif k == 2:  # For Rohan
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                value = input("Type...\n")
                with open('rohan-ex.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
            elif c == 2:
                value = input("Type...\n")
                with open('rohan-food.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
        elif k == 3:  # For Hammad
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                value = input("Type...\n")
                with open('hammad-ex.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
            elif c == 2:
                value = input("Type...\n")
                with open('hammad-food.txt', 'a') as op:
                    op.write(str([str(getdate())]) + ": " + value + '\n')
                print("Successfully written")
        else:
            print('Please enter a valid choice[1-Harry, 2-Rohan, 3-Hammad]')


    def show(k):
        if k == 1:
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                with open('harry-ex.txt') as op:
                    a = op.read()
                    print(a)
            elif c == 1:
                with open('harry-food.txt') as op:
                    a = op.read()
                    print(a)
        elif k == 2:
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                with open('rohan-ex.txt') as op:
                    a = op.read()
                    print(a)
            elif c == 1:
                with open('rohan-food.txt') as op:
                    a = op.read()
                    print(a)
        elif k == 3:
            c = int(input("Enter 1 for exercise and 2 for food: "))
            if c == 1:
                with open('hammad-ex.txt') as op:
                    a = op.read()
                    print(a)
            elif c == 1:
                with open('hammad-food.txt') as op:
                    a = op.read()
                    print(a)
        else:
            print("Invalid input")


    while 'y':
        print("*" * 80)
        print("                  Health management system")
        print("*" * 80)
        inp = int(input("Press 1 to log or Press 2 to display or Press 3 to clear the previous log: "))
        if inp == 1:
            b = int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad: "))
            log(b)
            yn = input("Do you want to continue(y/n): ")
            if yn.lower() == 'y':
                continue
            else:
                break
        elif inp == 2:
            d = int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad: "))
            show(d)
            yn = input("Do you want to continue(y/n): ")
            if yn.lower() == 'y':
                continue
            else:
                break
        elif inp == 3:
            d = input("Enter name (Harry/Rohan/Hammad): ")
            e = input("From which file you want to clear (ex for Exercise and food for Food): ")
            clean(d.lower(), e.lower())
            yn = input("Do you want to continue(y/n): ")
            if yn.lower() == 'y':
                continue
            else:
                break
        else:
            print("Invalid Input")
            yn = input("Do you want to continue(y/n): ")
            if yn.lower() == 'y':
                continue
            else:
                break

except Exception as e:
    print("Invalid Input!")
