# Install necessary packages
# pip install chatterbot==1.0.4
# pip install chatterbot_corpus

# Import the ChatterBot modules
import nltk
nltk.download('punkt_tab')

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
bot = ChatBot(
    "BookChatBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

# Create a trainer for the chatbot
trainer = ListTrainer(bot)

# Example training data with Bhagavad Gita verses and translations
qa_data = [
    {"question": "What is the main theme of Chapter 1?", "answer": "The main theme of Chapter 1 is the introduction of the battlefield, setting the stage for the dialogue between Krishna and Arjuna."},
    {"question": "Who is the protagonist?", "answer": "The protagonist is Arjuna, the warrior prince."},
    {"question": "What does Krishna teach Arjuna?", "answer": "Krishna teaches Arjuna about duty, righteousness, and devotion, emphasizing the importance of performing one's duty without attachment to the results."},
    # Continue adding more question-answer pairs for comprehensive coverage
]

# Train the chatbot with the QA data
for entry in qa_data:
    trainer.train([entry['question'], entry['answer']])

# Test the chatbot
response = bot.get_response("What is the main theme of Chapter 1?")
print(response)


