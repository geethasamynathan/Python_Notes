import threading

data_chunks = [
    list(range(100000)),  # First chunk
    list(range(100000, 200000)),  # Second chunk
    list(range(200000, 300000)),  # Third chunk
]



def process_data(data):# double the items
    print(f"Processing {len(data)} records")
    result = sum(data)  # Simulating data processing
    print(f"Processing complete: {result}")

threads = []

for chunk in data_chunks:
    thread = threading.Thread(target=process_data, args=(chunk,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All data processed")