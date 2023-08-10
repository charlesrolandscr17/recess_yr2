import sqlite3
import time
import threading
import multiprocessing

with open('roland.txt', 'w') as f:
    f.write("This is my very own file")


# Usage example
with sqlite3.connect('mydatabase.db') as db:
    cursor = db.cursor()


# Multithreading and Multiprocessing
# Function to run
def my_function(name, duration):
    print(f"Started {name}")
    time.sleep(duration)
    print(f"Finished {name}")

# Multithreading example
threads = []
thread_names = ["Thread 1", "Thread 2", "Thread 3"]
durations = [3, 5, 2]

for name, duration in zip(thread_names, durations):
    thread = threading.Thread(target=my_function, args=(name, duration))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
