import random

def choose_random_word():
    words = ["cat", "bat", "rat", "art", "car", "tar"]
    return random.choice(words)

def display_letters(letters):
    print("Letters available: " + " ".join(letters))

def is_valid_guess(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

def main():
    print("Welcome to Console Wordscapes!")

    target_word = choose_random_word()
    target_letters = list(target_word)
    guessed_words = set()

    while True:
        display_letters(target_letters)

        guess = input("Enter your guess (or type 'quit' to exit): ").lower()

        if guess == 'quit':
            print("Thanks for playing. The correct word was:", target_word)
            break

        if guess in guessed_words:
            print("You already guessed that word. Try again!")
            continue

        if is_valid_guess(guess, target_letters):
            guessed_words.add(guess)
            print("Good job! You guessed a valid word.")
        else:
            print("Invalid guess. Make sure to use the provided letters.")

        if set(guessed_words) == set(target_word):
            print("Congratulations! You guessed all the words. The correct word was:", target_word)
            break

if __name__ == "__main__":
    main()