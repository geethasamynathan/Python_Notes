import threading
import time

def single_task():
    print("Task started")
    time.sleep(2)
    print("Task completed")

thread = threading.Thread(target=single_task)
thread.start()
thread.join()  # Wait for the thread to finish before exiting
print("Main thread execution completed")