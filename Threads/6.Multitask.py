import threading
import time

def handle_request(user_id):
    print(f"Handling request for user {user_id}")
    time.sleep(2)  # Simulating request processing time
    print(f"Request completed for user {user_id}")

user_requests = [1, 2, 3, 4, 5]
threads = []

for user_id in user_requests:
    thread = threading.Thread(target=handle_request, args=(user_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All user requests handled")