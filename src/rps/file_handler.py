DEFAULT_RATING_FILE = "rating.txt"


def get_user_score(username: str, file_path: str = DEFAULT_RATING_FILE) -> int:
    """Reads a user's score from a specified file.

    This function opens a file at a given path, searches for a specific
    username, and returns their score.

    Args:
        username: The name of the user whose score is to be retrieved.
        file_path: The path to the file containing user ratings. Defaults
                   to "rating.txt".

    Returns:
        The user's score as an integer.

    Raises:
        FileNotFoundError: If the file at `file_path` cannot be found.
        ValueError: If a user's score in the file is not a valid integer,
                    or if a line is malformed.
    """
    with open(file_path) as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                continue

            name, score_str = parts
            if name == username:
                return int(score_str)  # Let potential ValueError propagate
    raise ValueError(f"Username '{username}' not found in {file_path}")
