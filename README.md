# Getting started

## Installation

- Create and activate the virtual environment.

- Install the required packages.

- Rename the sample.env to .env

- Set your `OPENAI_API_KEY` in the .env file.

- Go to [https://discord.com/developers/applications/](https://discord.com/developers/applications/) and click on `New Application`.

- Enter the name for your bot, accept the terms and click on `Create`. On the resulting page, enter the details of your bot as you like.

- On the left sidebar, click on `Bot`. Under the heading `Privileged Gateway Intents`, toggle all 3 options to ON position. Save your changes.

- Now click on `Reset Token` and copy the token value. Set it as `DISCORD_BOT_TOKEN` in .env file.

- On the left sidebar, click on `OAuth2` and go to `URL Generator`. Under `Scopes` select `bot`.

- Under `Bot Permissions` allow the following

```text
Read Messages/View Channel
Send Messages
Read Message History
Mention everyone
```

- Now scroll down and copy the `Generated URL`. Paste it in a browser window and select the Server where you want to add the bot.

- Click on `Continue` and authorize the bot.

- The bot has been successfully added to your server.

## Usage

- Activate your virtual environment, and run the discord bot server using the command

```bash
python discord_bot.py
```

- You can add data sources to the bot as follows:

```text
/embedchain add <data_type> <url_or_text>
```

- You can ask your queries from the bot as follows:

```text
/embedchain query <question>
```

## Supported Data Types

Please use the following keywords for the data_type argument to add data sources to the bot:
- Youtube Video - youtube_video
- PDF file - pdf_file
- Web Page - web_page
- Site Map - sitemap
- Doc file - docx
- Code documentation website - docs_site
- Text Data - text
