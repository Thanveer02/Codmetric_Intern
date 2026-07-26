import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")

while True:
    user_input = input("Enter your guess: ")

    # Input validation to ensure the user enters an integer
    if not user_input.isdigit():
        print("🚫 Oops! Please enter a valid whole number.")
        continue

    guess = int(user_input)
    attempts += 1

    if guess < secret_number:
        print("📉 Too low! Try a higher number.")
    elif guess > secret_number:
        print("📈 Too high! Try a lower number.")
    else:
        print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
        break
