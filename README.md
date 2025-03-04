# Slack Bot Project

Welcome to the Slack Bot Project! This repository contains a powerful Slack bot that offers various functionalities to enhance your Slack workspace experience.

## Key Features

1. **Reply to User Messages**
   - The bot automatically replies whenever a user sends a message in the Slack channel.

2. **New User Verification**
   - When a new user joins the channel, the bot receives a direct message (DM) containing the word "start" (case insensitive) to signify a new user.
   - The bot verifies the new user by reacting to the received DM. Once verified, the user can actively participate in channel discussions.

3. **Message Count**
   - Tracks and displays the total number of messages sent in the channel since the bot started running locally.


## Platforms and Tools Used

1. **Visual Studio Code (VS Code)**
   - Used for coding and testing the bot's functionalities.

2. **ngrok**
   - Creates a secure tunnel and provides a public URL to integrate the bot with Slack API while running locally.

3. **Slack API**
   - Ensures seamless integration between the bot's code and the Slack channel.

4. **Slack Channel**
   - The bot is installed in the channel to perform the specified tasks.

---

## Setting Up the Slack API

Before running the bot, you need to configure your Slack API settings properly. Follow these steps:

1. **Create a Slack App**
   - Go to the [Slack API Dashboard](https://api.slack.com/apps) and click on **Create New App**.
   - Choose "From scratch" and provide a name for your app. Select the workspace where you want to install the bot.

2. **Configure Bot Permissions**
   - Navigate to **OAuth & Permissions** in your app settings.
   - Add the following bot token scopes:
     - `chat:write`
     - `channels:read`
     - `channels:history`
     - `reactions:write`
     - `im:write`
     - `im:history`
   - Click **Install to Workspace** and authorize the app.

3. **Enable Event Subscriptions**
   - Go to **Event Subscriptions** in your app settings.
   - Toggle the feature to "On."
   - Paste the ngrok public URL followed by `/slack/events` into the Request URL field (e.g., `https://<ngrok-url>/slack/events`).
   - Subscribe to bot events:
     - `message.channels`
     - `message.im`
     - `reaction_added`

4. **Enable Interactivity & Shortcuts**
   - In **Interactivity & Shortcuts**, toggle the feature to "On."
   - Paste the same ngrok public URL followed by `/slack/interactive` (e.g., `https://<ngrok-url>/slack/interactive`).

5. **Add Bot to Workspace**
   - Go to **App Home** and click "Add to Workspace."
   - Ensure the bot is added to the appropriate Slack channel where it will operate.

6. **Obtain and Store Tokens**
   - Copy the **Bot User OAuth Token** from **OAuth & Permissions**.
   - Add it to your environment variables or configuration file to allow the bot to authenticate with the Slack API.

---

## How to Run the Bot Locally

Follow these steps to set up and run the Slack bot:

1. **Clone the Repository**
   ```bash
   git clone [<repository-link>](https://github.com/MahraibFatima/Slack-bot)
   cd slack-bot-project
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start ngrok**
   ```bash
   ngrok http 5000
   ```
   > Replace `5000` with the port on which your bot is configured to run.

4. **Configure Slack App**
   - Copy the ngrok public URL.
   - Paste it into your Slack App settings under **Event Subscriptions** and **Interactivity & Shortcuts**.

5. **Run the Bot**
   ```bash
   python bot.py
   ```

6. **Install the Bot in Your Slack Workspace**
   - Add the bot to your Slack workspace and test its features.

---


## Contributing

We welcome contributions! Feel free to open issues or submit pull requests with your suggestions and improvements.

## Future Enhancements

- Implement advanced user verification methods.
- Add functionality to persist message counts across bot restarts.
- Improve error handling and logging mechanisms for better maintainability.
