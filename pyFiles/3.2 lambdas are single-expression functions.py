"""If you find yourself doing anything remotely complex with lambda expressions,
consider defining a standalone function with a proper name instead
"""
#region
def number1():
    add = lambda x, y: x + y
    print(add(5, 3))
    def the_same_as_above_but_verbose(a, b):
        return a + b

def number2():
    print((lambda x, y: x + y)(5, 3))
#endregion
#region lambdas you can use
def number3():
    tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
    print(sorted(tuples, key=lambda x: x[1]))
    print(sorted(range(-5, 6), key=lambda x: x * x))

def number4():
    def make_adder(n):
        return lambda x: x + n
    plus_3 = make_adder(3)
    print(plus_3(4))
#endregion

#region Harmful and better ways to implement lambda
def number5():
    def harmful():
        print(list(filter(lambda x: x % 2 == 0, range(16))))
    def better():
        print([x for x in range(16) if x % 2 == 0])
    harmful()
    better()
#endregion


user_choice = int(input())
if user_choice == 1:
    number1()
if user_choice == 2:
    number2()
if user_choice == 3:
    number3()
if user_choice == 4:
    number4()
if user_choice == 5:
    number5()
