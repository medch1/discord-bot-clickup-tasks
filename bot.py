import discord
import requests

# Replace 'YOUR_BOT_TOKEN' with the token you copied from the Discord Developer Portal
BOT_TOKEN = ' '
CHANNEL_ID =   # Replace with the ID of the channel you want the bot to read messages from

CLICKUP_API_KEY = '  '  # Replace with your ClickUp API key
LIST_ID = "  "  # Replace with the ID of the list where you want to create tasks

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Assignee details
assignees = [
    {
        "id": 01010101,
        "username": "MED CH",
        "color": "#536cfe",
        "initials": "MD",
        "email": "med",
        "profilePicture": None
    },
]

def create_clickup_task(task_name):
    url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

    payload = {
        "name": task_name,
        "assignees": [assignee["id"] for assignee in assignees],
        "status": "Open"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": CLICKUP_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        data = response.json()
        task_id = data['id']
        print('Task created successfully. Task ID:', task_id)
    else:
        print('Failed to create task. Status code:', response.status_code)
        print('Response:', response.json())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    print(f"Message from {message.author.name}: {message.content}")
    # Check if the message is from the specified channel and sent by the target user
    if message.channel.id == CHANNEL_ID:
        message_content = message.content

        # Check if the message contains "is DOWN" (case-insensitive)
        if "down" in message_content.lower():
            # Modify the message content by adding "investigate why" at the beginning
            modified_message = "investigate why " + message_content

            # Create a task in ClickUp using the modified message content
            create_clickup_task(modified_message)

        for embed in message.embeds:
            embed_dict = embed.to_dict()
            print(embed.to_dict())
            # Check if the title or the description contains "down" (case_insensitive)
            if "down" in embed_dict.get('title', '').lower():
                #or "down" in embed_dict.get('description', '').lower()
                # Modify the message content by adding "investigate why" at the beginning

                modified_message = "investigate why " + embed_dict.get('title', '')
                # Create a task in ClickUp using the modified message content
                create_clickup_task(modified_message)

# Start the bot
client.run(BOT_TOKEN)
