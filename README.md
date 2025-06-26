# Bloom Care OR Take-home Test

## Overview
This project is structured using modern Python development practices and tooling.

## Setup

### Prerequisites
- Python 3.11+ (recommended)
- Poetry (for dependency management)

### Installation

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Development

### Running the application
```bash
poetry run python -m bloom_care_takehome
```

### Running tests
```bash
poetry run pytest
```

### Code formatting and linting
```bash
# Format code
poetry run black .
poetry run isort .

# Lint code
poetry run ruff check .
poetry run mypy .
```

### Pre-commit hooks
```bash
# Install pre-commit hooks
poetry run pre-commit install

# Run all hooks manually
poetry run pre-commit run --all-files
```

## Project Structure
```
bloom-care-takehome/
├── bloom_care_takehome/     # Main package
│   ├── __init__.py
│   └── main.py
├── tests/                   # Test files
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml          # Project configuration
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## Technologies Used
- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **black**: Code formatting
- **isort**: Import sorting
- **ruff**: Fast Python linter
- **mypy**: Static type checking
- **pre-commit**: Git hooks for code quality
