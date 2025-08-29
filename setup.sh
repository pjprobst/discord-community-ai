#!/bin/bash

# Setup script for Discord Chat Exporter Bot

echo "Setting up Discord Chat Exporter Bot..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete!"
echo ""
echo "To run the bot:"
echo "1. Make sure you have enabled 'Message Content Intent' in your Discord Developer Portal"
echo "2. Update the DISCORD_BOT_TOKEN in discord_bot.py with your bot token"
echo "3. Run: ./venv/bin/python discord_bot.py"
echo ""
echo "Note: You need to enable 'Message Content Intent' in your Discord Developer Portal:"
echo "Go to https://discord.com/developers/applications/ -> Your App -> Bot -> Message Content Intent" 