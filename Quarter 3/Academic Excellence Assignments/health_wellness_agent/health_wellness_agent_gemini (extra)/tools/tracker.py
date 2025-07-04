# tools/tracker.py

def track_progress(message, context):
    context.progress_logs.append({"update": message})
    return "📊 Progress updated!"
