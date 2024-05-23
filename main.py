import asyncio

from app.main import get_records_within_time_range
from app.db import database
from app.dateutils import datetime_to_iso


async def main():
    input_data = {
        "start_time": "2022-02-01T00:00:00",
        "end_time": "2022-02-02T00:00:00",
        "group_type": "hour",
    }

    output = await get_records_within_time_range(
        collection=database.salary, **input_data
    )
    result = {
        "dataset": output.dataset,
        "labels": [datetime_to_iso(label) for label in output.labels],
    }
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
