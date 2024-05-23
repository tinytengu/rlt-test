import asyncio
import logging
import json
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from app import get_records_within_time_range
from app.dateutils import parse_datetime, datetime_to_iso
from app.exceptions import InvlidGroupError
from app.types import GroupType
from app.db import database

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=getenv("BOT_TOKEN", ""))
dp = Dispatcher()


class JsonFilter(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        try:
            data = json.loads(str(message.text))
            return len(data) == 3 and all(
                key in data for key in ("dt_from", "dt_upto", "group_type")
            )
        except json.decoder.JSONDecodeError:
            return False


@dp.message(JsonFilter())
async def json_message(message: Message):
    data = json.loads(str(message.text))

    try:
        output = await get_records_within_time_range(
            collection=database.salary,
            start_time=parse_datetime(data["dt_from"]),
            end_time=parse_datetime(data["dt_upto"]),
            group_type=data["group_type"],
        )
    except InvlidGroupError as e:
        await message.answer(
            "* Неверный тип группировки: '{}'.\nДоступные варианты:\n{}".format(
                e.group_type, "\n".join([f"- {item}" for item in GroupType.values()])
            )
        )
        return
    except Exception as e:
        await message.answer("* Ошибка: `{}`".format(e))
        return

    result = {
        "dataset": output.dataset,
        "labels": [
            datetime_to_iso(label, drop_timezone=True) for label in output.labels
        ],
    }
    await message.answer(json.dumps(result, ensure_ascii=False))


@dp.message(~JsonFilter())
async def non_json_message(message: Message):
    example = '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}'
    await message.answer(
        f"* Неверный формат входных данных.\n\n<b>Пример</b>:\n<pre>{example}</pre>",
        parse_mode=ParseMode.HTML,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
