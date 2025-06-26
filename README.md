# Bloom Care OR Take-home Test

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

## Brief - Shift Scheduling with Constraints

### 🎯 Objective

Welcome to **Bloom Care** — you’ve just joined the team, on a mission to improve the daily lives of homecare professionals and the people they support.

You are tasked with building a **staff scheduler** to help our clients optimise their schedules. The agency needs to assign caregivers to shifts throughout a week, considering a few constraints:

Your goal is to **assign workers to shifts** while satisfying constraints and optionally optimizing for some extra criteria.

### **Given**:

- A list of **caregivers**, each with:
  - A weekly **availability** (e.g Monday 8h-12h, Tuesday 8h-18h, …)
  - A **maximum weekly working time** (e.g. 35h)
  - Skills (e.g. “cooking”, “hygiene”, “cleaning”)
- A list of **shifts**, each defined by:
  - A start and end time
  - Required **skill**
  - A neighborhood

### Core Requirements

- Each **shift is fully staffed** (required number of caregivers assigned)
- Each caregiver is only assigned to shifts they are **available** for
- No caregiver is assigned to **overlapping shifts**
- No caregiver works **more than their max hours per week**

### 🚀 Bonus Objectives (stretch)

Once the basics work, try optimizing further. Pick **one** or more of these:

- **Continuity of care**: minimize the number of different caregivers assigned to the same customer across multiple days (clients prefer familiar faces!)
- **Travel efficiency**: minimize how often caregivers switch **neighborhoods** during a single day (less travel time = better quality of life for caregivers)

# Instructions

Please try to not spend more than 5 hours on this assignment.

### **How to Successfully Complete this Technical Assignment**

- [ ] Clone this repository (do **not** fork it)
- [ ] Implement the features step-by-step (your commit history should be clear to follow)
- [ ] Document your choices along the way, as you’ll have to present them in the debrief interview
- [ ] Provide clear instructions on how we can run your code
- [ ] Publish it on GitHub (or equivalent)
- [ ] Send us the link, along with an estimate of how much time you spent on this assignment

### Guidelines

**Assumptions**

If anything is unclear, you can make reasonable assumptions and document them

**Use of AI is allowed**

Feel free to use AI.

**Choose your stack**

You can use any tool and language you deem suitable.

**End state**

The last state of your code should be clean and ready to be reviewed by peers in a real-world situation

### What you will be evaluated on

- [ ] You followed the instructions
- [ ] Your architecture and design choices are clearly documented
- [ ] Correctness: Are all constraints respected?
- [ ] Clarity: Is the code readable and well-explained?
- [ ] Modeling: Did you structure the problem thoughtfully?
- [ ] Tests are included and runnable

**Enjoy the assignment and good luck!**
