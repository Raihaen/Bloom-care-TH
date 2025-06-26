"""Main module for Bloom Care OR Take-home Test."""

import json

from .models import Availability, Caregiver, Visit


def load_visits(file_path: str = "inputs/visits.json") -> list[Visit]:
    """Load visits from JSON file.

    Args:
        file_path: Path to the visits JSON file

    Returns:
        List of Visit objects
    """
    with open(file_path) as f:
        data = json.load(f)

    visits = []
    for visit_data in data:
        visit = Visit(
            id=visit_data["id"],
            day=visit_data["day"],
            start=visit_data["start"],
            end=visit_data["end"],
            required_skill=visit_data["required_skill"],
            neighborhood=visit_data["neighborhood"],
        )
        visits.append(visit)

    return visits


def load_caregivers(file_path: str = "inputs/caregivers.json") -> list[Caregiver]:
    """Load caregivers from JSON file.

    Args:
        file_path: Path to the caregivers JSON file

    Returns:
        List of Caregiver objects
    """
    with open(file_path) as f:
        data = json.load(f)

    caregivers = []
    for caregiver_data in data:
        availability_list = []
        for avail_data in caregiver_data["availability"]:
            availability = Availability(
                day=avail_data["day"], start=avail_data["start"], end=avail_data["end"]
            )
            availability_list.append(availability)

        caregiver = Caregiver(
            id=caregiver_data["id"],
            name=caregiver_data["name"],
            max_hours=caregiver_data["max_hours"],
            availability=availability_list,
            skills=caregiver_data["skills"],
        )
        caregivers.append(caregiver)

    return caregivers


def main() -> None:
    """Main entry point for the application."""
    # Load the data
    visits = load_visits()
    caregivers = load_caregivers()

    print(f"Loaded {len(visits)} visits and {len(caregivers)} caregivers")


if __name__ == "__main__":
    main()
