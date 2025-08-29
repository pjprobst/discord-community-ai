import discord
from discord.ext import commands
from sentence_transformers import SentenceTransformer, util
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# Get Discord bot token from environment variable
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not DISCORD_BOT_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set. Please create a .env file with your bot token.")
# Path to your processed Q&A data
QA_DATA_FILE = "q_and_a.json"
# Semantic similarity threshold (adjust as needed)
SIMILARITY_THRESHOLD = 0.65

# --- Bot Setup ---
intents = discord.Intents.default()
# Temporarily disable message_content to avoid privileged intents error
# intents.message_content = True  # Required to read message content
# Note: You need to enable "Message Content Intent" in your Discord Developer Portal
# Go to https://discord.com/developers/applications/ -> Your App -> Bot -> Message Content Intent
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Load Knowledge Base and Model ---
qa_knowledge_base = []
model = None

async def load_knowledge_base_and_model():
    global model, qa_knowledge_base
    print("Loading SentenceTransformer model...")
    # Using a smaller, faster model for demonstration. Consider larger models for better accuracy.
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded.")

    print(f"Loading Q&A data from {QA_DATA_FILE}...")
    if os.path.exists(QA_DATA_FILE):
        with open(QA_DATA_FILE, 'r', encoding='utf-8') as f:
            qa_data = json.load(f)

        for entry in qa_data:
            question = entry['question']
            answers = entry['answers']
            if question and answers:
                qa_knowledge_base.append({
                    "question": question,
                    "answers": answers,
                    "embedding": model.encode(question, convert_to_tensor=True)
                })
        print(f"Loaded {len(qa_knowledge_base)} Q&A entries.")
    else:
        print(f"Error: {QA_DATA_FILE} not found. Please run process_exports.py first.")

# --- Bot Events ---
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await load_knowledge_base_and_model()

@bot.command(name='ask')
async def ask_question(ctx, *, question):
    """Ask a question and get an answer from the knowledge base"""
    if not model or not qa_knowledge_base:
        await ctx.send("Knowledge base or model not loaded. Please wait a moment or check bot logs.")
        return

    query_embedding = model.encode(question, convert_to_tensor=True)

    max_similarity = -1
    best_match_entry = None

    for entry in qa_knowledge_base:
        similarity = util.cos_sim(query_embedding, entry["embedding"])
        if similarity > max_similarity:
            max_similarity = similarity
            best_match_entry = entry

    if best_match_entry and max_similarity >= SIMILARITY_THRESHOLD:
        response = f"**Question:** {best_match_entry['question']}\n\n" \
                   f"**Answer(s):**\n" \
                   + "\n".join([f"- {ans}" for ans in best_match_entry['answers']])
        await ctx.send(response)
    else:
        await ctx.send("I'm sorry, I don't have a confident answer for that question. Please try rephrasing or ask a different question.")

@bot.command(name='review_resume')
async def review_resume(ctx):
    """Review resume functionality (in development)"""
    await ctx.send("Resume review functionality is under development. Please provide your resume text after the command, or attach a file.")

@bot.command(name='qa_help')
async def qa_help_command(ctx):
    """Show available commands"""
    help_text = """
**Available Commands:**
- `!ask <question>` - Ask a question and get an answer from the knowledge base
- `!review_resume` - Review resume functionality (in development)
- `!qa_help` - Show this help message

**Example:**
`!ask What is the best way to learn Python?`
    """
    await ctx.send(help_text)

# --- Run Bot ---
bot.run(DISCORD_BOT_TOKEN)