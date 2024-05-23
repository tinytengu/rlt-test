import unittest
from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

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


class HourTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        client = AsyncIOMotorClient("mongodb://localhost:27017/")
        self.database = client.testdb
        self.collection = self.database.salary

    async def test_case0(self):
        input_data = {
            "dt_from": "2022-09-01T00:00:00",
            "dt_upto": "2022-12-31T23:59:00",
            "group_type": "month",
        }

        expected_result = {
            "dataset": [5906586, 5515874, 5889803, 6092634],
            "labels": [
                "2022-09-01T00:00:00",
                "2022-10-01T00:00:00",
                "2022-11-01T00:00:00",
                "2022-12-01T00:00:00",
            ],
        }
        result = await process_input(self.collection, input_data)

        self.assertEqual(result, expected_result)

    async def test_case1(self):
        input_data = {
            "dt_from": "2022-09-01T00:00:00",
            "dt_upto": "2022-12-31T23:59:00",
            "group_type": "month",
        }

        expected_result = {
            "dataset": [5906586, 5515874, 5889803, 6092634],
            "labels": [
                "2022-09-01T00:00:00",
                "2022-10-01T00:00:00",
                "2022-11-01T00:00:00",
                "2022-12-01T00:00:00",
            ],
        }

        result = await process_input(self.collection, input_data)

        self.assertEqual(result, expected_result)

    async def test_case2(self):
        input_data = {
            "dt_from": "2022-10-01T00:00:00",
            "dt_upto": "2022-11-30T23:59:00",
            "group_type": "day",
        }

        expected_result = {
            "dataset": [
                0,
                0,
                0,
                195028,
                190610,
                193448,
                203057,
                208605,
                191361,
                186224,
                181561,
                195264,
                213854,
                194070,
                208372,
                184966,
                196745,
                185221,
                196197,
                200647,
                196755,
                221695,
                189114,
                204853,
                194652,
                188096,
                215141,
                185000,
                206936,
                200164,
                188238,
                195279,
                191601,
                201722,
                207361,
                184391,
                203336,
                205045,
                202717,
                182251,
                185631,
                186703,
                193604,
                204879,
                201341,
                202654,
                183856,
                207001,
                204274,
                204119,
                188486,
                191392,
                184199,
                202045,
                193454,
                198738,
                205226,
                188764,
                191233,
                193167,
                205334,
            ],
            "labels": [
                "2022-10-01T00:00:00",
                "2022-10-02T00:00:00",
                "2022-10-03T00:00:00",
                "2022-10-04T00:00:00",
                "2022-10-05T00:00:00",
                "2022-10-06T00:00:00",
                "2022-10-07T00:00:00",
                "2022-10-08T00:00:00",
                "2022-10-09T00:00:00",
                "2022-10-10T00:00:00",
                "2022-10-11T00:00:00",
                "2022-10-12T00:00:00",
                "2022-10-13T00:00:00",
                "2022-10-14T00:00:00",
                "2022-10-15T00:00:00",
                "2022-10-16T00:00:00",
                "2022-10-17T00:00:00",
                "2022-10-18T00:00:00",
                "2022-10-19T00:00:00",
                "2022-10-20T00:00:00",
                "2022-10-21T00:00:00",
                "2022-10-22T00:00:00",
                "2022-10-23T00:00:00",
                "2022-10-24T00:00:00",
                "2022-10-25T00:00:00",
                "2022-10-26T00:00:00",
                "2022-10-27T00:00:00",
                "2022-10-28T00:00:00",
                "2022-10-29T00:00:00",
                "2022-10-30T00:00:00",
                "2022-10-31T00:00:00",
                "2022-11-01T00:00:00",
                "2022-11-02T00:00:00",
                "2022-11-03T00:00:00",
                "2022-11-04T00:00:00",
                "2022-11-05T00:00:00",
                "2022-11-06T00:00:00",
                "2022-11-07T00:00:00",
                "2022-11-08T00:00:00",
                "2022-11-09T00:00:00",
                "2022-11-10T00:00:00",
                "2022-11-11T00:00:00",
                "2022-11-12T00:00:00",
                "2022-11-13T00:00:00",
                "2022-11-14T00:00:00",
                "2022-11-15T00:00:00",
                "2022-11-16T00:00:00",
                "2022-11-17T00:00:00",
                "2022-11-18T00:00:00",
                "2022-11-19T00:00:00",
                "2022-11-20T00:00:00",
                "2022-11-21T00:00:00",
                "2022-11-22T00:00:00",
                "2022-11-23T00:00:00",
                "2022-11-24T00:00:00",
                "2022-11-25T00:00:00",
                "2022-11-26T00:00:00",
                "2022-11-27T00:00:00",
                "2022-11-28T00:00:00",
                "2022-11-29T00:00:00",
                "2022-11-30T00:00:00",
            ],
        }

        result = await process_input(self.collection, input_data)

        self.assertEqual(result, expected_result)

    async def test_case3(self):
        input_data = {
            "dt_from": "2022-02-01T00:00:00",
            "dt_upto": "2022-02-02T00:00:00",
            "group_type": "hour",
        }

        expected_result = {
            "dataset": [
                8177,
                8407,
                4868,
                7706,
                8353,
                7143,
                6062,
                11800,
                4077,
                8820,
                4788,
                11045,
                13048,
                2729,
                4038,
                9888,
                7490,
                11644,
                11232,
                12177,
                2741,
                5341,
                8730,
                4718,
                0,
            ],
            "labels": [
                "2022-02-01T00:00:00",
                "2022-02-01T01:00:00",
                "2022-02-01T02:00:00",
                "2022-02-01T03:00:00",
                "2022-02-01T04:00:00",
                "2022-02-01T05:00:00",
                "2022-02-01T06:00:00",
                "2022-02-01T07:00:00",
                "2022-02-01T08:00:00",
                "2022-02-01T09:00:00",
                "2022-02-01T10:00:00",
                "2022-02-01T11:00:00",
                "2022-02-01T12:00:00",
                "2022-02-01T13:00:00",
                "2022-02-01T14:00:00",
                "2022-02-01T15:00:00",
                "2022-02-01T16:00:00",
                "2022-02-01T17:00:00",
                "2022-02-01T18:00:00",
                "2022-02-01T19:00:00",
                "2022-02-01T20:00:00",
                "2022-02-01T21:00:00",
                "2022-02-01T22:00:00",
                "2022-02-01T23:00:00",
                "2022-02-02T00:00:00",
            ],
        }

        result = await process_input(self.collection, input_data)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
