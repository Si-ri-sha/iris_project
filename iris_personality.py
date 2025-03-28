import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_sentiment_data():
    try:
        with open("sentiment_log.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_sentiment_data(data):
    with open("sentiment_log.json", "w") as file:
        json.dump(data, file, indent=4)


def analyze_and_store_sentiment(user_id, user_message):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_message)

    if score["compound"] >= 0.5:
        sentiment_label = "positive"
        response = "That's wonderful to hear! Keep shining! 😊"
    elif score["compound"] <= -0.5:
        sentiment_label = "negative"
        response = "I'm here for you. Remember, tough times don't last, but tough people do. 💙"
    else:
        sentiment_label = "neutral"
        response = "I see! If you ever need to talk, I'm here. ☕"

    sentiment_data = load_sentiment_data()

    if not isinstance(sentiment_data, dict):
        sentiment_data = {}

    if user_id not in sentiment_data:
        sentiment_data[user_id] = []

    sentiment_data[user_id].append({
        "message": user_message,
        "response": response,
        "sentiment": sentiment_label
    })

    save_sentiment_data(sentiment_data)

    return sentiment_label, response


if __name__ == "__main__":
    user_id = input("Enter your name: ")
    user_input = input("How are you feeling today? ")

    sentiment, response = analyze_and_store_sentiment(user_id, user_input)

    print(f"Sentiment Analysis: {sentiment}")
    print(f"IRIS: {response}")
