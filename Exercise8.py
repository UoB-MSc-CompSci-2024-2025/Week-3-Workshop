from random import randint

def generate_dice():
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    return num1, num2

def throw_dice(num1, num2, money):
    if num1 + num2 == 7:
        money += 4
    else:
        money -= 1
    return money

def main():
    money = int(input("How much money would you like to put into the pot? "))
    while True:
        num1, num2 = generate_dice()
        choice = input("Throw the dice? Y / N: ").lower()
        match choice:
            case "y":
                money = throw_dice(num1, num2, money)
                print(f"Your dice landed on: {num1} and {num2}")
                print(f"You now have: £{money}")
            case "n":
                print(f"You finished the game with: £{money}")
                exit()

if __name__ == "__main__":
    main()