"""Tests for the main module."""

from datetime import datetime, time

from scheduler.models import Availability, Visit


def test_check_availability() -> None:
    """Test the Availability.check_availability method."""
    # Create a Monday availability from 9:00 to 17:00
    availability = Availability(
        day="MONDAY",
        start=time(9, 0),  # 09:00
        end=time(17, 0),  # 17:00
    )

    # Test 1: Visit within availability window (should return True)
    visit_within = Visit(
        id="V1",
        start=datetime(2025, 6, 23, 10, 0),  # Monday 10:00
        end=datetime(2025, 6, 23, 12, 0),  # Monday 12:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert availability.check_availability(visit_within)

    # Test 2: Visit outside availability window (should return False)
    visit_outside = Visit(
        id="V2",
        start=datetime(2025, 6, 23, 18, 0),  # Monday 18:00 (after availability)
        end=datetime(2025, 6, 23, 20, 0),  # Monday 20:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert not availability.check_availability(visit_outside)

    # Test 3: Visit on different day (should return False)
    visit_different_day = Visit(
        id="V3",
        start=datetime(2025, 6, 24, 10, 0),  # Tuesday 10:00
        end=datetime(2025, 6, 24, 12, 0),  # Tuesday 12:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert not availability.check_availability(visit_different_day)


def test_visit_overlaps():
    """Test the Visit.overlaps method for various overlap scenarios."""
    base = Visit(
        id="base",
        start=datetime(2025, 6, 23, 10, 0),  # 10:00
        end=datetime(2025, 6, 23, 12, 0),  # 12:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )

    # 1. Overlap partially at the start
    overlap_start = Visit(
        id="overlap_start",
        start=datetime(2025, 6, 23, 9, 0),  # 09:00
        end=datetime(2025, 6, 23, 11, 0),  # 11:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert base.overlaps(overlap_start)
    assert overlap_start.overlaps(base)

    # 2. Overlap partially at the end
    overlap_end = Visit(
        id="overlap_end",
        start=datetime(2025, 6, 23, 11, 0),  # 11:00
        end=datetime(2025, 6, 23, 13, 0),  # 13:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert base.overlaps(overlap_end)
    assert overlap_end.overlaps(base)

    # 3. One visit contains the other
    containing = Visit(
        id="containing",
        start=datetime(2025, 6, 23, 9, 0),  # 09:00
        end=datetime(2025, 6, 23, 13, 0),  # 13:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert base.overlaps(containing)
    assert containing.overlaps(base)

    # 4. Visits don't overlap at all
    no_overlap = Visit(
        id="no_overlap",
        start=datetime(2025, 6, 23, 13, 0),  # 13:00
        end=datetime(2025, 6, 23, 14, 0),  # 14:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert not base.overlaps(no_overlap)
    assert not no_overlap.overlaps(base)

    # 5. Visits finish and start at the same time (edge case)
    edge_case = Visit(
        id="edge_case",
        start=datetime(2025, 6, 23, 12, 0),  # 12:00
        end=datetime(2025, 6, 23, 13, 0),  # 13:00
        customer="Test Customer",
        required_skill="test",
        neighborhood="test",
    )
    assert not base.overlaps(edge_case)
    assert not edge_case.overlaps(base)
