# Discord Management Bot

A powerful Discord bot for server management and utility features.

## Features

### Moderation Commands
- `!kick <member> [reason]` - Kick a member from the server
- `!ban <member> [reason]` - Ban a member from the server
- `!unban <member#discriminator>` - Unban a member from the server
- `!mute <member> [duration] [reason]` - Mute a member (duration in seconds, default 60)
- `!unmute <member>` - Unmute a member
- `!warn <member> [reason]` - Warn a member
- `!purge [amount]` - Delete messages (1-100, default 10)

### Utility Commands
- `!avatar [member]` - Get a member's avatar
- `!nickname <member> [new_nickname]` - Change a member's nickname
- `!userinfo [member]` - Get information about a user
- `!serverinfo` - Get information about the server
- `!ping` - Check bot latency
- `!help` - Show all available commands

### Welcome Commands
- `!setwelcome <channel> <message>` - Set a welcome message for new members
- `!removewelcome` - Remove the welcome message

## Installation

### Requirements
- Python 3.8 or higher
- pip

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iamnotneji/discord-management-bot.git
   cd discord-management-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**
   ```bash
   cp .env.example .env
   ```

4. **Get your Discord Bot Token:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section and click "Add Bot"
   - Copy the token and paste it in your `.env` file:
   ```
   DISCORD_TOKEN=your_token_here
   PREFIX=!
   ```

5. **Set Bot Permissions:**
   - In Discord Developer Portal, go to OAuth2 > URL Generator
   - Select these scopes: `bot`
   - Select these permissions:
     - Kick Members
     - Ban Members
     - Manage Messages
     - Manage Nicknames
     - Timeout Members
   - Copy the generated URL and invite the bot to your server

6. **Run the bot:**
   ```bash
   python main.py
   ```

## Project Structure

```
discord-management-bot/
├── main.py                 # Main bot file
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── README.md             # This file
└── cogs/
    ├── moderation.py     # Moderation commands
    ├── utility.py        # Utility commands
    └── welcome.py        # Welcome commands
```

## Usage Examples

### Kick a member
```
!kick @username This user was spamming
```

### Set a welcome message
```
!setwelcome #welcome Welcome to our server, {member}! We're glad to have you here in {server}!
```

### Mute a member for 5 minutes (300 seconds)
```
!mute @username 300 Spamming
```

### Purge messages
```
!purge 50
```

## Troubleshooting

### Bot not responding
- Make sure the bot token is correct in `.env`
- Ensure the bot has the required permissions in your server
- Check if the bot is online in Discord

### Permission errors
- Give the bot higher roles in your server
- Ensure the bot has the required permissions (Kick, Ban, Manage Messages, etc.)

### Welcome messages not working
- Make sure you've set a welcome message with `!setwelcome`
- Ensure the bot has permission to send messages in the welcome channel

## Deployment to Wispbyte

1. Push your code to GitHub
2. Connect your GitHub repository to Wispbyte
3. Set the `.env` variables in Wispbyte's environment settings
4. Deploy and your bot will run 24/7!

## Support

If you encounter any issues, please open an issue on GitHub.

## License

MIT License - feel free to use and modify!
