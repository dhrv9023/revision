import random

target = int(random.random() * 10)
chance = 10

while chance > 0:
    x = int(input("Enter your guess: "))
    chance -= 1
    
    if x == target:
        print(f"{x} is the right answer!")
        break
    elif x < target:
        print(f"Cold! You have {chance} chances left.")
    else:
        print(f"Hot! You have {chance} chances left.")

if chance == 0 and x != target:
    print(f"Game over! The target was {target}.")