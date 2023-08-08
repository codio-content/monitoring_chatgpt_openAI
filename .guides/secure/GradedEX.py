import os
import subprocess
import sys

sys.path.insert(1, '/home/codio/workspace')
import time
import exerc

def test_generate():
    prompts = ["How does photosynthesis work?", "Recite the Pythagorean theorem.", 
               "Write a poem about summer.", "Who is Elon Musk?", "What is the theory of relativity?"]
    
    start_time = time.time()
    responses = exerc.Generate(prompts)
    end_time = time.time()
    total_time_taken = end_time - start_time
    
    assert isinstance(responses, list), "The function should return a list."
    assert len(responses) == len(prompts), "The length of the responses list should be equal to the length of the prompts."
    
    for i, (response, time_taken) in enumerate(responses):
        assert isinstance(response, str), f"The response to prompt {i+1} should be a string."
        assert isinstance(time_taken, float), f"The time taken for prompt {i+1} should be a float."
        print(f"Prompt: {prompts[i]}\nResponse: {response}\nTime Taken: {time_taken} seconds\n")
    
    print(f"Total time taken: {total_time_taken} seconds")

    # If all assertions pass, print a success message
    print("All tests passed!")

test_generate()
