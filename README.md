# 👮‍♂️ GrammarPoliceBot

> **Telegram bot that corrects my English in real conversations to help me prepare for the IELTS exam.**

This bot monitors your English in Telegram chats, using **Qwen 30B Thinking** (via OpenRouter) to detect mistakes and suggest improvements. It also maintains a **"Wall of Shame"** to track who needs the most practice.

---

## 🚀 Features

* **Real-time Correction:** Uses AI to identify and correct grammar/spelling errors instantly.
* **The "Wall of Shame":** A competitive leaderboard tracking user error counts.
* **Focused Feedback:** Ignores minor capitalization/punctuation issues to focus on actual IELTS-relevant errors.
* **Minimalist Style:** No fluff—just the correction and a concise explanation.
* **Slang Aware:** Intelligent enough to "PASS" on laughter, emojis, and common internet slang.

## 🛠️ Technology Stack

* **Language:** Python 3.10+
* **Framework:** `python-telegram-bot`
* **AI Engine:** OpenRouter API (`qwen/qwen3-vl-30b-a3b-thinking` or similar)
* **Environment:** `python-dotenv`

## 📋 Prerequisites

1.  **Python 3.10+** installed.
2.  A **Telegram Bot Token** (from [@BotFather](https://t.me/botfather)).
3.  An **OpenRouter API Key** (from [openrouter.ai](https://openrouter.ai/)).

---

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/teoang/GrammarPoliceBot.git](https://github.com/teoang/GrammarPoliceBot.git)
    cd GrammarPoliceBot
    ```

2.  **Install dependencies:**
    ```bash
    pip install python-telegram-bot openai python-dotenv
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the root directory:
    ```env
    TELEGRAM_TOKEN=your_telegram_bot_token_here
    OPENROUTER_API_KEY=your_openrouter_key_here
    ```

4.  **Run the Bot:**
    ```bash
    python main.py
    ```

---

## 🤖 Bot Commands

| Command | Description |
| :--- | :--- |
| `/start` | Initializes the bot and displays the welcome message. |
| `/stats` | Shows the **Wall of Shame** leaderboard. |
| *Auto-Monitor* | The bot automatically checks every text message sent in the chat. |

## 💡 Logic & Workflow

1.  **Analysis:** The bot sends every message to the AI.
2.  **Validation:** If the text is correct or purely slang/emojis, the AI returns "PASS".
3.  **Correction:** If an error is detected, the AI provides the corrected version + a short explanation.
4.  **Tracking:** The bot increments the user's error count and replies to the original message.

> [!WARNING]
> **Persistence Note:** User stats are currently stored in-memory. If the bot restarts, the leaderboard resets. Integrating a JSON file or SQLite database is a recommended next step.
