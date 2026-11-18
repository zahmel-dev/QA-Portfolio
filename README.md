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