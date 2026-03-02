from bootstrap import initialize_chatbot

if __name__ == "__main__":
    bot = initialize_chatbot()
    response = bot.query("What courses are offered in AI?")
    print(response["answer"])