from src.rps.game_logic import GameOptions


def test_classic_rock_paper_scissors():
    options = GameOptions("rock,paper,scissors")
    # User wins
    assert options.compare("rock", "scissors") == 1
    assert options.compare("scissors", "paper") == 1
    assert options.compare("paper", "rock") == 1
    # Draws
    assert options.compare("rock", "rock") == 0
    # Computer wins
    assert options.compare("rock", "paper") == -1
