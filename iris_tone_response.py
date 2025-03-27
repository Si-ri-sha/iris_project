from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_tone(user_input):
  """Analyze the tone of user input and generate a response."""
  sentiment = analyzer.polarity_scores(user_input)
  compound_score = sentiment['compound']

  if compound_score >= 0.5:
        return "You sound really happy! 😊 That's great to hear!"
  elif compound_score <= -0.5:
        return "I'm sensing you're feeling down. 💙 Want to talk about it?"
  else:
        return "Got it! Sounds pretty neutral. 🤔 What’s on your mind?"

# Take user input and respond
user_text = input("You: ")
response = analyze_tone(user_text)
print("IRIS:", response)
