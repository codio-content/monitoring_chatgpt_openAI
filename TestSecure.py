# CODIO SOLUTION BEGIN
import os
from dotenv import load_dotenv

# Load the environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_KEY")

print(api_key)

# CODIO SOLUTION END