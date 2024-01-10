import time
from threading import Thread


# Пишем функции для каждого потока
def thread1_func():
    while True:
        time.sleep(2)
        print("Hello")


def thread2_func():
    while True:
        time.sleep(4)
        print("Привет")


def thread3_func():
    while True:
        time.sleep(6)
        print("Здравствуйте")


t1 = Thread(target=thread1_func)  # В именованный аргумент `target` передаём функцию,
t1.start()                        # которая будет выполнятся в этом потоке.
t2 = Thread(target=thread2_func)
t2.start()
t3 = Thread(target=thread3_func)
t3.start()
