from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import AsyncOpenAI  
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

MODEL_ID = "qwen/qwen3-vl-30b-a3b-thinking"

user_stats = {}

# BOT COMMANDS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm ready to judge your grammar!. Use /stats to see the leaderboard! 🧐"
    )

async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not user_stats:
        await update.message.reply_text("No mistakes recorded yet! Everyone is perfect... for now. 😎")
        return

    sorted_stats = sorted(user_stats.values(), key=lambda x: x['errors'], reverse=True)
    
    message = "🏆 **Wall of Shame (Grammar Mistakes)** 🏆\n\n"
    for idx, user in enumerate(sorted_stats, 1):
        message += f"{idx}. {user['name']}: {user['errors']} mistakes\n"

    await update.message.reply_text(message, parse_mode='Markdown')

async def check_grammar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text
    user = update.message.from_user
    
    prompt = f"""
    ROLE: Strict English Grammar Specialist.
    RULES:
    1. Analyze the following text: "{user_text}"
    2. If the text is correct, slang, laughter (e.g., "hahaha"), or just emojis, respond ONLY with the word "PASS".
    3. If there is a grammar or spelling error:
    - Provide the corrected version first.
    - Provide a 1-sentence explanation of the fix.
    4. IGNORE capitalization and missing punctuation at the end of the sentence.
    5. DO NOT be polite. No "Here is the correction:".
    """
    
    try:
        response = await client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        
        ai_reply = response.choices[0].message.content.strip()
        print(f"🧠 AI ({MODEL_ID}) risponde: {ai_reply}")
        
        if "PASS" not in ai_reply:
            user_id = user.id
            if user_id not in user_stats:
                user_stats[user_id] = {"name": user.first_name, "errors": 0}
            
            user_stats[user_id]["errors"] += 1
            
            await update.message.reply_text(
                ai_reply, 
                reply_to_message_id=update.message.message_id
            )
           
    except Exception as e:
        print(f"Error checking message: {e}")

# START THE BOT

if __name__ == '__main__':
    print(f"Bot is running with ({MODEL_ID})! Press Ctrl+C to stop.")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", show_stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_grammar))
    
    app.run_polling()