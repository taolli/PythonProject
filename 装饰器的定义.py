import time

print(time.time())


def i_can_sleep():
    time.sleep(3)


start_time = time.time()
i_can_sleep()
stop_time = time.time()
print('函数运行了% s 秒' % (stop_time - start_time))


def timmer(func):
    def wrapper():
        time.time()
        func()
        time.time()
        print('运行了 % s秒' % (stop_time - start_time))

    return wrapper


@timmer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
