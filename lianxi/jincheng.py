import threading
import time

class mop_floor(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print('我要拖地了')
        time.sleep(1)
        print(threading.current_thread().name)
        print('地拖完了')

class heat_up_watrt(threading.Thread):
    def __init__(self,name):
        # 这里传入参数name，就是传入子线程名字
        super().__init__(name=name)
        # 记住这里的格式不能错

    def run(self):
        print('我要烧水了')
        print(self.name)
        print(threading.current_thread().name)
        # 这两个都是打印出当前子线程的名字
        time.sleep(6)
        print('水烧开了')

start_time = time.time()
t1 = mop_floor('啥也不是')
t2 = heat_up_watrt('***我是烧水员***')
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print('总共耗时:{}'.format(end_time-start_time))
if __name__ == "__main__":
    print(__name__)