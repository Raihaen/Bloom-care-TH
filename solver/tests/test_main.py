"""Tests for the main module."""

from solver.main import hello_world


def test_hello_world() -> None:
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello, Bloom Care OR!"
    assert isinstance(result, str)


def test_hello_world_not_empty() -> None:
    """Test that hello_world returns a non-empty string."""
    result = hello_world()
    assert len(result) > 0
