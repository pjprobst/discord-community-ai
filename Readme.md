# Discord Q&A and Resume Review System

An intelligent system that leverages Discord community knowledge to provide personalized Q&A responses and resume feedback using machine learning and semantic search.

## 🎯 Vision

Transform Discord communities into intelligent knowledge bases by:
- **Smart Q&A**: Automatically answer new questions using historical Discord conversations
- **Intelligent Resume Reviews**: Provide personalized, human-like resume feedback based on community expertise

Unlike generic resume review sites, this system learns from real human feedback patterns to deliver contextual, community-driven advice.

## 🏗️ Architecture

### Core Components

1. **Data Extraction** (`DiscordChatExporter`)
   - Exports Discord channel conversations to structured JSON
   - Currently focused on `questions-forum` channels from CSC @ Pitt server

2. **Data Processing** (`process_exports.py`)
   - Parses exported JSON files
   - Extracts question-answer pairs and resume feedback threads
   - Generates clean datasets for ML training

3. **Semantic Search Engine** (`discord_bot.py`)
   - Uses SentenceTransformers for question similarity matching
   - Implements cosine similarity scoring with configurable thresholds
   - Currently using `all-MiniLM-L6-v2` model for fast inference

4. **Discord Bot Interface**
   - `!ask <question>` - Query the knowledge base
   - `!review_resume` - Resume analysis (in development)

### Data Flow
```
Discord Channels → JSON Export → Processing → Knowledge Base → Semantic Search → Bot Responses
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Discord Bot Token
- Access to Discord channels for data extraction

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd DiscordChatExporter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Setup
1. **Export Discord Data**
   - Use DiscordChatExporter CLI to export channel conversations
   - Place JSON files in `exported_data/` directory

2. **Process Data**
   ```bash
   python process_exports.py
   ```

3. **Configure Bot**
   - Update `DISCORD_BOT_TOKEN` in `discord_bot.py`
   - Adjust `SIMILARITY_THRESHOLD` (default: 0.65)

4. **Run Bot**
   ```bash
   python discord_bot.py
   ```

## 📊 Current Status

### ✅ Implemented
- Discord data export and parsing
- Question-answer pair extraction
- Semantic similarity search
- Basic Discord bot commands
- SentenceTransformer integration

### 🚧 In Development
- Resume review functionality
- PDF/image resume parsing
- Advanced feedback generation
- Multi-modal input processing

### 🎯 Planned Features
- Fine-tuned LLM integration for response generation
- Resume template matching and scoring
- Community feedback learning
- Web interface
- Analytics dashboard

## 📁 Project Structure

```
DiscordChatExporter/
├── discord_bot.py              # Main bot with Q&A functionality
├── process_exports.py          # Data processing pipeline
├── requirements.txt            # Python dependencies
├── exported_data/             # Raw Discord JSON exports
│   └── *.json                 # Individual channel exports
├── q_and_a.json              # Processed Q&A knowledge base
├── resume_advice.json        # Processed resume feedback data
└── venv/                     # Python virtual environment
```

## 🔧 Configuration

### Key Parameters
- `SIMILARITY_THRESHOLD`: Minimum cosine similarity for question matching (0.65)
- `QA_DATA_FILE`: Path to processed Q&A knowledge base
- `MODEL`: SentenceTransformer model for embeddings

### Supported Channels
- `questions-forum`: Academic and technical Q&A
- `resume-reviews`: Resume feedback and career advice (planned)

## 🤖 Usage Examples

### Query the Knowledge Base
```
!ask What's the best CS 1550 project for my resume?
```
**Response:** *Matches against historical discussions and provides community-backed recommendations*

### Resume Review (Planned)
```
!review_resume [attachment: resume.pdf]
```
**Expected Response:** *Detailed feedback on format, content, and improvements based on community patterns*

## 🔮 Technical Details

### Machine Learning Pipeline
1. **Text Preprocessing**: Clean and normalize Discord message content
2. **Embedding Generation**: Convert questions to vector representations
3. **Similarity Search**: Find closest matching historical questions
4. **Response Aggregation**: Combine relevant answers with confidence scoring

### Performance Considerations
- Model: `all-MiniLM-L6-v2` (384 dimensions, ~80MB)
- Inference time: ~50ms per query
- Memory usage: Scales with knowledge base size

## 🤝 Contributing

This project is in early development. Key areas for contribution:
- Resume parsing and analysis algorithms
- UI/UX improvements
- Data quality enhancement
- Performance optimization

## 📝 Notes

- Bot token is currently hardcoded (move to environment variables)
- Limited to CSC @ Pitt Discord server data
- Resume functionality is placeholder implementation
- Consider privacy implications when handling user data

## 🎯 Next Steps

1. **Resume Analysis Engine**
   - PDF text extraction
   - Common mistake detection
   - Personalized feedback generation

2. **Advanced NLP**
   - Fine-tune models on domain-specific data
   - Implement retrieval-augmented generation (RAG)
   - Add conversation memory

3. **User Experience**
   - Web dashboard
   - Batch processing capabilities
   - Analytics and insights

---

*Built with DiscordChatExporter for data extraction and powered by SentenceTransformers for semantic search.*
