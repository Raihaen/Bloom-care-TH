# Contributing to Bloom Care OR Take-home

## Quick Start

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
poetry run python -m scheduler
```

### Running tests

```bash
poetry run pytest
```

### Code Formatting and linting

We use several tools to maintain consistent code formatting:

#### Black (Code Formatter)

```bash
# Format all Python files
poetry run black .
```

#### isort (Import Sorter)

```bash
# Sort imports in all Python files
poetry run isort .
```

#### Ruff (Fast Python Linter)

```bash
# Run linting checks
poetry run ruff check .

# Fix automatically fixable issues
poetry run ruff check --fix .
```

#### MyPy (Static Type Checker)

```bash
# Run type checking
poetry run mypy .

# Check specific files
poetry run mypy bloom_care_takehome/
```

## Technologies Used

- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **black**: Code formatting
- **isort**: Import sorting
- **ruff**: Fast Python linter
- **mypy**: Static type checking
- **pre-commit**: Git hooks for code quality

## Getting Help

If you encounter any issues with the development setup or have questions about the code quality standards, please refer to:

- [Black documentation](https://black.readthedocs.io/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [MyPy documentation](https://mypy.readthedocs.io/)
- [pytest documentation](https://docs.pytest.org/)
