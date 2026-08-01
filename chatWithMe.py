from google import genai
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat=client.chats.create(model="gemini-3.5-flash")
while True:
    message = input("> ")
    if message == "exit":
        break
    res=chat.send_message(message)
    print(res.text)