# 类和异常的结合

class Testwith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has a NameError')


with Testwith():
    print('Test is running')
    raise NameError('Test NameError')


