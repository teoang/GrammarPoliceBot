Grammar Judge Telegram Bot
Telegram bot that corrects my English in real conversations to help me prepare for the IELTS exam. It uses Qwen 30B Thinking to detect mistakes and suggest improvements while chatting. It maintains a "Wall of Shame" leaderboard to track who fails the most at basic English.

🚀 Features
Real-time Correction: Uses AI to identify and correct grammar/spelling errors instantly.

- The "Wall of Shame": Tracks the number of mistakes made by each user.
- Strict Criteria: Ignores minor issues like missing periods or capitalization to focus on actual linguistic crimes.
- Minimalist Feedback: No polite fluff—just the correction and a one-sentence explanation.
- Slang Friendly: Programmed to "PASS" on laughter, emojis, and common slang.

🛠️ Technology Stack
- Language: Python
- Library: python-telegram-bot
- AI Engine: OpenRouter API (using qwen/qwen3-vl-30b-a3b-thinking)

Environment Management: python-dotenv

📋 Prerequisites
1) Python 3.10+ installed.
2) A Telegram Bot Token (obtainable via @BotFather).
3) An OpenRouter API Key (obtainable at openrouter.ai).

⚙️ Installation & Setup
1) Clone the repository:

git clone <your-repo-url>
cd <repo-folder>

2) Install dependencies:

pip install python-telegram-bot openai python-dotenv

3) Configure Environment Variables:
Create a .env file in the root directory and add your credentials:

TELEGRAM_TOKEN=your_telegram_bot_token_here
OPENROUTER_API_KEY=your_openrouter_key_here

4) Run the Bot:

python main.py

🤖 Bot Commands
/start - Initializes the bot and provides a welcome message.
/stats - Displays the Wall of Shame leaderboard showing who has the most recorded mistakes.
Automatic Monitoring - The bot automatically checks every text message sent in the chat.

💡 How it Works (Logic)
The bot sends a specific prompt to the AI for every message received:

1) If the text is correct or contains only emojis/slang, the AI responds with "PASS" and nothing happens.
2) If an error is found, the AI returns the corrected version and a short explanation.
3) The bot then increments the user's error count in a local dictionary and replies to the offending message.

⚠️ Important note
Currently, user_stats are stored in memory. If the bot restarts, the leaderboard will reset. To make the "Wall of Shame" permanent, you might want to integrate a JSON file or a database for persistent storage.
