"""Test fake package."""
from module2 import func2, func3  # type: ignore


def test_fakepkg():
    assert func2() == 2
    assert func3() == 3
