"""Multiprocessing — CPU-bound parallelism across processes."""

import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


def square(n):
    return n * n


def cpu_heavy(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def worker(queue, result_list):
    while True:
        item = queue.get()
        if item is None:
            break
        result_list.append(item * 2)


if __name__ == "__main__":
    print("=== ProcessPoolExecutor ===")
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(square, range(8)))
    print(results)

    print("\n=== mp.Process ===")
    queue = mp.Queue()
    manager = mp.Manager()
    results = manager.list()
    processes = [mp.Process(target=worker, args=(queue, results)) for _ in range(2)]
    for p in processes:
        p.start()
    for i in range(5):
        queue.put(i)
    for _ in processes:
        queue.put(None)
    for p in processes:
        p.join()
    print(sorted(results))

    print("\n=== CPU-bound comparison note ===")
    print("Threading won't speed this up due to GIL; processes have separate memory.")
