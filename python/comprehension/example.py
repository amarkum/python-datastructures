"""Comprehension examples — list, dict, set, and generator."""

from itertools import islice


# --- List comprehension ---
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# --- Dict comprehension ---
word_lengths = {word: len(word) for word in ["python", "java", "go"]}
inverted = {v: k for k, v in word_lengths.items()}

# --- Set comprehension ---
unique_lengths = {len(word) for word in ["aa", "bbb", "cccc", "aa"]}

# --- Generator comprehension (lazy) ---
sum_of_squares = sum(x ** 2 for x in range(1000))

# --- Nested comprehension (flatten 2D list) ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]

# --- Walrus operator in comprehension (3.8+) ---
def first_long_word(words, min_len=5):
    return next((w for w in words if (n := len(w)) >= min_len), None)


if __name__ == "__main__":
    print("=== List ===")
    print(f"squares: {squares}")
    print(f"evens: {evens}")

    print("\n=== Dict ===")
    print(f"word_lengths: {word_lengths}")
    print(f"inverted: {inverted}")

    print("\n=== Set ===")
    print(f"unique_lengths: {unique_lengths}")

    print("\n=== Generator ===")
    print(f"sum_of_squares: {sum_of_squares}")
    gen = (x * 2 for x in range(5))
    print(f"first 3: {list(islice(gen, 3))}")

    print("\n=== Nested / flatten ===")
    print(f"flat: {flat}")

    print("\n=== Walrus ===")
    print(first_long_word(["hi", "hey", "hello", "world"]))
