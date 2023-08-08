import os
import openai
import secret
openai.api_key=secret.api_key
### write your code below 
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's a good book to read on a rainy day? please just name 2."}
    ],
  n=3
)

for i in (response["choices"]):
  print(i["message"]['content'].strip()) 
  print(" ////////    ")