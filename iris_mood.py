import json
import os
from collections import Counter

MEMORY_FILE = "iris_memory.json"

def load_memory():
    """Loads past interactions from the memory file."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def analyze_mood_trends(user_id):
    """Analyzes the mood trends of a specific user."""
    memory = load_memory()
    
    if user_id not in memory:
        return "No data available to track your mood yet. Start chatting more!"

    sentiment_counts = Counter(entry['sentiment'] for entry in memory[user_id])

    total_entries = sum(sentiment_counts.values())
    
    mood_report = f"📊 **Mood Summary for {user_id}** 📊\n"
    for sentiment, count in sentiment_counts.items():
        percentage = (count / total_entries) * 100
        mood_report += f"➡ {sentiment.capitalize()}: {count} times ({percentage:.2f}%)\n"
    
    return mood_report

if __name__ == "__main__":
    user_id = input("Enter your name: ")
    print("\n" + analyze_mood_trends(user_id))
