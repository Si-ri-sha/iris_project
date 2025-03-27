from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_tone(user_input):
  """Analyze the sentiment of the user input and return a response."""
  analyzer = SentimentIntensityAnalyzer()
  sentiment_score = analyzer.polarity_scores(user_input)

  if sentiment_score['compound'] >= 0.5:
    return "You seem really happy! "
  elif sentiment_score['compound'] <= -0.5:
    return "I sense some sadness. I'm here to listen"
  else:
    return "You sound neutral or thoughtful. Tell me more!"
  
user_text = input("How are you feeling today?")
response = analyze_tone(user_text)
print(response)