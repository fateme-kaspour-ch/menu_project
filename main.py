selection = 0
error = False


class Menu:
    def menu(self):
        print("""--------------------\U0001F40D
1. diagram
2. calsalary
3. prime
4. palindrome
5. uppercase_word
6. copy-file
--------------------\U0001F40D""")
        return input("enter your choose number of menu: ")

    # -------------------------------------------------------------------------------------pro1

    def diagram(self):
        global error
        error = True
        s = 0
        a = 0
        p = 3.14

        try:
            while True:
                name = input('Enter your diagram : ')
                if name == 'end':
                    self.menu()
                if name == 'circle':
                    r = int(input('Enter the radius : '))
                    s = p * r * r
                    a = p * r * 2
                    print(
                        'The area of circle is equal to : {} and The circumference of circle is equal to : {}'.format(s,
                                                                                                                      a))
                    break

                elif name == 'square':
                    z_s = int(input('Enter the side : '))
                    s = z_s ** 2
                    a = z_s * 4
                    print(
                        'The area of square is equal to : {} and The circumference of the square is equal to : {}'.format(
                            s, a))
                    break

                elif name == 'rectangle':
                    l = int(input('Enter the length : '))
                    w = int(input('Enter the width : '))
                    s = l * w
                    a = (l + w) * 2
                    print(
                        'The area of the rectangle is : {} and The circumference of the rectangle is : {}'.format(s, a))
                    break
                else:
                    raise ValueError('please enter a valid name')
                error = False
        except (TypeError, ValueError):
            print('please enter a diagram name')

    # -------------------------------------------------------------------------------------pro2

    def calsalary(self):
        global error
        error = True
        try:
            money = [1200030, 1600000, 1165485, 654987, 256413,
                     112215, 654987, 100005, 120036, 300213, 165006, 100254]
            sum = 0
            count = 0
            for e in money:
                sum += e
                count += 1
                average = sum / count
            print("the salary is%4s:%11i,%4sand the avrage is%4s:%10i" %
                  ('    ', sum, '   ', '     ', average))
            error = False
        except ZeroDivisionError:
            print('count can not be zero!!!')

    # -------------------------------------------------------------------------------------pro3

    def prime(self):
        global error
        error = True
        try:
            while True:
                number = int(input('Enter your number : '))
                if number < 2:
                    print('please enter a number more than 1')
                    break
                temp = 0
                for e in range(2, number):
                    if number % e == 0:
                        temp = 1
                        break
                if temp == 0:
                    print(number, 'is prime')
                    break
                else:
                    print(number, 'is not prime')
            error = False
        except ValueError:
            print('Please enter a number')

    # -------------------------------------------------------------------------------------pro4

    def palindrome(self):
        global error
        error = True
        a = ('fafa', 'hami', 'salam', 'lol', 'dire', 'bob', 'non', 'hello')
        try:
            def isPalindrome(a):
                for e in a:
                    if (e == e[::-1]):
                        print(e)

            isPalindrome(a)
            error = False
        except TypeError as e:
            print(e)

    # -------------------------------------------------------------------------------------pro5

    def uppercase_word(self):
        global error
        error = True
        string = 'fatemekaspour'
        try:
            def uppercase(string):
                result = ''
                for e in string:
                    if ord(e) >= 65:
                        result += chr(ord(e) - 32)
                    else:
                        result += chr(ord(e) + 32)
                return result

            print(uppercase(string))
            error = False
        except TypeError as e:
            print('please choose a string')

    # -------------------------------------------------------------------------------------pro6

    def copy_file(self):
        global error
        error = True
        try:
            main_file = input('Enter the name of file : ')
            if main_file[:-1] == '.txt':
                print(main_file)
            else:
                main_file += '.txt'
                print(main_file)
            copy_file = input('Enter the name of the copy file : ') + '.txt'
            if copy_file[:-1] == '.txt':
                print(copy_file)
            else:
                copy_file += '.txt'
                print(copy_file)
            with open(main_file, "r") as fr, open(copy_file, "w") as fw:
                for line in fr:
                    fw.writelines(line)
                    print('file copied')
            error = False
        except FileNotFoundError:
            print('There is no file with this name')


m = Menu()

# -----------------------Running menu
while True:
    if not error:
        selection = f.menu()
    if selection == "1":
        m.diagram()
    elif selection == "2":
        m.calsalary()
    elif selection == "3":
        m.prime()
    elif selection == "4":
        m.palindrome()
    elif selection == "5":
        m.uppercase_word()
        m.menu()
    elif selection == "6":
        m.copy_file()
    elif selection == "end":
        exit()
    else:
        print("Please enter a True number between 1 to 6 ")
