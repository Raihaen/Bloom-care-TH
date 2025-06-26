# Bloom Care OR Take-home Test

## 🎯 Assignment Overview

Welcome to **Bloom Care** — you've just joined the team, on a mission to improve the daily lives of homecare professionals and the people they support.

You are tasked with building a **staff scheduler** to help our clients optimise their schedules. The agency needs to assign caregivers to shifts throughout a week, considering a few constraints.

**Your goal**: Assign workers to shifts while satisfying constraints and optionally optimizing for some extra criteria.

### **Given**:

- A list of **caregivers**, each with:
  - A weekly **availability** (e.g Monday 8h-12h, Tuesday 8h-18h, …)
  - A **maximum weekly working time** (e.g. 35h)
  - Skills (e.g. "cooking", "hygiene", "cleaning")
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

Once the basics work, if you still have some time, you can try optimizing further. Pick one or more of these:

- **Continuity of care**: minimize the number of different caregivers assigned to the same customer across multiple days (clients prefer familiar faces!)
- **Travel efficiency**: minimize how often caregivers switch **neighborhoods** during a single day (less travel time = better quality of life for caregivers)

### Instructions

Please try to not spend more than 5 hours on this assignment.

#### Expected output

Your solver should return a list of assignments. Run `poetry run python -m scheduler` to evaluate your output (see [CONTRIBUTING.md](CONTRIBUTING.md))

```python
  assignments = [
    {
      visit_id: "V1",
      caregiver_id: "C1"
    },
    {
      visit_id: "V2",
      caregiver_id: "C2"
    },
    # and so on...
  ]
```

#### How to Successfully Complete this Technical Assignment

- [ ] Clone this repository (do **not** fork it)
- [ ] Implement the features step-by-step (your commit history should be clear to follow)
- [ ] Feel free to add files and folders and reorganise the code as you wish. Right now, it is set up so that you mostly just need to touch to the solver (`solver.py`) part.
- [ ] Document your choices along the way, as you'll have to present them in the debrief interview
- [ ] Provide clear instructions on how we can run your code
- [ ] Publish it on GitHub (or equivalent)
- [ ] Send us the link, along with an estimate of how much time you spent on this assignment

#### What you will be evaluated on

- [ ] You followed the instructions
- [ ] Your architecture and design choices are clearly documented
- [ ] Correctness: Are all constraints respected?
- [ ] Clarity: Is the code readable and well-explained?
- [ ] Modeling: Did you structure the problem thoughtfully?
- [ ] Tests are included and runnable

### Guidelines

**Assumptions**

If anything is unclear, you can make reasonable assumptions and document them

**Use of AI is allowed**

Feel free to use AI.

**Choose your stack**

You can use any tool and language you deem suitable. If you don't know where to start, you can use `CP-SAT` from `OR-Tools`.

**End state**

The last state of your code should be clean and ready to be reviewed by peers in a real-world situation

**Enjoy the assignment and good luck!**

---

## Documentation

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Development help and code quality standards
- **[SCORING.md](SCORING.md)**: Detailed explanation of how your solution is evaluated and scored
