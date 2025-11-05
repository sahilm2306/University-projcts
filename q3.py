# question 3.py

from collections import Counter


# --------------------------------------------------------
# (a) Find the most frequent word not in another list
# --------------------------------------------------------
def findMostFrequentWord(words_list: list[str], exclude_list: list[str]) -> str:
    excluded_words = set(exclude_list)
    valid_words = [word for word in words_list if word not in excluded_words]

    if not valid_words:
        return ""

    word_count = Counter(valid_words)
    most_common_word, _ = word_count.most_common(1)[0]
    return most_common_word


# --------------------------------------------------------
# (b) Find the most frequent follower of a given word
# --------------------------------------------------------
def findMostFrequentFollower(word_list: list[str], target_word: str) -> str:

    lower_list = [w.lower() for w in word_list]
    target = target_word.lower()
    follower_counts = {}

    # Go through all pairs of words
    for i in range(len(lower_list) - 1):
        if lower_list[i] == target:
            next_word = lower_list[i + 1]
            follower_counts[next_word] = follower_counts.get(next_word, 0) + 1

    if not follower_counts:
        return ""

    # Find the follower(s) with the highest frequency
    max_count = max(follower_counts.values())
    candidates = {word for word, count in follower_counts.items()
                  if count == max_count}

    # Return whichever candidate appears last in the original list
    for word in reversed(lower_list):
        if word in candidates:
            return word

    return ""


# --------------------------------------------------------
# (c) QuickSort (using the first element as the pivot)
# --------------------------------------------------------
def quicksort(numbers: list[int]) -> list[int]:

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    smaller = [n for n in numbers[1:] if n <= pivot]
    larger = [n for n in numbers[1:] if n > pivot]

    return quicksort(smaller) + [pivot] + quicksort(larger)


# --------------------------------------------------------
# Menu display
# --------------------------------------------------------
def show_menu():
    print("\n===================================")
    print("  MOST FREQUENT WORD PROGRAM")
    print("===================================")
    print("1  Find most frequent word (not in another list)")
    print("2  Find most frequent follower of a given word")
    print("3  Sort a list using QuickSort")
    print("4  Exit")
    print("===================================\n")


# --------------------------------------------------------
# Main program
# --------------------------------------------------------
def main():
    print("Welcome! This program helps you explore words and sorting.\n")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Most frequent word not in another list
        if choice == "1":
            words1 = input(
                "Enter words for List 1 (separated by spaces): ").split()
            words2 = input(
                "Enter words for List 2 (separated by spaces): ").split()
            result = findMostFrequentWord(words1, words2)

            if result:
                print(
                    f"\n The most frequent word (not in list 2) is: '{result}'")
            else:
                print("\n No valid words found — check your input lists!")

        # Option 2: Most frequent follower
        elif choice == "2":
            sentence = input("Enter a sentence: ").replace(".", "").split()
            target = input("Enter the target word: ")
            result = findMostFrequentFollower(sentence, target)

            if result:
                print(
                    f"\n The word that most often follows '{target}' is: '{result}'")
            else:
                print(f"\n Couldn’t find any words that follow '{target}'.")

        # Option 3: QuickSort demonstration
        elif choice == "3":
            try:
                numbers = list(
                    map(int, input("Enter numbers separated by spaces: ").split()))
                sorted_list = quicksort(numbers)
                print(f" Sorted list: {sorted_list}")
            except ValueError:
                print(" Please enter valid whole numbers only!")

        # Option 4: Exit program
        elif choice == "4":
            print("\n Thanks for using the program! Goodbye!\n")
            break

        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")


# --------------------------------------------------------
# Run the program
# --------------------------------------------------------
if __name__ == "__main__":
    main()
