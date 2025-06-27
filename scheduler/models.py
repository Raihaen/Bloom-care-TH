"""Data models for Bloom Care OR Take-home Test."""

from dataclasses import dataclass
from datetime import datetime, time


@dataclass
class Visit:
    """Represents a visit/shift that needs to be staffed."""

    id: str
    start: datetime  # Format: "YYYY-MM-DD HH:MM" parsed to datetime
    end: datetime  # Format: "YYYY-MM-DD HH:MM" parsed to datetime
    customer: str
    required_skill: str
    neighborhood: str

    def overlaps(self, other: "Visit") -> bool:
        """Check if the visit overlaps with another visit."""
        # they can overlap at the start or end, or one can be contained in the other
        # or the other can be contained in one
        return (
            # other visit completely contains this visit
            (other.start <= self.start and self.end <= other.end)
            or
            # this visit completely contains other visit
            (self.start <= other.start and other.end <= self.end)
            or
            # other visit overlaps the beginning
            (other.start <= self.start and self.start < other.end)
            or
            # other visit overlaps the end
            (other.start < self.end and self.end <= other.end)
        )


@dataclass
class Availability:
    """Represents a caregiver's availability for a specific day."""

    day: str
    # "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
    start: time
    end: time

    def check_availability(self, visit: Visit) -> bool:
        """Check if the availability overlaps with the visit."""
        # 1. check if the visit start is the same day of the week as the day string
        if visit.start.strftime("%A").upper() != self.day:
            return False

        # 2. check that both start and end are in the availability
        visit_start_time = visit.start.time()
        visit_end_time = visit.end.time()

        # Both start and end times must be within availability window
        return self.start <= visit_start_time and visit_end_time <= self.end


@dataclass
class Caregiver:
    """Represents a caregiver with their availability and skills."""

    id: str
    name: str
    max_hours: int
    availability: list[Availability]
    skills: list[str]


@dataclass
class Assignment:
    """Represents the assignment of a caregiver to a visit."""

    visit_id: str
    caregiver_id: str
