# -*-coding:utf-8-*-
import threading

# 多线程比多进程更容易通讯，多线程更多用于通讯，如flask，多进程多CPU大量计算场景。
# GIL锁让线程在同一时刻，只能有一个线程运行
# 三个进程，三个CPU，多进程
def task():
    print("扔第二个苹果")


def task2():
    print("扔第三个苹果")


def main():
    # threading.Thread创建了一个线程
    thread1 = threading.Thread(target=task)
    # 让线程执行
    thread1.start()
    thread1.join()
    thread2 = threading.Thread(target=task2)
    thread2.start()
    # 让其他线程等待自己执行完成

    print("扔一个苹果")


if __name__ == '__main__':
    main()
