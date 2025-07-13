# 🧠 Health & Wellness Agents

An intelligent wellness planner built using Streamlit and the OpenAI Agents SDK (via [OpenRouter](https://openrouter.ai)). This project provides personalized advice on fitness, nutrition, recovery, and wellness goals using structured agents and modular tools.

> 🔬 Built by [Okasha Nadeem](https://github.com/okashanadeem)

---

## 🚀 Features

- 🤖 AI-powered conversational wellness assistant
- 🏋️ Fitness plans, 🥗 diet tips, 🤕 injury support, and 🧠 mental wellness
- 🌐 Powered by OpenRouter (`deepseek-chat`, `gpt-4o`, etc.)
- 🔌 Modular tools and agents for clean separation of responsibilities
- ⚡ Real-time streamed replies using `openai_agents` with `AsyncOpenAI`
- 🎨 Responsive, modern UI via Streamlit (`streamlit_app.py`)

---

## 🛠️ Tech Stack

| Layer         | Technology                                      |
|---------------|--------------------------------------------------|
| Frontend      | [Streamlit](https://streamlit.io)               |
| Agents SDK    | [openai_agents](https://github.com/openai/openai-python) |
| LLM Provider  | [OpenRouter](https://openrouter.ai)             |
| Models Used   | `deepseek/deepseek-chat-v3-0324:free` (via API) |
| Project Config| `pyproject.toml`, `uv`, `AsyncOpenAI`           |

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/health-wellness-agents.git
cd health_wellness_agent

# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate  # Or use `.venv\Scripts\activate` on Windows

# Install dependencies via pyproject.toml
uv pip install -e .
````

Or:

```bash
pip install -e .
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root with your OpenRouter API key:

```env
OPENAI_ROUTER_KEY=your-openrouter-api-key
```

In code, the client is initialized like this:

```python
OpenAIChatCompletionsModel(
    model="deepseek/deepseek-chat-v3-0324:free",
    openai_client=AsyncOpenAI(
        api_key=os.getenv("OPENAI_ROUTER_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
)
```

---

## ▶️ Run the App

```bash
uv run streamlit_app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
health_wellness_agent/
├── main.py                        # Base orchestration logic
├── streamlit_app.py              # Streamlit frontend app
├── agent.py                      # Main assistant logic
├── context.py                    # User session context
├── guardrails.py                 # Safety and validation logic
├── hooks.py                      # Optional lifecycle hooks
├── guardrails_ext.py             # Custom guardrail extensions
│
├── tools/                        # Agent tools (functional units)
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── scheduler.py
│   ├── tracker.py
│   └── fetch_user_name.py
│
├── agents_folder/                # Specialized agents
│   ├── escalation_agent.py
│   ├── nutrition_expert_agent.py
│   └── injury_support_agent.py
│
└── README.md                     # This file
```

---

## 💬 Try Asking

* “Suggest a 3-day home workout for weight loss.”
* “I have a knee injury — what rehab should I do?”
* “Plan a 1800-calorie vegetarian meal for the day.”
* “Track my weekly progress and recommend improvements.”

---

## 💡 Planned Enhancements

* 🗣️ Voice interface (speech-to-text + TTS)
* 🧠 Memory with context persistence
* 📈 Weekly dashboard to track health stats
* 🌓 Light/dark theme toggle

---

## 📜 License

MIT License © 2025 [Okasha Nadeem](https://github.com/okashanadeem)

---

## 🌍 Powered By

[![OpenRouter](https://openrouter.ai/static/logo.svg)](https://openrouter.ai)
Running cutting-edge models (like DeepSeek, GPT-4o, Claude) through [OpenRouter](https://openrouter.ai)
````