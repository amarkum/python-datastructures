"""Threading examples — locks, threads, and the GIL."""

import threading
import time
from concurrent.futures import ThreadPoolExecutor


counter = 0
counter_lock = threading.Lock()


def unsafe_increment():
    global counter
    for _ in range(100_000):
        counter += 1


def safe_increment():
    global counter
    for _ in range(100_000):
        with counter_lock:
            counter += 1


def worker(name, delay):
    print(f"  Thread {name} starting")
    time.sleep(delay)
    print(f"  Thread {name} done")


def demonstrate_race_condition():
    global counter
    counter = 0
    threads = [threading.Thread(target=unsafe_increment) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Unsafe counter (expected 400000): {counter}")


def demonstrate_lock():
    global counter
    counter = 0
    threads = [threading.Thread(target=safe_increment) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Safe counter (expected 400000): {counter}")


if __name__ == "__main__":
    print("=== Basic threads ===")
    threads = [threading.Thread(target=worker, args=(i, 0.1)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\n=== Race condition ===")
    demonstrate_race_condition()

    print("\n=== Lock fixes race ===")
    demonstrate_lock()

    print("\n=== ThreadPoolExecutor ===")
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(worker, f"pool-{i}", 0.05) for i in range(3)]
        for f in futures:
            f.result()
