from queues.queuecustom import Queue


class QueueCaller:
    @staticmethod
    def main():
        queue_capacity = 5
        queue = Queue(queue_capacity)

        # Enqueue elements until the queue is full
        print("Enqueuing elements:")
        for i in range(queue_capacity):
            queue.enqueue(i + 1)
            print(f"Enqueued: {i + 1}")

        # Displaying queue full scenario
        print("Attempting to enqueue in a full queue:")
        queue.enqueue(99)  # This should trigger the 'Queue Full' message

        # Dequeue some elements to make space
        print("\nDequeuing elements to make space:")
        for _ in range(2):  # Dequeue two elements
            value = queue.dequeue()
            print(f"Dequeued: {value}")

        # Enqueue more elements after making space
        print("\nEnqueuing more elements:")
        for i in range(3):
            queue.enqueue(i + 10)
            print(f"Enqueued: {i + 10}")

        # Displaying the elements in the queue
        print("\nCurrent Queue elements:")
        while not queue.is_empty():
            value = queue.dequeue()
            print(f"Dequeued: {value}")


if __name__ == "__main__":
    QueueCaller.main()
