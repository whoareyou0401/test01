# import threading
# import time
#
# import os
#
#
#
# def litions(name):
#     for i in range(3):
#         # print("I was listening to %s. %s" % (name, time.ctime()))
#         print("听音乐", name)
#         time.sleep(1)
#
# def singe(name):
#     for i in range(5):
#         # print("I was singe to %s. %s" % (name, time.ctime()))
#         print("唱歌", name)
#         time.sleep(1)
#
#
# class myThread(threading.Thread):  # 继承父类threading.Thread
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         print("Starting " + self.name)
#
#         sale()
#         print( "Exiting " + self.name)
#
# # exitFlag = 0
# #
# # def print_time(threadName, delay, counter):
# #     while counter:
# #
# #         time.sleep(delay)
# #         print("%s: %s" % (threadName, time.ctime(time.time())))
# #
# #         counter -= 1
# lock = threading.Lock()
# num = 100
# def sale():
#     while True:
#         global lock
#         global num
#         lock.acquire()
#         num -= 1
#         print("还有", num)
#         print(threading.currentThread())
#         if num==0:
#             os._exit(0)
#         lock.release()
#         time.sleep(0.3)
#
#
#
# if __name__ == '__main__':
#     # import threading
#     #
#     # lock = threading.Lock()
#     # # Lock对象
#     # lock.acquire()
#     # lock.acquire()
#     # # 产生了死琐。
#     # lock.release()
#     # lock.release()
#     # import threading
#     #
#     # rLock = threading.RLock()
#     # # RLock对象
#     # rLock.acquire()
#     # rLock.acquire()
#     # # 在同一线程内，程序不会堵塞。
#     # rLock.release()
#     # rLock.release()
#     # thread1 = myThread(1, "Thread-1", 1)
#     # thread2 = myThread(2, "Thread-2", 2)
#     # thread3 = myThread(2, "Thread-2", 2)
#     #
#     # # 开启线程
#     # thread1.start()
#     # thread2.start()
#     # thread3.start()
#     # thread2.join()
#     # thread1.join()
#     # thread3.join()
#
#     print("Exiting Main Thread")
#
#     # now = time.time()
#     # r1 = threading.Thread(target=litions, args=("逍遥", ))
#     # r2 = threading.Thread(target=singe, args=("逍遥", ))
#     # # r1.setDaemon(True)
#     # # r2.setDaemon(True)
#     # datas = [r1, r2]
#     # for i in datas:
#     #     i.start()
#
#     # for i in datas:
#     #     i.join()
#     # print("OK")
#     # print(time.time()-now)
#     # litions("sssss")

# from threading import Timer
# def hello():
#   print("hello, world")
# t = Timer(3, hello)
# t.start()
# # t.join()
# print("lll")

# from threading import Thread
# import time
#
#
# def my_counter():
#   i = 0
#   for _ in range(100000000):
#     i = i + 1
#   return True
#
#
# def main():
#   thread_array = {}
#   start_time = time.time()
#   for tid in range(2):
#     t = Thread(target=my_counter)
#     t.start()
#     thread_array[tid] = t
#   for i in range(2):
#     thread_array[i].join()
#   end_time = time.time()
#   print("Total time: {}".format(end_time - start_time))
#
#
# if __name__ == '__main__':
#   main()
#
# from threading import Thread
# import time
#
#
# def my_counter():
#   i = 0
#   for _ in range(100000000):
#     i = i + 1
#   return True
#
#
# def main():
#   thread_array = {}
#   start_time = time.time()
#   for tid in range(2):
#     t = Thread(target=my_counter)
#     t.start()
#     t.join()
#   end_time = time.time()
#   print("Total time: {}".format(end_time - start_time))


# if __name__ == '__main__':
#   main()

# import multiprocessing
#
# def writer_proc(q):
#     try:
#         q.put(1)
#     except:
#         pass
#
# def reader_proc(q):
#     while True:
#       print(q.get())
#
# if __name__ == "__main__":
#     q = multiprocessing.Queue()
#     writer = multiprocessing.Process(target=writer_proc, args=(q,))
#     writer.start()
#
#     reader = multiprocessing.Process(target=reader_proc, args=(q,))
#     reader.start()
#
#     reader.join()
#     writer.join()

# import time
# from multiprocessing.dummy import Pool as ThreadPool
#
#
# #给线程池取一个别名ThreadPool
# def testRun(n):
#   time.sleep(1)
#   print(n, "职工")
#
#
# if __name__ == '__main__':
#   li = [1,2,3,4,5,6,7,8]
#   pool = ThreadPool(3)  # 创建10个容量的线程池并发执行
#   # pool.map(testRun, li)  # pool.map同map用法
#   for i in li:
#       # pool.apply_async(testRun, args=(i, ))
#       pool.apply(testRun, args=(i, ))
#   pool.close()
#   pool.join()

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)

import inspect

def simple_coroutine(a):
    try:
        print('-> start')

        b = yield a
        print('-> recived', a, b)

        c = yield a + b
        print('-> recived', a, b, c)
    except:
        pass

# run
sc = simple_coroutine(5)

next(sc)
try:
    sc.send(6) # 5, 6
    sc.send(7)
except:
    pass

