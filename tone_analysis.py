from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_tone(text):
  """
  Analyzes the sentiment of the given text.
  Returns the tone as Positive, Negative, or neutral.
  """
  sentiment_score = analyzer.polarity_scores(text)
  compound = sentiment_score['compound']

  if compound >= 0.05:
    return "Positive 😊"
  elif compound <= -0.05:
    return "Negative 😠"
  else:
    return "Neutral 😐"
  
  if __name__ == "__main__":
    print(analyze_tone("I am so happy today!"))
    print(analyze_tone("This is the worst day ever."))
    print(analyze_tone("It's an okay day."))
    print(f"Sentiment Scores: {sentiment_score}")  # Debugging
