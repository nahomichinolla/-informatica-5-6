def main():
    doctrine = ["Faith in the Lord Jesus Christ", "Repentance", "Baptism", "Impocicion de manos", "Perseverar hasta el fin"]

    index = 0

    # while index < len(doctrine): Condition
    #   print(doctrine[index])
    #   index += 1 Update

    for i in range(len(doctrine)):
        print(f"{i+1} {doctrine[i]}")

if __name__ == "__main__":
    main()
