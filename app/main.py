from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection

from .types import AggregationResult, GroupType
from .exceptions import InvlidGroupError
from .dateutils import parse_datetime


def get_mongo_group(group_type: GroupType) -> dict[str, dict[str, str]]:
    """Get mongo aggregation `$group._id` object for futher grouping.

    Args:
    - group_type (GroupType): Group type.

    Returns:
    - dict[str, dict[str, str]]: Mongo aggregation `$group._id` object.
    """
    match group_type:
        case GroupType.YEAR:
            return {
                "year": {"$year": "$dt"},
            }
        case GroupType.MONTH:
            return {
                "year": {"$year": "$dt"},
                "month": {"$month": "$dt"},
            }
        case GroupType.DAY:
            return {
                "year": {"$year": "$dt"},
                "month": {"$month": "$dt"},
                "day": {"$dayOfMonth": "$dt"},
            }
        case GroupType.HOUR:
            return {
                "year": {"$year": "$dt"},
                "month": {"$month": "$dt"},
                "day": {"$dayOfMonth": "$dt"},
                "hour": {"$hour": "$dt"},
            }
        case _:
            raise InvlidGroupError(group_type)


async def get_records_within_time_range(
    collection: AsyncIOMotorCollection,
    start_time: str | datetime,
    end_time: str | datetime,
    group_type: GroupType,
) -> AggregationResult:
    """
    This function retrieves records from a MongoDB collection within a specified time range and groups them based on a given group type.
    It uses MongoDB aggregation pipeline stages to perform the grouping and aggregation operations.

    Args:
    - collection (AsyncIOMotorCollection): The MongoDB collection to query.
    - start_time (str | datetime): The start time of the time range. Can be a string or a datetime object.
    - end_time (str | datetime): The end time of the time range. Can be a string or a datetime object.
    - group_type (GroupType): The type of grouping to perform.

    Returns:
    - AggregationResult: An object containing the grouped records and labels.

    Raises:
    - InvlidGroupError: If the provided group type is not valid.
    """
    start_datetime = parse_datetime(start_time)
    end_datetime = parse_datetime(end_time)

    # Pipeline
    match_documents = {
        "$match": {
            "dt": {
                "$gte": start_datetime,
                "$lte": end_datetime,
            }
        }
    }
    group_documents = {
        "$group": {
            "_id": get_mongo_group(group_type),
            "total_value": {"$sum": "$value"},
            "count": {"$count": {}},
        },
    }
    sort_documents = {
        "$sort": {
            "_id": 1,
        }
    }
    # Adds a 'label' field to each document that contains ISO datetime string, used for labels later
    add_label = {
        "$project": {
            "total_value": 1,
            "label": {
                "$dateFromParts": {
                    "year": "$_id.year",
                    "month": {"$ifNull": ["$_id.month", 1]},
                    "day": {"$ifNull": ["$_id.day", 1]},
                    "hour": {"$ifNull": ["$_id.hour", 0]},
                    "minute": {"$ifNull": ["$_id.minute", 0]},
                    "second": {"$ifNull": ["$_id.second", 0]},
                    "millisecond": {"$ifNull": ["$_id.millisecond", 0]},
                    "timezone": "+00:00",
                }
            },
        }
    }
    add_dataset_and_labels = {
        "$group": {
            "_id": None,
            "dataset": {
                "$push": "$total_value",
            },
            "labels": {
                "$push": "$label",
            },
        }
    }
    filter_out_id = {
        "$project": {
            "_id": 0,
        }
    }

    cursor = collection.aggregate(
        [
            match_documents,
            group_documents,
            sort_documents,
            add_label,
            add_dataset_and_labels,
            filter_out_id,
        ]
    )
    grouped_records: dict = await cursor.next()

    return AggregationResult(**grouped_records)
