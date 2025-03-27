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


def analyze_and_store_sentiment(user_message):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(user_message)

    sentiment_data = load_sentiment_data()
    sentiment_data.append({"message": user_message, "score": score})  

    save_sentiment_data(sentiment_data)

    if score["compound"] >= 0.5:
        response = "That's wonderful to hear! Keep shining! 😊"
    elif score["compound"] <= -0.5:
        response = "I'm here for you. Remember, tough times don't last, but tough people do. 💙"
    else:
        response = "I see! If you ever need to talk, I'm here. ☕"

    return response, score


if __name__ == "__main__":
    user_input = input("How are you feeling today? ")
    response, sentiment = analyze_and_store_sentiment(user_input)
    print(f"Sentiment Analysis: {sentiment}")
    print(f"IRIS: {response}")
