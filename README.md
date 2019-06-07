# Red Bull Telegram Bot

![Docker Pulls](https://img.shields.io/docker/pulls/unixmib/redbull.svg)
![GitHub](https://img.shields.io/github/license/unixmib/red-bull-bot.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/unixmib/red-bull-bot.svg)
![GitHub issues](https://img.shields.io/github/issues/unixmib/red-bull-bot.svg)

## Usage

Open a chat on thelegram with [@UnixMib_RedBull_Bot](https://t.me/UnixMib_RedBull_Bot)

[![UnixMib_RedBull_Bot](https://img.shields.io/badge/telegram-%40UnixMib__RedBull__Bot-blue.svg)](https://t.me/UnixMib_RedBull_Bot)

## Deploy

You need to set the environmen variable `BOT_TOKEN` with a token from [@BotFather](https://t.me/botfather)

[![@BotFather](https://img.shields.io/badge/telegram-%40BotFather-blue.svg)](https://t.me/botfather)

```bash
pip3 install -r requirements.txt
python3 bot.py
```

## Docker images

### Docker container tags

-  `190607-slim`, `slim` (190318/slim)

-  `190607-windowsservercore-1809`, `windowsservercore-1809` (190318/windows/servercore/1809)

### Shared tags

- `latest`
- `190607`
  - Debian Strech Slim
  - Windows Server Core 1809
