# In hangman/tests/test_hangman_session.py

import pytest

from src.hangman.models import HangmanSession, Status


class TestHangmanSession:
    """Tests for the HangmanSession class."""

    def test_initial_state(self) -> None:
        """Tests the initial state of a new session."""
        # Arrange
        session = HangmanSession(word="java")

        # Assert
        assert session.word == "java"
        assert session.guesses == set()
        assert not session.is_word_solved()
        assert session.get_current_progress() == "----"

    def test_repeated_guess_returns_same(self) -> None:
        """Tests that guessing the same letter twice returns Status.SAME."""
        # Arrange
        session = HangmanSession(word="python")
        session.make_guess("p")  # First guess

        # Act
        status = session.make_guess("p")  # Second, repeated guess

        # Assert
        assert status == Status.SAME
        assert session.guesses == {"p"}  # The set should not change size

    def test_is_solved_after_all_letters_guessed(self) -> None:
        """Tests that the word is solved only after all unique letters are guessed."""
        # Arrange
        session = HangmanSession(word="on")

        # Assert initial state
        assert not session.is_word_solved()

        # Act & Assert during progress
        session.make_guess("o")
        assert not session.is_word_solved()
        assert session.get_current_progress() == "o-"

        session.make_guess("n")
        assert session.is_word_solved()
        assert session.get_current_progress() == "on"

    # --- A More Pytest-ic Way: Parametrizing Tests ---
    @pytest.mark.parametrize(
        "letter, expected_status",
        [
            ("p", Status.HIT),  # A correct letter
            ("y", Status.HIT),  # Another correct letter
            ("z", Status.MISS),  # An incorrect letter
            ("a", Status.MISS),  # Another incorrect letter
        ],
    )
    def test_make_guess_hit_or_miss(self, letter: str, expected_status: Status) -> None:
        """
        Tests a single guess for both HIT and MISS cases using parametrization.
        """
        # Arrange
        session = HangmanSession(word="python")

        # Act
        status = session.make_guess(letter)

        # Assert
        assert status == expected_status
        assert letter in session.guesses
