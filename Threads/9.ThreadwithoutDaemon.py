import threading
import time

def background_task():
    for i in range(5):
        print(f"Daemon thread running {i}")
        time.sleep(2)

t = threading.Thread(target=background_task)
t.start()  # Starts the thread (but not as a daemon)

print("Main program exits, but thread keeps running...")