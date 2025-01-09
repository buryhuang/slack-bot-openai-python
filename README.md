# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Slack_icon_2019.svg/2048px-Slack_icon_2019.svg.png" width="40"> 🤖 Slack Bot OpenAI in AWS Lambda

Hey there! 👋 Looking for a Slack bot that works with OpenAI but doesn't cost a fortune? You're in the right place! This is the only OpenAI-powered Slack bot that runs on both free Slack workspaces and AWS Lambda. This package provides a streamlined framework for handling Slack events with OpenAI integration, conversation history, and thread support - all without requiring a paid Slack subscription or dedicated server infrastructure.

## 🚀 Quick Start

All you need are these three keys to get started:
```bash
OPENAI_API_KEY=sk-xxx
SLACK_BOT_TOKEN=xoxb-xxx
SLACK_SIGNING_SECRET=xxx
```

## 💡 Why Choose This Bot?

Let me tell you why this bot is different from others out there:

1. **Works with Free Slack! 🎉**
   - Unlike other solutions that require Slack's paid plans, this bot works perfectly with free Slack workspaces
   - Full functionality without any paid workspace requirements
   - All core functionalities maintained on free tier

2. **True Serverless Design ⚡**
   - The only Slack-OpenAI bot specifically engineered for AWS Lambda
   - Eliminates the need for costly EC2 instances or self-hosting
   - Addresses all Lambda-specific challenges out of the box

3. **Using Latest OpenAI SDK**
   - Many existing solutions use outdated OpenAI versions
   - We maintain compatibility with the latest OpenAI Python SDK (v1.59.5) as much as we can.
   - Stays current with the latest LLM advancements

4. **Simple Yet Powerful 💪**
   - While there are comprehensive solutions like [@seratch's ChatGPT-in-Slack](https://github.com/seratch/ChatGPT-in-Slack) (created 2 years ago) or [chatgpt-on-deno](https://github.com/seratch/chatgpt-on-deno) from same author, who is Slack employee Kazuhiro Sera
   - They either lack updates or require Slack's framework that needs a paid plan
   - We focus on simplicity and essential text-based chat functionality

5. **Core Features Without Bloat 🛠️**
   - Handles the most critical issue: message deduplication
   - Maintains automated testing
   - Simple enough to fork and modify
   - Available as a Python package for quick start
   - Open source and free to use (no Slack paid version required)

6. **Future-Proof & Extensible 🔮**
   - While keeping the core simple, the project is designed to be extensible
   - Additional integrations through [MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)
   - Supports hundreds of integrations using the same OpenAI format

## 📚 Complete Working Example

Want to see it in action? Check out `examples/slack_bot_bob` in this repo! It's a production-ready example with:

✨ Full AWS SAM deployment setup
🔧 Detailed configuration guide
💬 Thread support & conversation history
🎯 Custom model configuration

Everything's included:
- Ready-to-use `template.yaml` for AWS SAM configuration
- Step-by-step deployment instructions
- Environment variable setup
- Complete Slack app configuration walkthrough

## 🔌 Flexible Model Support

Use any OpenAI-compatible API you prefer:
```bash
# Optional: Use any OpenAI-compatible API endpoint
OPENAI_BASE_URL=https://your-endpoint
# Optional: Use any model including your fine-tuned ones
OPENAI_MODEL=your-model-name
```

Works seamlessly with:
- OpenAI API
- DeepSeek
- MCP-Bridge
- Ollama
- Your own fine-tuned models
- Any OpenAI-compatible API endpoint

## 🛠️ Installation

Simple as pie:
```bash
pip install slack_bot_openai
```

## 💻 Usage

Here's all you need to get started:
```python
from slack_bot_openai.handler import SlackBotHandler

# Initialize the bot handler
bot_handler = SlackBotHandler(
    system_message="Your system message here",
    model="gpt-4o",  # or your preferred model
    include_chat_history=True
)

# Get the Lambda handler
lambda_handler = bot_handler.get_lambda_handler()
```

## ✨ Features

- 💬 Slack event handling with OpenAI integration
- 🧠 Message history management
- 🔄 DynamoDB integration for message deduplication
- 📝 Thread message support
- ⚙️ Configurable system messages and models

## 📋 Requirements

- Python 3.11+
- openai==1.53.0
- slack-bolt>=1.18.0
- boto3==1.34.49

## 🔑 Environment Variables

Required:
- `SLACK_BOT_TOKEN`: Slack Bot User OAuth Token
- `SLACK_SIGNING_SECRET`: Slack Signing Secret
- `OPENAI_API_KEY`: OpenAI API Key

Optional:
- `OPENAI_BASE_URL`: Custom OpenAI API base URL
- `OPENAI_MODEL`: OpenAI model name (defaults to gpt-4o)
- `INCLUDE_CHAT_HISTORY`: Whether to include chat history (defaults to true)
- `DYNAMODB_TABLE`: DynamoDB table name for message deduplication

## 🤝 Contributing

Love this bot? Want to make it better? We'd love your help! Feel free to:
- Open issues
- Submit PRs
- Suggest improvements
- Share your use cases

## 📝 License

MIT License - Go wild! Use it, modify it, share it.