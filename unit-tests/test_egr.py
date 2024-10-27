"""Test egr."""

# external
import pytest

# local
from src.fns.egr import egr


@pytest.mark.parametrize(
    ("value",),
    [
        ("7736050003",),
        (None,),
    ],
)
def test_returns_success_response(value: str):
    assert egr(value)
