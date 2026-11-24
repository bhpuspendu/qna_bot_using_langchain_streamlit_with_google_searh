# 🔎 Q&A Chatbot with LangChain Search Agent

A conversational Q&A chatbot built with **LangChain** and **Streamlit**. It uses a tool-calling agent that can search Google in real time, so answers are not limited to the LLM's training data.

## ✨ Features

- 💬 Chat-style interface built with Streamlit
- 🤖 LangChain agent that decides when to use a tool and when to answer directly
- 🌐 Live Google search tool for current and factual information
- 🧠 Conversation history maintained during the session
- ⚡ Simple setup and easy to extend with more tools

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | LangChain |
| UI | Streamlit |
| LLM | Groq |
| Search Tool | Google Search (via Serper) |
| Language | Python 3.10+ |

## 🧩 How It Works

1. The user types a question in the Streamlit chat UI.
2. The LangChain agent reads the question and decides whether it needs a tool.
3. If it needs fresh information, it calls the Google Search tool.
4. The search results are passed back to the LLM.
5. The LLM writes the final answer, which is shown in the chat.

```
User → Streamlit UI → LangChain Agent → (Google Search Tool) → LLM → Answer
```

## 📁 Project Structure

```
├── app.py              # Streamlit app
├── requirements.txt    # Dependencies
├── .env                # API keys (not committed)
├── .env.example        # Sample environment file
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bhpuspendu/project_qna_chatbot_with_google_search_and_streamlit.git
cd project_qna_chatbot_with_google_search_and_streamlit
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_llm_api_key
SERPER_API_KEY=your_google_search_api_key
```

### 5. Run the app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 💡 Example Questions

- "What are the latest developments in AI this week?"
- "Who won the most recent Formula 1 race?"
- "Explain LangChain agents in simple terms."

## 🔮 Future Improvements

- Add more tools (Wikipedia, calculator, arXiv)
- Add long-term memory
- Show sources and links for each answer
- Support streaming responses
- Deploy on Streamlit Community Cloud

## 🤝 Contributing

Contributions are welcome. Fork the repo, create a branch, and open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Puspendu Bhaduri**
[GitHub](https://github.com/bhpuspendu) · [LinkedIn](https://www.linkedin.com/in/puspendu-bhaduri-b333a6183)