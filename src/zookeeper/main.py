from .art import ALL_ART

GREETING = (
    "Please enter the number of the habitat "
    f"(0-{len(ALL_ART) - 1}) you would like to view:"
)
FAREWELL = "See you later!"
ERROR_MESSAGE = "\nInvalid habitat number. Please try again.\n"
EXIT_COMMAND = "exit"


def main() -> None:
    habitats = {str(i): animal for i, animal in enumerate(ALL_ART)}

    while (channel := input(GREETING)) != EXIT_COMMAND:
        if animal_art := habitats.get(channel):
            print(animal_art)
        else:
            print(ERROR_MESSAGE)

    print(FAREWELL)


if __name__ == "__main__":
    main()
