from stack.stackcustom import Stack


class StackCaller:
    @staticmethod
    def main():
        stack_capacity = 5
        stack = Stack(stack_capacity)

        # Push elements onto the stack
        print("Pushing elements onto the stack:")
        for i in range(stack_capacity):
            stack.push(i + 1)
            print(f"Pushed: {i + 1}")

        # Displaying stack full scenario
        print("Attempting to push onto a full stack:")
        stack.push(99)  # This should trigger the 'Stack is Full' message

        # Popping elements from the stack
        print("\nPopping elements from the stack:")
        while not stack.is_empty():
            value = stack.pop()
            print(f"Popped: {value}")

        # Attempt to pop from an empty stack
        print("\nAttempting to pop from an empty stack:")
        stack.pop()


if __name__ == "__main__":
    StackCaller.main()
