import threading
import time

def task1():
    for i in range(1,10,2) :
        print(f"I print odd numbers Task 1 - Count: {i}")
        time.sleep(1)

def task2():
    for i in range(2,10,2) :
        print(f"I print even numbers Task 2 - Count: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Both tasks completed")