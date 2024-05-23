from typing import Any

from motor.motor_asyncio import AsyncIOMotorCollection

from app.main import get_records_within_time_range
from app.dateutils import datetime_to_iso


async def process_input(
    collection: AsyncIOMotorCollection, input_data: dict
) -> dict[str, Any]:
    output = await get_records_within_time_range(
        collection=collection,
        start_time=input_data["dt_from"],
        end_time=input_data["dt_upto"],
        group_type=input_data["group_type"],
    )

    return {
        "dataset": output.dataset,
        "labels": [
            datetime_to_iso(label, drop_timezone=True) for label in output.labels
        ],
    }
