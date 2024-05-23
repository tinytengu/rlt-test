# rlt-test

Тестовое задание для RLT.

Ссылка на тестовое: https://docs.google.com/document/d/14DcCb6Pj3PNsFqJzaS_hAhyePqRXF6uvmTzobp_G8PM/edit

# 0. Инструментарий
- [Python 3.12.3](https://www.python.org/downloads/release/python-3123/)
- Виртуальное окружение - [Poetry](https://python-poetry.org)
- Контроль PEP8 - [pycodestyle](https://pypi.org/project/pycodestyle/)
- Форматирование кода - [ruff](https://pypi.org/project/ruff/)
- Тестирование кода - [unittest](https://docs.python.org/3/library/unittest.html)
- Асинхронное взаимодействие с MongoDB - [motor](https://pypi.org/project/motor/)
- Асинхронный бот Telegram - [aiogram](https://pypi.org/project/aiogram/)

# 1. Запуск
## 1.1 Создание и активация виртуального окружения
### Poetry
```bash
poetry new
poetry shell # Опционально
```
### venv
```bash
# Unix
python3.12 -m venv venv
source venv/bin/activate

# Windows Powershell
python -m venv .venv
.\.venv\Scripts\activate
```

## 1.2 Установка зависимостей
### Poetry
```bash
poetry install
```
### venv
```bash
pip install -r requirements.txt
```

# 2. Тестирование
```bash
python -m unittest
```