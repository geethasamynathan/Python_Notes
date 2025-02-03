import threading
import time

def background_task():
    for i in range(5):
        print(f"Daemon thread running {i}")
        time.sleep(2)

t = threading.Thread(target=background_task, daemon=True)  # 👈 Daemon thread
t.start()

print("Main program exits, daemon thread will be killed automatically.")
