import google.generativeai as ai

API_Key="" # use your api key here

ai.configure(api_key=API_Key);

model = ai.GenerativeModel("gemini-pro")
chat=model.start_chat()

while True:
  message=input("You: ")
  if message.lower()=='bye':
    print('Chatbot: GoodBye!!')
    break
  response = chat.send_message(message)
  print('Chatbot: ', response.text)


