from google import genai
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
uploaded_file=client.files.upload(file="window.jpeg")  #.mp3, jpg, mp4, .pdf
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=["Describe this image for me", uploaded_file]
)
print(response.text)
# while True:
#     message = input("> ")
#     if message == "exit":
#         break
#     res=chat.send_message(message)
#     print(res.text)