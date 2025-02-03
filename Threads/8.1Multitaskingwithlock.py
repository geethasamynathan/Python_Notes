import threading
import time

class TicketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets  # Shared resource
        self.lock = threading.Lock()  # Lock object

    def book_ticket(self, name):
        print(f"{name} is trying to book a ticket...")
        with self.lock:  # Ensures only one thread accesses this block at a time
            if self.available_tickets > 0:
                time.sleep(1)  # Simulate delay
                self.available_tickets -= 1  # Reduce ticket count
                print(f"{name} successfully booked a ticket! Remaining: {self.available_tickets}")
            else:
                print(f"Sorry {name}, no tickets available!")

# Creating a shared TicketBooking object
booking_system = TicketBooking(1)

# Multiple users trying to book at the same time
threads = []
users = ["Alice", "Bob"]
for user in users:
    t = threading.Thread(target=booking_system.book_ticket, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
    
