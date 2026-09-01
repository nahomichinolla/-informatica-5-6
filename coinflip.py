import random
def main():

    flip = input("Heads(1) or Tails(2): ")
    coin = random.randint(1,2)

    if coin == 1:
        print("Heads")
    else:
        print("Tails")

    if flip == coin:
        print("you win!")
    else:
        print("you loose")


if __name__ == "__main__":
    main()

