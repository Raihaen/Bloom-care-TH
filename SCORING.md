# Bloom Care Scheduling - Evaluation & Scoring Guide

This document explains how your scheduling solution is evaluated and scored.

## Overview

The evaluation system checks both **constraint compliance** and **optimization quality**. Your solution must satisfy all constraints to be considered valid, and the optimization metrics help assess the quality of your solution.

## Constraint Validation

### Core Requirements (Must Pass)

1. **All Visits Assigned**

   - Every visit must have exactly one caregiver assigned
   - Unassigned visits are listed in `unassigned_visits`

2. **Availability Compliance**

   - Caregivers can only be assigned to shifts during their available times
   - Violations are listed in `availability_violations`

3. **No Overlapping Shifts**

   - No caregiver can be assigned to overlapping shifts on the same day
   - Violations are listed in `overlap_violations` with conflicting visit pairs

4. **Maximum Hours Compliance**
   - No caregiver can exceed their weekly hour limit
   - Violations are listed in `max_hours_violations` with actual vs max hours

## Optimization Metrics

### 1. Continuity of Care Score (0.0 - 1.0)

**Goal**: Minimize the number of different caregivers assigned to the same customer across multiple days.

**Calculation**:

- For each customer, calculate: `1.0 - (unique_caregivers / total_visits)`
- Average the scores across all customers
- Single visits get a perfect score of 1.0

**Example**:

- Marie-Anne has 6 visits assigned to 2 different caregivers
- Score: `1.0 - (2/6) = 0.67`
- Pauline has 4 visits assigned to 1 caregiver
- Score: `1.0 - (1/4) = 0.75`
- Overall continuity score = average of all customer scores

**Interpretation**:

- **1.0**: Perfect continuity (each customer has only one caregiver)
- **0.8+**: Good continuity
- **0.6-0.8**: Moderate continuity
- **<0.6**: Poor continuity (many different caregivers per customer)

### 2. Travel Efficiency Score (0.0 - 1.0)

**Goal**: Minimize neighborhood switches per caregiver per day.

**Calculation**:

- For each caregiver-day combination, count neighborhood switches
- Calculate average switches per caregiver per day
- Score: `max(0.0, 1.0 - (avg_switches / 2.0))`
- Single visits per day get a perfect score

**Example**:

- Caregiver C1 on Monday: visits Centre-ville → Sud → Nord (2 switches)
- Caregiver C2 on Monday: visits Nord only (0 switches)
- Average: 1.0 switches per caregiver per day
- Score: `1.0 - (1.0/2.0) = 0.5`

**Interpretation**:

- **1.0**: Perfect efficiency (no neighborhood switches)
- **0.8+**: Good efficiency (few switches)
- **0.5-0.8**: Moderate efficiency
- **<0.5**: Poor efficiency (many neighborhood switches)

## Evaluation Output

The evaluator returns a dictionary with:

```json
{
  "constraint_violations": {
    "unassigned_visits": ["V1", "V5"],
    "availability_violations": [{ "visit_id": "V2", "caregiver_id": "C1" }],
    "overlap_violations": [
      { "caregiver_id": "C2", "conflicting_visits": ["V3", "V4"] }
    ],
    "max_hours_violations": [
      { "caregiver_id": "C3", "assigned_hours": 38, "max_hours": 35 }
    ]
  },
  "optimization_metrics": {
    "continuity_score": 0.78,
    "travel_efficiency_score": 0.85
  }
}
```

## Success Criteria

### Minimum Requirements

- ✅ All constraint violations must be empty
- ✅ All visits must be assigned
- ✅ All assignments must respect availability, overlaps, and max hours

### Quality Indicators

- **Continuity Score**: Aim for 0.8+ for good customer experience
- **Travel Efficiency**: Aim for 0.8+ for caregiver quality of life

## Tips for Optimization

1. **For Continuity**: Try to assign the same caregiver to the same customer across multiple days
2. **For Travel Efficiency**: Group visits by neighborhood when possible, or minimize switches within the same day
3. **Balance**: Sometimes you need to trade off between continuity and travel efficiency
4. **Constraints First**: Always ensure all constraints are satisfied before optimizing

## Example Scoring

| Scenario            | Continuity | Travel Efficiency | Quality           |
| ------------------- | ---------- | ----------------- | ----------------- |
| Perfect solution    | 0.95       | 0.90              | Excellent         |
| Good solution       | 0.80       | 0.75              | Good              |
| Acceptable solution | 0.65       | 0.60              | Acceptable        |
| Poor solution       | 0.40       | 0.30              | Needs improvement |

Remember: **Constraints must be satisfied first**. Optimization metrics only matter if your solution is valid!
