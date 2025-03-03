import streamlit as st
import random
import datetime

# Set up the Streamlit app
st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

# Store progress using session state
if "goals_set" not in st.session_state:
    st.session_state.goals_set = 0
if "goals_completed" not in st.session_state:
    st.session_state.goals_completed = 0

# --- TITLE & INTRO ---
st.title("🌱 Growth Mindset Challenge")
st.write("### Unlock Your Full Potential – One Step at a Time 🚀")

st.write(
    "Hey there! Have you ever felt stuck or doubted your abilities? Don't worry, we've all been there. "
    "But guess what? Your intelligence and skills aren’t fixed! With **effort, practice, and the right mindset**, "
    "you can grow beyond your limits. That’s the power of a **growth mindset**. 🌟"
)

# --- DAILY CHALLENGE GENERATOR ---
st.subheader("🎯 Today's Growth Challenge")

challenges = [
    "Try something you've never done before, even if it scares you.",
    "Find a problem you're struggling with and tackle it from a new angle.",
    "Spend 5 minutes learning something new in a field outside your comfort zone.",
    "Turn one negative thought into a positive affirmation.",
    "Ask someone for constructive feedback on something you’ve worked on.",
    "Write down one thing you're proud of achieving this week.",
    "Help someone else grow today by sharing a tip or piece of advice."
]

daily_challenge = random.choice(challenges)
st.success(f"**{daily_challenge}** 💡")

# --- RANDOM INSPIRATIONAL QUOTES ---
st.subheader("💡 Your Daily Dose of Inspiration")

quotes = [
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“It does not matter how slowly you go as long as you do not stop.” – Confucius",
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“A person who never made a mistake never tried anything new.” – Albert Einstein",
    "“Your attitude, not your aptitude, will determine your altitude.” – Zig Ziglar",
    "“Every strike brings me closer to the next home run.” – Babe Ruth",
    "“Doubt kills more dreams than failure ever will.” – Suzy Kassem"
]

daily_quote = random.choice(quotes)
st.info(f"**{daily_quote}**")

# --- INTERACTIVE QUIZ ---
st.subheader("📝 Quick Check: How Do You Handle Challenges?")
st.write("Let’s see where you stand! No judgment, just an honest self-check. 😉")

question = "Imagine you’re stuck on a really tough problem. What’s your first instinct?"
options = [
    "😞 I feel frustrated and want to give up.",
    "💪 I take a deep breath, look for another way, and keep trying.",
    "😬 I try to avoid challenges like this whenever possible."
]
response = st.radio(question, options)

if response:
    if response == options[1]:
        st.success("That’s the spirit! A growth mindset in action. 🚀 Keep pushing forward!")
    else:
        st.warning("It’s okay, challenges can be tough! Try to see them as **stepping stones** rather than roadblocks. 🌱")

# --- GOAL SETTING SECTION ---
st.subheader("🎯 What's Your Growth Goal for This Week?")
st.write("Think of something—big or small—that you want to improve. Maybe it’s learning a new skill, overcoming a fear, or just staying consistent.")
goal = st.text_input("Write down one thing you want to get better at:")

if st.button("Lock It In!"):
    if goal:
        st.session_state.goals_set += 1
        st.success(f"**Awesome! You’ve set your goal:** {goal} 🎯\n\n Now go crush it! 💪")
    else:
        st.error("Oops! Enter a goal first.")

# --- PROGRESS TRACKER ---
st.subheader("📊 Your Progress Tracker")
st.write(f"✅ **Goals Set:** {st.session_state.goals_set}")
st.write(f"🏆 **Goals Completed:** {st.session_state.goals_completed}")

if st.button("Mark a Goal as Completed"):
    if st.session_state.goals_set > st.session_state.goals_completed:
        st.session_state.goals_completed += 1
        st.success("Woohoo! One step closer to success! 🚀")
    else:
        st.warning("You haven't set any new goals yet!")

# --- AFFIRMATIONS SECTION ---
st.subheader("🌟 Growth Mindset Affirmations")
st.write("Repeat these affirmations to reinforce your mindset:")

affirmations = [
    "💡 I am constantly learning and growing.",
    "💪 Challenges make me stronger and wiser.",
    "✨ I embrace mistakes as opportunities to improve.",
    "🚀 I believe in my ability to succeed.",
    "🔥 Hard work and persistence lead to mastery.",
    "🌱 Every effort I make is a step toward success."
]

for affirmation in affirmations:
    st.write(f"✅ {affirmation}")

# --- REFLECTION SECTION ---
st.subheader("🔍 What’s One Thing You’ve Learned Recently?")
st.write("Maybe it’s a new skill, a lesson from failure, or something about yourself. Reflecting helps us grow even more!")

reflection = st.text_area("Share your recent learning moment:")
if st.button("Submit Reflection"):
    if reflection:
        st.success("That’s amazing! Keep learning, keep growing. 🌱")
    else:
        st.error("Take a moment to reflect and write something before submitting!")

# --- CLOSING MESSAGE ---
st.write("---")
st.write("🚀 **Remember: Every small step forward counts. Believe in yourself, keep growing, and never stop learning!**")
