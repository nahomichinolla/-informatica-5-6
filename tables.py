def main():

        num = input("Enter a number (1-10): ")

        num = int(num)
        print("Here is the {num} times table")

        for x in range(11):
              answer = x * num
              print(f"{x} times {num} is {answer}")



if __name__=="__main__":
    main()
