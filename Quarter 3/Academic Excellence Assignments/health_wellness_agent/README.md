# 🏃‍♀️ Health & Wellness Planner Agent

## Overview

The **Health & Wellness Planner Agent** is a fully functional AI-powered digital wellness assistant built using the OpenAI Agents SDK. This intelligent system helps users achieve their health and fitness goals through personalized meal planning, workout recommendations, progress tracking, and expert guidance.

### Key Features

- **🎯 Goal Analysis**: Converts natural language goals into structured, actionable plans
- **🥗 Meal Planning**: Generates personalized 7-day meal plans based on dietary preferences
- **💪 Workout Recommendations**: Creates custom fitness routines tailored to user experience and goals
- **📅 Smart Scheduling**: Sets up recurring progress check reminders
- **📊 Progress Tracking**: Monitors user journey and updates plans accordingly
- **🔄 Expert Handoffs**: Seamlessly transfers to specialized agents for complex needs
- **⚡ Real-time Streaming**: Provides engaging, chatbot-like interactions with live responses
- **🛡️ Guardrails**: Ensures valid inputs and structured, trustworthy outputs

## Project Architecture

### Core Components

- **Main Agent** (`planner_agent`): Primary health and wellness planning assistant
- **Tools**: Specialized functions for goal analysis, meal planning, workout recommendations, scheduling, and progress tracking
- **Specialized Agents**: Expert agents for nutrition, injury support, and escalation to human coaches
- **Context Management**: Maintains user session state across conversations
- **Guardrails**: Input/output validation for reliable interactions
- **Streaming Interface**: Real-time response delivery

### Specialized Agents

1. **Nutrition Expert Agent**: Handles complex dietary needs (diabetes, allergies, medical conditions)
2. **Injury Support Agent**: Provides adapted workouts for physical limitations
3. **Escalation Agent**: Connects users with human coaches when needed

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for API calls

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
cd health_wellness_agent
```

### Step 2: Install Dependencies

Install all required packages using the provided requirements file:

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `openai-agents`: Core SDK for agent functionality
- `streamlit`: Web interface framework
- `pandas`: Data manipulation and analysis
- `pydantic`: Data validation and settings management
- `python-dotenv`: Environment variable management

### Step 3: Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

## How to Run

### Option 1: Streamlit Web Interface (Recommended)

Launch the interactive web application:

```bash
streamlit run streamlit_app.py
```

This will:
- Start a local web server (usually at `http://localhost:8501`)
- Open your default browser automatically
- Provide a full-featured GUI with chat interface, user profiles, and progress tracking

### Option 2: Command Line Interface

Run the agent directly from the command line:

```bash
python main.py
```

This provides a text-based interaction with the agent.

### Option 3: Python Integration

Use the agent programmatically in your own Python scripts:

```python
from main import Runner
from context import UserSessionContext
from agent import planner_agent

# Create user context
user_context = UserSessionContext(name="John", uid=1)

# Stream agent responses
async for step in Runner.stream(
    starting_agent=planner_agent,
    input="I want to lose 5kg in 2 months",
    context=user_context
):
    print(step.pretty_output)
```

## Project Structure

```
health_wellness_agent/
├── main.py                     # Main entry point and Runner setup
├── agent.py                    # Primary planner agent definition
├── context.py                  # User session context management
├── guardrails.py              # Input/output validation
├── streamlit_app.py           # Web interface (Streamlit app)
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
├── tools/                     # Agent tools directory
│   ├── __init__.py
│   ├── goal_analyzer.py       # Goal parsing and analysis
│   ├── meal_planner.py        # Meal plan generation
│   ├── workout_recommender.py # Workout plan creation
│   ├── scheduler.py           # Progress check scheduling
│   └── tracker.py             # Progress tracking and updates
├── agents/                    # Specialized agents
│   ├── __init__.py
│   ├── escalation_agent.py    # Human coach escalation
│   ├── nutrition_expert_agent.py  # Nutrition specialist
│   └── injury_support_agent.py    # Injury-adapted workouts
└── utils/                     # Utility functions
    ├── __init__.py
    └── streaming.py           # Streaming response utilities
```

## Usage Guide

### Getting Started

1. **Launch the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Set Your Profile**
   - Enter your name in the sidebar
   - The system will remember your information across sessions

3. **Start a Conversation**
   - Type your health and wellness goals in natural language
   - Example: "I want to lose 5kg in 2 months"

### Example User Journey

```
User: "I want to lose 5kg in 2 months"
→ GoalAnalyzer extracts structured goal (quantity: 5, metric: kg, duration: 2 months)

User: "I'm vegetarian and don't eat dairy"
→ MealPlanner generates 7-day vegetarian, dairy-free meal plan

User: "I have knee problems"
→ System hands off to InjurySupportAgent for specialized guidance

User: "I'm also diabetic"
→ System hands off to NutritionExpertAgent for medical dietary guidance

User: "I want to speak with a human trainer"
→ EscalationAgent handles connection to human coach
```

### Quick Start Examples

Use these example inputs to quickly test the system:

- **Weight Loss**: "I want to lose 5kg in 2 months"
- **Muscle Building**: "I want to gain muscle mass and get stronger"
- **Dietary Planning**: "I'm vegetarian and need a meal plan"
- **Workout Planning**: "I need a beginner workout routine"
- **Progress Update**: "I lost 2kg this week"
- **Injury Support**: "I have back pain and need modified exercises"
- **Nutrition Help**: "I'm diabetic and need help with meal planning"

## Features in Detail

### 🎯 Goal Analysis
- Parses natural language goals into structured format
- Validates goal completeness (quantity, metric, duration)
- Provides feedback on goal feasibility

### 🥗 Meal Planning
- Generates 7-day personalized meal plans
- Honors dietary restrictions and preferences
- Adapts to medical conditions through expert handoffs

### 💪 Workout Recommendations
- Creates custom fitness routines
- Adapts to experience level and equipment availability
- Modifies plans for injuries or limitations

### 📅 Smart Scheduling
- Sets up recurring progress check reminders
- Tracks milestone dates and deadlines
- Sends motivational check-ins

### 📊 Progress Tracking
- Records user updates and measurements
- Modifies plans based on progress
- Maintains historical progress logs

### 🔄 Agent Handoffs
- **Nutrition Expert**: Complex dietary needs, medical conditions
- **Injury Support**: Physical limitations, adaptive workouts
- **Escalation**: Human coach connections

### 🛡️ Guardrails
- **Input Validation**: Ensures goals follow proper format
- **Output Validation**: Guarantees structured, reliable responses
- **Safety Checks**: Prevents harmful or incomplete advice

## Technical Details

### State Management
- **UserSessionContext**: Maintains user profile, goals, plans, and progress
- **Persistent Storage**: Remembers information across conversations
- **Context Sharing**: All tools and agents access shared state

### Streaming Implementation
- **Real-time Responses**: Uses `Runner.stream()` for live interactions
- **Step-by-Step Processing**: Shows tool calls and agent handoffs
- **Async Support**: Non-blocking operations for better performance

### Error Handling
- Graceful fallbacks for API failures
- Clear error messages for users
- Logging for debugging and monitoring

## Troubleshooting

### Common Issues

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **OpenAI API key issues**
   - Check your `.env` file exists and contains valid API key
   - Verify API key has sufficient credits

3. **Streamlit won't start**
   - Ensure port 8501 is available
   - Try: `streamlit run streamlit_app.py --server.port 8502`

4. **Agent not responding**
   - Check internet connection
   - Verify OpenAI API status
   - Review console logs for specific errors

### Performance Tips

- Use specific, clear goals for better results
- Provide dietary preferences upfront for better meal planning
- Update progress regularly for adaptive planning
- Use handoffs for specialized needs

## Development Notes

### Adding New Tools
1. Create tool file in `tools/` directory
2. Implement tool class with proper guardrails
3. Add to agent's tool list in `agent.py`

### Adding New Agents
1. Create agent file in `agents/` directory
2. Implement agent with proper handoff logic
3. Add to handoffs list in main agent

### Customizing Guardrails
- Modify `guardrails.py` for input/output validation
- Add custom validators for specific use cases
- Implement safety checks for sensitive operations

## License

This project is for educational and demonstration purposes. Please ensure compliance with OpenAI's usage policies and terms of service.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the OpenAI Agents SDK documentation
3. Open an issue in the project repository

---

**Built with ❤️ using OpenAI Agents SDK and Streamlit**

*Note: This is a demo application. Always consult healthcare professionals for medical advice.*