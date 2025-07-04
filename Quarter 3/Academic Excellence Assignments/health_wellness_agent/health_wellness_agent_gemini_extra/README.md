Perfect! Here’s your **`README.md`** and `requirements.txt` for your Gemini-powered Health & Wellness Planner hosted on Streamlit:

---

## ✅ `README.md`

```markdown
# 🧠 Health & Wellness Planner Agent (Gemini + Streamlit)

This is an AI-powered Health & Wellness Assistant that helps users:
- Set fitness goals
- Get personalized meal and workout plans
- Track their progress
- Handle injuries or complex dietary needs via agent handoffs
- All in a simple Streamlit UI using **Gemini 1.5 Flash API**

🚀 Live Demo: [Click to Open App](https://health-wellness-agent-gemini-by-okasha.streamlit.app)

---

## 📦 Features

✅ Goal Analyzer  
✅ Meal Planner  
✅ Workout Recommender  
✅ Weekly Check-in Scheduler  
✅ Progress Tracker  
✅ Agent Handoffs (Nutrition Expert, Injury Support, Escalation)  
✅ Streamlit UI with Chat-like Flow  
✅ Context Memory (Session-based)  
✅ Guardrails (Basic Input Validation)  
✅ Modular Folder Structure  

---

## 🗂️ Folder Structure

```

health\_wellness\_agent\_gemini/
├── app.py                       # Streamlit UI
├── context.py                   # Context Class (State)
├── tools/                       # Tool Modules
│   ├── goal\_analyzer.py
│   ├── meal\_planner.py
│   ├── workout\_recommender.py
│   ├── scheduler.py
│   └── tracker.py
├── agents/                      # Specialized Agent Simulations
│   ├── escalation\_agent.py
│   ├── injury\_support\_agent.py
│   └── nutrition\_expert\_agent.py
├── utils/                       # Logger Tool
│   └── logger.py
├── .env                         # API Key (Not uploaded)
├── .gitignore
└── README.md

````

---

## 🛠️ How to Run Locally

### 1. Clone this repository

```bash
git clone https://github.com/your-username/health_wellness_agent_gemini.git
cd health_wellness_agent_gemini
````

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API key

Create a `.env` file with:

```env
GEMINI_API_KEY=your_google_generative_ai_api_key
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

| Variable         | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| `GEMINI_API_KEY` | Your Google Gemini API Key (free via [Google AI Studio](https://makersuite.google.com/app)) |

---

## 📋 Evaluation Criteria (Covered)

✅ Agent & Tool Integration
✅ State / Context Management
✅ Input/Output Guardrails
✅ Real-Time Interaction
✅ Agent Handoffs
✅ Folder Structure & Logging
✅ Streamlit UI (Optional ✅)

---

## 🙋‍♂️ Author

Made with ❤️ by [Okasha Khan](https://github.com/Okashanadeem)

---

## 🧪 Bonus Ideas

* Export progress to PDF
* Add calendar-based scheduling
* Integrate Firebase/DB for login-based sessions

---

## 📄 License

MIT License – use freely, credit appreciated!

````

---

## ✅ `requirements.txt`

```txt
streamlit
python-dotenv
pydantic
google-generativeai
````