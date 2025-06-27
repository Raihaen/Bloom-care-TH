import json
from datetime import datetime

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
            start=datetime.strptime(visit_data["start"], "%Y-%m-%d %H:%M"),
            end=datetime.strptime(visit_data["end"], "%Y-%m-%d %H:%M"),
            customer=visit_data["customer"],
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
            # Parse time strings to datetime objects (using a dummy date)
            start_time = datetime.strptime(avail_data["start"], "%H:%M").time()
            end_time = datetime.strptime(avail_data["end"], "%H:%M").time()

            availability = Availability(
                day=avail_data["day"],
                start=start_time,
                end=end_time,
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
