def main():
    # planet = input("Planet: ")

    # # Separation
    # print("Hello", planet)

    # # Concatenation
    # print("Hello " + planet)

    # #Formatted Strings
    # print(f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adjective = input("Give me an adjective: ").strip().lower()
    goal = input("A goal you want to achieve: ").strip().lower()

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story: ")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")
    print("This is your story: ")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}!".upper())



if __name__ == "__main__":
    main()
