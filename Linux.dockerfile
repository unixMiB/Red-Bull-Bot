FROM python:3-slim

SHELL [ "bash" ]

COPY requirements.txt .

RUN "pip3 install --no-cache-dir -r requirements.txt"

VOLUME /pic

ENV BOT_TOKEN=

COPY . .

CMD ["python", "bot.py"]