import random

def User_guess(limit):
    print(f"You have to Guess a number between 1 to {limit}")
    print("To exit the game you have give the input number as 0")
    random_number = random.randint(1,limit)
    guess = 0;
    while guess != random_number:
        guess = int(input(f"Give a number between 1 and {limit} : "))
        if guess == 0:
            print("You have exited the game")
            break;
        elif guess > random_number:
            print("Guessed Number is high")
        elif guess < random_number:
            print("Guessed Number is low")
        elif guess == random_number:
            print(f"hoorah You have found the number {random_number}")  
            break;


def Computer_guess(limit):
    min = 1
    max = limit
    feedback = ""
    while feedback != 'c':
        guess = random.randint(min,max)
        feedback = input(f'Is {guess} too high(h), too low(l) or correct(c)').lower()
        if feedback  == 'h':
            max = guess - 1
        elif feedback == 'l':
            min = guess + 1
    print("Hoorah Computer has guessed the number")


Computer_guess(20)
