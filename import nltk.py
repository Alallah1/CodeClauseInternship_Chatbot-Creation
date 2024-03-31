import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import random

nltk.download("punkt")
nltk.download("stopwords")

# Responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": [
        "I'm doing well, thank you!",
        "I'm great, thanks for asking!",
        "All good here!",
    ],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ],
    "what's your name?": [
        "I'm just a humble chatbot!",
        "You can call me Chatbot.",
        "I don't really have a name, I'm just here to chat!",
    ],
    "default": [
        "I'm not sure I understand.",
        "Could you please rephrase that?",
        "Let's talk about something else.",
    ],
}


# Function to preprocess input text
def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    tokens = [
        token
        for token in tokens
        if token not in stop_words and token not in string.punctuation
    ]

    return tokens


# Function to find the most similar response based on input
def get_response(user_input):
    tokens = preprocess(user_input)

    # Find the most similar response based on token overlap
    max_overlap = 0
    best_response = random.choice(responses["default"])
    for key in responses:
        if key != "default":
            key_tokens = preprocess(key)
            overlap = len(set(tokens).intersection(set(key_tokens)))
            if overlap > max_overlap:
                max_overlap = overlap
                best_response = random.choice(responses[key])

    return best_response


# Function to handle the conversation
def chat():
    print("Welcome! (type 'bye' to exit)")
    conversation_history = []
    while True:
        user_input = input("You: ").lower()
        conversation_history.append(user_input)

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

    # Optionally, you can print the conversation history
    # print("Conversation History:", conversation_history)


# Main function to run the chatbot
if __name__ == "__main__":
    chat()
