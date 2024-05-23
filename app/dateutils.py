from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta


def parse_datetime(source: datetime | str) -> datetime:
    """
    Parses a datetime object or string into a datetime object.

    Args:
    - source (datetime | str): The datetime object or string to parse.

    Returns:
    - datetime: The parsed datetime object.

    Raises:
    - ValueError: If the input is neither a datetime object nor a valid datetime string.
    """
    return source if isinstance(source, datetime) else datetime.fromisoformat(source)


def datetime_to_iso(source: datetime, drop_timezone: bool = False) -> str:
    """
    Converts a datetime object to an ISO 8601 formatted string.

    Args:
    - source (datetime): The datetime object to convert.

    Returns:
    - str: The ISO 8601 formatted string representation of the datetime object.

    Raises:
    - ValueError: If the input is not a datetime object.
    """
    if not isinstance(source, datetime):
        raise ValueError("Input must be a datetime object.")

    result = source.replace(tzinfo=timezone.utc).isoformat()

    if drop_timezone:
        return result.replace("+00:00", "")

    return result


def get_datetime_range(
    start_datetime: datetime,
    end_datetime: datetime,
    delta: relativedelta,
    tzinfo: timezone | None = None,
) -> list[datetime]:
    """
    Generates a list of datetime objects within a specified range, with a given time delta increment.

    Args:
    - start_datetime (datetime): The start datetime object.
    - end_datetime (datetime): The end datetime object.
    - delta (relativedelta): The time delta increment.
    - tzinfo (timezone | None): The timezone object, if desired. Defaults to None.

    Returns:
    - list[datetime]: A list of datetime objects within the specified range, incremented by the given time delta.

    Raises:
    - ValueError: If the input is not a datetime object.
    """
    result: list[datetime] = []

    current_date = start_datetime
    while current_date <= end_datetime:
        if tzinfo:
            current_date = current_date.replace(tzinfo=tzinfo)
        result.append(current_date)
        current_date += delta

    return result
