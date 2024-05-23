from datetime import datetime, timezone


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


def datetime_to_iso(source: datetime) -> str:
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
    return source.replace(tzinfo=timezone.utc).isoformat()
