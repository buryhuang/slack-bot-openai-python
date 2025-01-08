# Slack Bot Setup Guide

This guide will help you set up and configure the Slack bot for both development and production environments.

## Prerequisites

- Python 3.11 or higher
- A Slack workspace where you can install apps
- OpenAI API key
- AWS account with appropriate permissions
- AWS SAM CLI installed (`brew install aws-sam-cli` on macOS)
- AWS CLI configured with credentials

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up environment variables in `samconfig.toml` or pass them during deployment.

## Slack App Configuration

### 1. Create a Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click "Create New App"
3. Choose "From scratch"
4. Name your app and select your workspace

### 2. Bot Token Scopes

Under "OAuth & Permissions", add these Bot Token Scopes:

- `chat:write` (Send messages)
- `channels:history` (View messages in public channels)
- `groups:history` (View messages in private channels)
- `im:history` (View direct messages)
- `mpim:history` (View group direct messages)
- `app_mentions:read` (Receive mention events)
- `im:write` (Send direct messages)
- `im:read` (View DM channels)

### 3. Event Subscriptions

Under "Event Subscriptions":

1. Enable Events
2. After deployment, set the Request URL to your Lambda Function URL + `/slack/events`
3. Subscribe to these bot events:
   - `message.channels` (Messages in public channels)
   - `message.groups` (Messages in private channels)
   - `message.im` (Direct messages)
   - `message.mpim` (Multi-person DMs)
   - `app_mention` (When the bot is mentioned)

### 4. App Home

1. Go to "App Home"
2. Enable the Messages Tab
3. Check "Allow users to send Slash commands and messages from the messages tab"

### 5. Install App

1. Go to "Install App"
2. Click "Install to Workspace"
3. Authorize the requested permissions

## AWS Lambda Deployment

1. Install AWS SAM CLI:

   ```bash
   # On macOS
   brew install aws-sam-cli

   # On Linux
   pip install aws-sam-cli
   ```

2. Build the SAM application:

   ```bash
   sam build
   ```

3. Deploy to AWS:

   ```bash
   sam deploy --guided
   ```

   During the guided deployment, you'll be prompted for:

   - Stack name (e.g., slack-bot)
   - AWS Region
   - Parameter values:
     - SlackBotToken (your Slack Bot User OAuth Token)
     - SlackSigningSecret (your Slack Signing Secret)
     - OpenAIApiKey (your OpenAI API Key)
   - Confirmation of IAM role creation
   - Function URL authorization

   The command will create a `samconfig.toml` file with your preferences for future deployments.

4. For subsequent deployments, you can either:

   a. Use the same parameters:

   ```bash
   sam deploy
   ```

   b. Update parameters:

   ```bash
   sam deploy --parameter-overrides \
       SlackBotToken=xoxb-new-token \
       SlackSigningSecret=new-secret \
       OpenAIApiKey=new-key
   ```

   c. Update with custom OpenAI model and base URL:

   ```bash
   sam deploy --parameter-overrides \
       SlackBotToken=xoxb-new-token \
       SlackSigningSecret=new-secret \
       OpenAIApiKey=new-key \
       OpenAIModel=ft:gpt-3.5-turbo-0613:my-org:custom-model:id \
       OpenAIBaseURL=https://my-custom-openai-proxy.com/v1
   ```

5. After deployment, SAM will output the Function URL. Use this URL + `/slack/events` as your Slack app's Request URL.

## Security Notes

- Never commit sensitive values to version control
- Store the parameter values securely
- Regularly rotate API keys and tokens
- Monitor AWS Lambda usage and costs
- Set up CloudWatch alarms for errors

## Usage

### Direct Messages

- Find the bot under "Apps" in your Slack sidebar
- Start a DM conversation
- The bot will respond using the configured OpenAI model

### Channel Interactions

- Invite the bot to a channel using `/invite @botname`
- Mention the bot using `@botname` followed by your message
- The bot will respond in a thread

### Private Channels

- Add the bot to private channels the same way as public ones
- The bot needs to be explicitly invited to private channels

