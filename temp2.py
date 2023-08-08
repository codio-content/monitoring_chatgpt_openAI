import os
import openai
import secret
openai.api_key=secret.api_key
import time
### write your code below 
# Start the timer
start_time = time.time()

# Make the API call to generate the completion
response=openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's a good book to read on a rainy day? please just name 2."}
    ],
  n=3
)

# Calculate the elapsed time
elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
for i in (response["choices"]):
  print(i["message"]['content'].strip()) 
  print(" ////////    ")