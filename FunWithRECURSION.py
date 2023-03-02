import time


def message():
    print("Hello World")
    time.sleep(1)
    message1()


def message1():
    print("Hello World1")
    time.sleep(1)
    message2()


def message2():
    print("Hello World2")
    time.sleep(1)
    message3()


def message3():
    print("Hello World3")
    time.sleep(1)
    message4()


def message4():
    print("Hello World4")
    # message() FOREVER LOOP XD


message()
