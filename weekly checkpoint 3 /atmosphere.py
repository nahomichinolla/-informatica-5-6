def main() :
    print("Descent atmosphere layer: ")
    layer = input("Descent atmosphere layer: ").strip().lower()
    if layer == "Exosphere":
        print("Your altiltitude level will be between 700 - 10000km")
    elif layer == "Mesosphere":
        print("Your altitude level will be between 50 - 85km")
    elif layer == "Thermosphere":
        print("Your altitude will be between 85 - 700km")
    elif layer == "Stratosphere":
        print("Your altitude will be between 12 - 50km")
    elif layer == "Troposhere":
        print("Your altitude will be between 0 - 12km")
    else:
        print("Insert a valid atmosphere layer: ")
    exact = input("Enter exact altitude: ")
    ex = 2000
    me = 200
    th = 500
    st = 75
    tr = 20
    if exact > 699:
        a1 = (exact*1000)/ex
        a2 = 35000/me
        a3 = 30000/st
        a4 = 12000/tr
        a5 = 61500/th
        a6 = a2 + a3 + a4 + a5
        print(a2 + a3 + a4 + a5, "seconds")
    elif exact > 84:



    print("Enter exact altitude: ")
    if
        print("Total descend time:")

if __name__ == "__main__":
    main()
