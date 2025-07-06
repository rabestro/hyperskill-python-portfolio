![CI](https://img.shields.io/github/actions/workflow/status/rabestro/hyperskill-python-portfolio/ci.yml?branch=main&label=ci)
![Python](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue)
![License](https://img.shields.io/github/license/rabestro/hyperskill-python-portfolio)
![Style](https://img.shields.io/badge/code%20style-ruff-blueviolet)
![Type Check](https://img.shields.io/badge/type%20checked-mypy-informational)
![Complexity](https://img.shields.io/badge/complexity-A-brightgreen)
![Built with](https://img.shields.io/badge/built%20with-make-blue)

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
- ⚙️ Managed with [uv](https://github.com/astral-sh/uv) and automated via [Makefile](Makefile)

---

## Goal

> Learn Python **quickly and practically**, while building confidence with the **Python development toolkit** (
> formatting, linting, typing, testing, CI).

---

## Project Structure

Each subfolder represents a small educational project:

| Folder         | Description                                   |
|----------------|-----------------------------------------------|
| `billsplitter` | A simple program to split bills among friends |
| `chatbot`      | A basic chatbot with scripted dialogue        |
| `hangman`      | The classic Hangman game                      |
| `rps`          | Rock-Paper-Scissors with score tracking       |

Each project may include its own `README.md`, source code (`src/`) and tests (`tests/`).

---

## Getting Started

### Prerequisites

- Python `>=3.11`
- [uv](https://github.com/astral-sh/uv) installed (`pip install uv`)

### Setup

```bash
make install
```

### Run checks

```shell
make check      # All checks: lint, format, mypy, test, radon
make test       # Run pytest
```

---

## Tools Used

- Ruff — linter and formatter
- Mypy — static typing
- Pytest — testing
- Radon — complexity and maintainability metrics
- Make — automation
- uv — ultra-fast Python packaging

---

## Quality Metrics

Metrics such as cyclomatic complexity and maintainability index are generated with:

```bash
make cc     # complexity
make mi     # maintainability index
```

---

## License

This project is licensed under the MIT License.

---

## Why I Started This

I needed to quickly learn Python while applying best practices from day one: testing, formatting, CI, and type safety.
This portfolio is the result of hands-on exploration through real educational tasks.
