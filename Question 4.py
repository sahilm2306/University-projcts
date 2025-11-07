def collatz(n: int) -> int:
    # Show the current number in the sequence
    print(n, end=" ")

    #  Base case:
    if n == 1:
        return 1

    # If the number is even number then it is divided by 2
    elif n % 2 == 0:
        return collatz(n // 2)

    # If the number is odd then 3*number +1 is added
    else:
        return collatz(3 * n + 1)


# #######################################################
# Main function (user interaction)
# #######################################################
def main():
    print("***********************")
    print("\n    Welcome to the Collatz Explorer!\n")
    print("***********************\n")

    try:
        num = int(input(" Enter a positive integer to begin: "))

        if num <= 0:
            print("  Please enter a number greater than zero.")
            return

        print("\n\n Collatz sequence:")
        collatz(num)
        print("\n\n\n Sequence completed — you reached 1!")

    except ValueError:
        print(" Invalid input. Please enter a valid whole number.")


# Looping the start
if __name__ == "__main__":
    main()
