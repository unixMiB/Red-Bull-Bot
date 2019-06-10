FROM python:3-windowsservercore-1809

WORKDIR C:/

COPY requirements.txt ./

RUN "pip3 install --no-cache-dir -r requirements.txt"

VOLUME C:/pic

ENV BOT_TOKEN=

COPY . .

CMD ["python", "bot.py"]