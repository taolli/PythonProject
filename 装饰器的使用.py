def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')

        return nei

    return tips


@new_tips('add_model')
def add(a, b):
    print(a + b)


@new_tips('sub_model')
def sub(a, b):
    print(a + b)


print(add(5, 7))
print(sub(23, 6))
