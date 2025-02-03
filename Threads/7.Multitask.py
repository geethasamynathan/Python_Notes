import threading
import queue
import time

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(i)
        print(f"Produced: {i}")

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(2)

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal the consumer to exit
consumer_thread.join()
print("Thread communication completed")