print("Welcome to ChatBot! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")

    elif user_input == "how are you?":
        print("Bot: I'm just a bunch of code, but I'm doing great!")

    elif user_input == "what is your name?":
        print("Bot: I'm ChatBot, your Python assistant.")

    elif user_input == "what can you do?":
        print("Bot: I can answer simple questions and have a basic chat.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I didn’t understand that.")
