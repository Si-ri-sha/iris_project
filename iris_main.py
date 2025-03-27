import json
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from iris_memory import remember_user, recall_user_history

MEMORY_FILE = "iris_memory.json"

def load_sentiment_data():
    """Loads past sentiment logs."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def analyze_sentiment(user_message):
    """Uses VaderSentiment to analyze the message."""
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_message)
    
    if score['compound'] >= 0.5:
        return "positive", score
    elif score['compound'] <= -0.5:
        return "negative", score
    else:
        return "neutral", score

def generate_response(sentiment_label):
    """Generates an appropriate response based on sentiment."""
    responses = {
        "positive": "That's wonderful to hear! 😊",
        "negative": "I'm here for you. If you need to talk, I'm listening. ☕",
        "neutral": "I see! Tell me more. 🌸"
    }
    return responses.get(sentiment_label, "Interesting!")

if __name__ == "__main__":
    user_id = input("Enter your name: ")

    print("\n--- Your Previous Conversations ---")
    history = recall_user_history(user_id)

    if history:
        for entry in history[-3:]:
            print(f"You: {entry['message']}")
            print(f"IRIS: {entry['response']}\n")
    else:
        print("No past conversations found.\n")

    user_message = input("You: ")
    sentiment_label, score = analyze_sentiment(user_message)
    response = generate_response(sentiment_label)

    remember_user(user_id, user_message, response)

    print(f"\nIRIS: {response}")
    print(f"Sentiment Scores: {score}")