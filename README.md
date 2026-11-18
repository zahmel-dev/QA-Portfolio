# Python Exercises & Test Automation

Solving various Python logic exercises and implementing automated unit, UI, and end-to-end (E2E) tests using **Pytest**, **Playwright**, and **Selenium**.

## Project Structure

This project follows the standard Python `src` layout and uses `uv` for fast dependency and environment management. Tests are strictly separated into unit tests and framework-specific E2E suites following the **Page Object Model (POM)**.

```text
QA-Portfolio/
├── pyproject.toml          # Dependencies & Pytest configuration
├── uv.lock                 # Reproducible dependency lockfile
├── src/
│   └── exercises/          # Core logic and exercise modules
└── tests/
    ├── unit/               # Unit tests for src/exercises
    └── e2e/                # UI & E2E tests structured via POM (Playwright & Selenium)
```

## Setup & Running Tests

### Option 1: Using `uv` (Recommended)
If you have [uv](https://astral.sh) installed, you can run the test suite directly. `uv` will automatically create a virtual environment and install all exact dependencies from `uv.lock`:

```bash
uv run pytest
```

### Option 2: Using standard `pip`
Alternatively, create a virtual environment manually, install the project dependencies from `pyproject.toml`, and run `pytest`:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install .
pytest
```