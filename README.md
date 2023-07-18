# Discord Bot for ClickUp Tasks

This is a simple Discord bot built using discord.py that reads messages from a specific channel and creates tasks in ClickUp based on the message content or embed titles containing "down."

## Requirements

- Python 3.x
- discord.py library
- requests library

## Setup

1. Clone this repository to your local machine using:

```bash
git clone https://github.com/your-username/discord-bot-clickup-tasks.git
```
Install the required libraries:

```bash
pip install discord.py requests
```
Obtain your Discord bot token and ClickUp API key. Replace 'YOUR_BOT_TOKEN' and 'YOUR_CLICKUP_API_KEY' with your actual tokens in the code.

Replace 'CHANNEL_ID' with the ID of the Discord channel where you want the bot to read messages from.

Replace 'LIST_ID' with the ID of the ClickUp list where you want to create tasks.

Customize the 'assignees' list with the ClickUp assignee details as needed.

Run the bot using:

```bash
python bot.py 
```

## Usage
Once the bot is running, it will listen to messages in the specified Discord channel. When it receives a message containing "down" or an embed with a title containing "down," it will create a task in ClickUp with the modified message content.
