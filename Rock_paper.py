import random

dic = {"r": 1, "p": -1, "s": 0}

def game(a, b):
    if a == b:
        return "Tie"
    elif (dic[a] - dic[b]) % 3 == 1:
        return "Player 1 wins"
    else:
        return "Player 2 / wins"

while True:
    try:
        cho = int(input("\n1: Play with Computer\n2: Play with Friend\n0: Exit\nEnter choice: "))
    except:
        print("Invalid input! Enter a number.")
        continue

    if cho == 0:
        print("Game exited.")
        break

    elif cho == 1:
        a = input("Enter r/p/s: ").lower()
        if a not in dic:
            print("Invalid choice!")
            continue

        b = random.choice(["r", "p", "s"])
        print("Computer chose:", b)
        print(game(a, b))

    elif cho == 2:
        a = input("Player 1 (r/p/s): ").lower()
        b = input("Player 2 (r/p/s): ").lower()

        if a not in dic or b not in dic:
            print("Invalid input!")
            continue

        print(game(a, b))
        

    else:
        print("Invalid menu choice!")
        