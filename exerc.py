import os
import openai
import secret
openai.api_key=secret.api_key
# CODIO SOLUTION BEGIN
import time

def Generate(prompts):
    responses = []

    for prompt in prompts:
        start_time = time.time()
        response = openai.Completion.create(
            engine="text-davinci-002",  # Select the engine
            prompt=prompt,
            max_tokens=100  # Limit the response length
        )
        end_time = time.time()
        time_taken = end_time - start_time

        # Store the generated response and the time taken
        responses.append((response.choices[0].text.strip(), time_taken))

    return responses

# CODIO SOLUTION END
