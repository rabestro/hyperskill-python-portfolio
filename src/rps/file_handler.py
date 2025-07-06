RATING_FILE_PATH = "rating.txt"


def get_user_score(username):
    """
    Reads 'rating.txt' to find and return a user's score.
    Returns 0 if the user is not found or the file doesn't exist.
    """
    try:
        with open(RATING_FILE_PATH) as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    name, score = parts
                    if name == username:
                        return int(score)
    except FileNotFoundError:
        print(f"{RATING_FILE_PATH} not found. Starting with a score of 0.")
        return 0
    except ValueError:
        print(
            f"Error reading score from {RATING_FILE_PATH}. Starting with a score of 0."
        )
        return 0

    return 0
