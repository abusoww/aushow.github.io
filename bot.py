import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

# Enable logging to see what is going on
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle /playagain command
async def play_again(update: Update, context: CallbackContext):
    logger.info("Received /playagain command")  # Log when the command is received
    try:
        # Send a "new game" message
        message = await update.message.reply_text("A new game has started! Try guessing the new number.")
        
        # Simulate magic by waiting for a few seconds (5 seconds here)
        await asyncio.sleep(5)
        
        # Delete the message after 5 seconds
        await message.delete()
    except Exception as e:
        logger.error(f"Error in play_again function: {e}")

# Main function to set up the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot API token
    token = '7634849512:AAGsUO-DBn0vbnzxEjpEPtgdpa0M_lmAwFA'  # Example: '123456789:ABCDEF1234567890ABCDEF1234567890ABCDEF'
    
    # Set up the application with the token
    application = Application.builder().token(token).build()

    # Add the /playagain command handler
    application.add_handler(CommandHandler("playagain", play_again))

    # Start polling to check for updates
    application.run_polling()

if __name__ == '__main__':
    main()
