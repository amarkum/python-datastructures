"""Async/await examples — coroutines and asyncio."""

import asyncio


async def fetch_data(name, delay):
    print(f"  [{name}] starting...")
    await asyncio.sleep(delay)
    print(f"  [{name}] done")
    return f"result-{name}"


async def gather_example():
    """Run coroutines concurrently."""
    results = await asyncio.gather(
        fetch_data("A", 0.2),
        fetch_data("B", 0.1),
        fetch_data("C", 0.15),
    )
    return results


async def task_example():
    """Create tasks for concurrent execution."""
    task1 = asyncio.create_task(fetch_data("task-1", 0.1))
    task2 = asyncio.create_task(fetch_data("task-2", 0.1))
    return await asyncio.gather(task1, task2)


async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.05)
        yield i


async def main():
    print("=== Sequential await ===")
    await fetch_data("solo", 0.1)

    print("\n=== asyncio.gather (concurrent) ===")
    results = await gather_example()
    print(f"Results: {results}")

    print("\n=== asyncio.create_task ===")
    await task_example()

    print("\n=== async generator ===")
    async for value in async_generator():
        print(f"  got {value}")


if __name__ == "__main__":
    asyncio.run(main())
