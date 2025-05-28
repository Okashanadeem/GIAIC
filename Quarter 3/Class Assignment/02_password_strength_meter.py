import streamlit as st
import re
import random
import string
import time

def generate_strong_password():
    """Generate a strong password that meets all criteria"""
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    # Ensure at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest with random characters
    all_chars = lowercase + uppercase + digits + special_chars
    while len(password) < 12:  # Generate a 12-character password
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    """Check password strength and return score and feedback"""
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*)")
    
    # Common Password Check
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a common password. Please choose a stronger one")
    
    # Strength Rating
    if score == 4:
        strength = "Strong"
        color = "green"
        feedback = ["✅ Excellent! Your password meets all security criteria"]
    elif score == 3:
        strength = "Moderate"
        color = "orange"
        feedback.append("⚠️ Consider adding more security features")
    else:
        strength = "Weak"
        color = "red"
        feedback.append("❌ Your password needs improvement")
    
    return score, strength, color, feedback

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
    
    st.title("🔒 Password Strength Meter")
    st.write("Check your password strength and get suggestions for improvement")
    
    # Create two columns for input and strength meter
    col1, col2 = st.columns([2, 1])
    
    with col1:
        password = st.text_input("Enter your password:", type="password", key="password_input")
        
        if st.button("Generate Strong Password"):
            with st.spinner("Generating a strong password..."):
                time.sleep(0.5)  # Add a small delay for better UX
                generated_password = generate_strong_password()
                st.success("Generated Password:")
                st.code(generated_password)
                st.info("Click the copy button to copy the password")
                if st.button("Copy Password", key="copy_button"):
                    st.write("Password copied to clipboard!")
    
    if password:
        score, strength, color, feedback = check_password_strength(password)
        
        with col2:
            st.markdown("### Password Strength")
            st.markdown(f"<h2 style='color: {color}'>{strength}</h2>", unsafe_allow_html=True)
            st.progress(score/4)
            st.markdown(f"Score: {score}/4")
        
        st.markdown("### Feedback")
        for message in feedback:
            st.write(message)
        
        # Additional security tips
        st.markdown("### 💡 Security Tips")
        st.markdown("""
        - Use a unique password for each account
        - Avoid using personal information
        - Consider using a password manager
        - Change passwords regularly
        - Enable two-factor authentication when possible
        """)

if __name__ == "__main__":
    main()
