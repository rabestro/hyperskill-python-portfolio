# hyperskill-python-portfolio

My journey through Hyperskill, captured in a portfolio of Python projects. Each solution is refactored for quality,
tested with pytest, and statically checked with mypy.

## About

This repository contains a curated portfolio of small Python projects completed as part of
my [Hyperskill](https://hyperskill.org) learning journey.

Each project is:

- ✅ Refactored for readability and structure
- 🧪 Tested with [pytest](https://docs.pytest.org/)
- 🧼 Linted and formatted with [ruff](https://docs.astral.sh/ruff/)
- 🧠 Type-checked with [mypy](https://mypy.readthedocs.io/)
- 📐 Analyzed for complexity and maintainability using [radon](https://radon.readthedocs.io/)
- ⚙️ Managed with [uv](https://github.com/astral-sh/uv) and automated
  via [Makefile](https://www.google.com/search?q=Makefile)

## Goal

> Learn Python **quickly and practically**, while building confidence with the **Python development toolkit** (
> formatting, linting, typing, testing, CI).

## Installation

To use the applications from this portfolio, you can install the package directly from PyPI:

```
pip install hyperskill-python-portfolio
```

Once installed, you can run any of the applications directly from your command line.

### Examples

```
# Run the loan calculator
loancalc annuity --principal 500000 --interest 5 --periods 360

# Run the hangman game
hangman

# Run the rock-paper-scissors game
rps
```

## Project Structure

Each application is a self-contained project within this portfolio.

| Folder         | Description                                   |
|----------------|-----------------------------------------------|
| `loancalc`     | A powerful command-line loan calculator       |
| `billsplitter` | A simple program to split bills among friends |
| `chatbot`      | A basic chatbot with scripted dialogue        |
| `hangman`      | The classic Hangman game                      |
| `rps`          | Rock-Paper-Scissors with score tracking       |

## Development Setup

If you wish to contribute to the project, follow these steps to set up a local development environment.

### Prerequisites

- Python `>=3.11`

- [uv](https://github.com/astral-sh/uv "null") installed (`pip install uv`)

### Setup

```
# 1. Clone the repository
git clone [https://github.com/rabestro/hyperskill-python-portfolio.git](https://github.com/rabestro/hyperskill-python-portfolio.git)
cd hyperskill-python-portfolio

# 2. Install dependencies for development
make install
```

### Run checks

```
make check      # All checks: lint, format, mypy, test, radon
make test       # Run pytest
```

## Tools Used

- **uv** — Ultra-fast Python packaging and resolution
- **Ruff** — Linter and formatter
- **Mypy** — Static typing
- **Pytest** — Testing framework
- **Radon** — Complexity and maintainability metrics
- **Make** — Automation and command runner

## Quality Metrics

Metrics such as cyclomatic complexity and maintainability index are generated with:

```
make cc     # complexity
make mi     # maintainability index
```

## Why I Started This

This portfolio was born from a desire to learn Python quickly and practically by applying software engineering best
practices from day one: testing, formatting, CI, and type safety. This portfolio is the result of hands-on exploration
through real educational tasks.

## License

This project is licensed under the MIT License.
