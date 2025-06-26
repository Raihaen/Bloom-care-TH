"""Data models for Bloom Care OR Take-home Test."""

from dataclasses import dataclass


@dataclass
class Visit:
    """Represents a visit/shift that needs to be staffed."""

    id: str
    day: str
    start: str
    end: str
    customer: str
    required_skill: str
    neighborhood: str


@dataclass
class Availability:
    """Represents a caregiver's availability for a specific day."""

    day: str
    start: str
    end: str


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
