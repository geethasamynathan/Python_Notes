import threading
import time

def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(3)  # Simulate download time
    print(f"Download complete: {file_name}")

files = ["file1.zip", "file2.zip", "file3.zip"]
threads = []

for file in files:
    thread = threading.Thread(target=download_file,args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All downloads completed")