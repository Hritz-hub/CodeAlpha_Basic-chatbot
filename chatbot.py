print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("ChatBot: Hello there! How can I help you?")
    elif user_input == "how are you":
        print("ChatBot: I'm fine,thanks.")
    elif user_input == "bye":
        print("ChatBot: Goodbye! Have a great day!")
