import string
from getpass import getpass

def hangman_drawing(guesses):
    stages = [  # guess: 1
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,
                # guess: 2
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     /
                    -
                    """,
                # guess: 3
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |
                    -
                    """,
                # guess: 4
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |
                    -
                    """,
                # guess: 5
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |
                    -
                    """,
                # guess: 6
                """
                    --------
                    |      |
                    |      O
                    |
                    |
                    |
                    -
                    """,
                # guess: 7
                """
                    --------
                    |      |
                    |
                    |
                    |
                    |
                    -
                    """
    ]

    print(stages[guesses])

print("Welcome to Hangman! Enter a word and have someone try to guess it by entering letters. They can also enter the entire word if they've guessed it.")

while True:
    secret = getpass("Enter the secret word: ").upper()
    blank = "_ " * (len(secret)-1) + "_"
    blank = list(blank)

    guesses = 6
    letters = string.ascii_uppercase

    hangman_drawing(guesses)

    while True:
        for i in blank:
            print(i, end="")
        print("\nGuesses left:", guesses, "\nAvailible letters:", letters, "\n")

        user_guess = input("Guess a letter: ").upper()

        if user_guess.upper() == secret:
            print("Congratulations! The word was", secret + ".")
            break

        while not user_guess.isalpha() or len(user_guess) != 1:
            user_guess = input("Invalid input. Guess a letter: ").upper()

        if not user_guess in letters:
            print("You've already guessed that letter!")
            continue

        letters = letters.replace(user_guess, " ")

        if not user_guess in secret:
            guesses -= 1

            hangman_drawing(guesses)
            print("There is no", user_guess, "in the word.")

            if guesses == 0:
                print("You ran out of guesses. The word was",
                      secret + ".", "Better luck next time!")
                break

        else:
            hangman_drawing(guesses)

            for i in range(len(secret)):
                if secret[i] == user_guess:
                    blank[i*2] = secret[i]

        if not "_" in blank:
            print("Congratulations! The word was", secret + ".")
            break

    print()
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        break
