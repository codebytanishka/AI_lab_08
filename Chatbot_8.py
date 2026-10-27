print("Chatbot: Hello!! If u want to exit type BYE!!")
while True:
    user=input("You: ").lower()
    if "bye" in user:
        print("Chatbot: Goodbye!!!")
        break
    elif "hey" in user or "hello" in user:
        print("CHatbot: Hellow! how r u!?")
    elif "fine" in user:
        print("Chatbot: Glad to hear that!")
    elif "name" in user:
        print("Chatbot: I dont have any!")
    elif "thank" in user:
        print("Chatbot: My pleasure !")
    else:
        print("Chatbot: Cant understand!")
        
