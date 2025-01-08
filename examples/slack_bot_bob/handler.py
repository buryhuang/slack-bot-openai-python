import os
import logging
from slack_bot_openai.handler import SlackBotHandler

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

DEFAULT_SYSTEM_MESSAGE = """You are helpful AI assistant."""

# Initialize the bot handler
bot_handler = SlackBotHandler(
    system_message=DEFAULT_SYSTEM_MESSAGE,
    model='gpt-4o',
    include_chat_history=True
)

# Get the Lambda handler
lambda_handler = bot_handler.get_lambda_handler()

# For local development and testing
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bot_handler.app.start(port=int(os.getenv('PORT', 6001))) 