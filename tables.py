def main():

        num = input("Enter a number (1-10): ")

        num = int(num)
        print("Here is the", num, "times table")

        for i in range(1, 11):
              print(i, "times", num, "is", i * num)



if __name__=="__main__":
    main()
