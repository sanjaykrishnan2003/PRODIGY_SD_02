
import random

def number_guessing_game():
  number = random.randint(0, 100)
  attempts = 0
  max_attempts = 10

  print("Welcome to the Number Guessing Game!")
  print("I've picked a number between 0 and 100. Can you guess it?")
  print(f"You have {max_attempts} attempts.")

  while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
      print(f"Congratulations! You guessed the number in {attempts} attempts.")
      break
    elif guess < number:
      if abs(guess - number) <= 5:
        print("You're getting close! A bit low.")
      else:
        print("Too low. Try again.")
    else:
      if abs(guess - number) <= 5:
        print("You're getting close! A bit high.")
      else:
        print("Too high. Try again.")

  if attempts == max_attempts:
    print(f"Sorry, you ran out of attempts. The number was {number}.")

if __name__ == "__main__":
  number_guessing_game()

