from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


@dataclass(frozen=False)
class AggregationResult:
    """Used for `get_records_within_time_range` result."""

    dataset: list[int | float]
    labels: list[datetime]


class GroupType(StrEnum):
    """The type of grouping to perform."""

    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    HOUR = "hour"

    @classmethod
    def values(cls) -> list[str]:
        """Get all values of the enum."""
        return [item.value for item in cls]
