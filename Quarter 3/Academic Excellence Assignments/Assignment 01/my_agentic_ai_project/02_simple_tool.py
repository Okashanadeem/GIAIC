from datetime import datetime

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("User: What time is it?")
print("Agent:", get_time())
