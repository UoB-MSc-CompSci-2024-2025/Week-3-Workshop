import random

# Function to get user's guess
def get_user_guess():
    guess = int(input("Enter your guess (1-100): "))
    return guess


# Function to check the guess against the target number
def check_guess(guess, target):
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number.")
        return True
    return False


def guessing_game_entrypoint(score):
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    guessed_correctly = False

    print("Welcome to the Guessing Game!")

    # Repetition: Continue looping until the correct guess is made
    while not guessed_correctly:
        # Selection: Get the user's guess and check if it's correct
        user_guess = get_user_guess()
        guessed_correctly = check_guess(user_guess, target_number)
        if guessed_correctly:
            score += 1
    return score


# Function to find the smallest number divisible by both 3 and 5
def find_divisible_by_3_and_5(start, end):
    for num in range(start, end + 1):
        # Selection: Check if number is divisible by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            return num #using a return in a for loop
    return None  # If no such number is found, return None


# Function to get the range from the user
def get_range():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    return start, end

# Main game function
def divisible_game_entrypoint(score):
    print("Welcome to the Number Divisibility Game!")

    # Get the range from the user
    start, end = get_range()
    guess = int(input("What is your guess? If you think there is no number type 0 "))
    # Find the smallest number divisible by both 3 and 5
    result = find_divisible_by_3_and_5(start, end)

    # Selection: Print the result or no number found message
    if result:
        print(f"The smallest number divisible by both 3 and 5 in the range is: {result}")
        if result == guess:
            print(f"You guessed correctly")
            score += 1
        else:
            print(f"You did not guess that one correctly, better luck next time!")
    else:
        print("No number found that is divisible by both 3 and 5 within the range.")
    if guess == 0:
        print(f"You guessed correctly")
    return score

def hangman_entrypoint(score):
    # Step 1: List of words and randomly select one
    words = ['python', 'javascript', 'java', 'hangman', 'developer', 'algorithm']
    word_to_guess = random.choice(words) #used in lists, tuples and strings to make a choice out of the data collection
    guessed_word = ['_'] * len(word_to_guess)  # Display word with dashes
    attempts = 6  # Player gets 6 wrong attempts
    guessed_letters = []  # Track guessed letters

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word_to_guess)} letters.")
    print("You have 6 attempts to guess the word.")

    # Step 2: Game loop
    while attempts > 0 and '_' in guessed_word:
        print("\nWord to guess: ", " ".join(guessed_word))
        guess = input("Enter a letter: ").lower()

        # Step 3: Check if letter has been guessed already
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        # Step 4: Check if the guessed letter is in the word
        if guess in word_to_guess:
            # Reveal the guessed letters in the word
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
            print(f"Good job! '{guess}' is in the word.")
        else:
            # Wrong guess, reduce attempts
            attempts -= 1
            print(f"'{guess}' is not in the word. You have {attempts} attempts left.")

    # Step 5: Game over scenarios
    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word_to_guess)
        score += 1
    else:
        print("\nSorry, you're out of attempts. The word was:", word_to_guess)
    return score

def main():
    score = 0
    while True:
        print(f"Your current score is: {score}")
        choice = int(input("What is your choice of game?\n"
                           "1. Guessing game\n"
                           "2. Find the smallest number divisible by 3 and 5\n"
                           "3. Hangman\n" 
                           "4. Exit\n"))
        match choice:
            case 1:
                score = guessing_game_entrypoint(score)
            case 2:
                score = divisible_game_entrypoint(score)
            case 3:
                score = hangman_entrypoint(score)
            case 4:
                break
            case _:
                print("Incorrect choice entered")

if __name__ == '__main__':
    main()
