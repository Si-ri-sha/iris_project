import json
import os

MEMORY_FILE = "iris_memory.json"

def load_memory():
    """Loads past interactions from a JSON file if it exists."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_memory(memory):
    """Saves user interactions into a JSON file."""
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def remember_user(user_id, message, response):
    """Stores messages and responses under a user ID."""
    memory = load_memory()
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append({"message": message, "response": response})
    save_memory(memory)

def recall_user_history(user_id):
    """Retrieves past conversations of a specific user."""
    memory = load_memory()
    return memory.get(user_id, [])

if __name__ == "__main__":
    user_id = input("Enter your name: ")
    print("\n--- Previous Conversations ---")
    history = recall_user_history(user_id)
    
    if history:
        for entry in history:
            print(f"You: {entry['message']}")
            print(f"IRIS: {entry['response']}\n")
    else:
        print("No past conversations found.\n")

    user_message = input("You: ")
    response = f"IRIS remembers! {user_message}"
    remember_user(user_id, user_message, response)

    print(f"IRIS: {response}")
