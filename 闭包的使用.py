# a * x + b = y

def a_line():
    def arg_y():
        return
    return arg_y



def a_line(a, b):
    def arg_y(x):
        return a * x + b

    return arg_y


# a=5 b=9
# x=11 y=?


line1 = a_line(5, 9)
line2 = a_line(12, 8)
print(line1(10))
print(line2(12))




def a_line(a, b):
    return lambda x: a * x + b


line3 = a_line(34, 11)
print(line3(17))
