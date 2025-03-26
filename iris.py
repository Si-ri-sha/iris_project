import nltk

class IRIS:
  def __init__(self) :
    self.greetings = ["hello", "hi", "hey", "greetings"]
  
  def respond(self, user_input):
     user_input = user_input.lower()
     if user_input in self.greetings:
       return "Hello! How can I assist you today?"
     return "I'm still learning, bujt I'm here to help!"
  
iris = IRIS()
while True:
  user_text = input("You: ")
  if user_text.lower() == "exit":
    print("IRIS: Goodbye!")
    break
  print("IRIS:", iris.respond(user_text))
   