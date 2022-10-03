----

The same word can have 2 different tokens count depending on the structure of the text. On that same note, how we split up our words into tokens is language-dependent.

GPT-3 takes the prompt, converts the input into a list of tokens, processes the prompt, and converts the predicted tokens back to the words we see in the response.

### Token Limits
Keep track on the following when using the API:

* **Completions** - depending on the engine used, requests can use up to 4000 tokens shared between prompt and completion.

* **For specialized endpoints** - Answers, Search, and Classifications - the query and longest document must be below 2000 tokens together.

```python3 


prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", prompt=prompts, 
                                    temperature=0, 
                                    max_tokens=6)

print(response)
```
Now when we go back and analyze the response being printed.
{Try it!}(python3 temp.py)

We can see there is a <b>usage</b> being printed and there we can see the total tokens being used. It tells us the total number of tokens, and how they are split between prompt and completion. Now try modifying the `max_tokens` argument from 6 to 9. 

```python
response = openai.Completion.create(model="text-davinci-002", prompt=prompts, temperature=0, max_tokens=9)
```

{Try it!}(python3 temp.py 2)

We can see the completion token going from 6 to 9. Try increasing the `max_tokens` from 9 to 10 to 16 to 30.  
{Try it!}(python3 temp.py 3)

As you can see after a certain number of tokens, the completion token wont change in value. That is because we have reached the maximum number of tokens that could be assigned. Now try the following, change our prompt to the following. 

```python
prompts ="Write a tagline for an ice cream shop in Paris"
```
{Try it!}(python3 temp.py 4)

We can see the prompt token switch from 9 to 11. Now we know a little bit more of the `max_tokens` argument now. 

|||
The **max_tokens** argument is at default 16 and simply sets a boundary for the number of tokens to be generated in the completion.
|||

### Top P
---

**Top P** an alternative to sampling with temperature, also referred to as nucleus sampling. Generally, it is not recommended to alter both the temperature and the Top P.  Top P controls how many random result should be considered for completion as per the temperature. If we set so 0.1 means only the tokens comprising the top 10% probability mass are considered.

Remember how when using the temperature of 1 we had different answers show up. Let's try setting the `top_p`=0.1. Meaning only top 10% of probable answer. 
```python
for i in range(5):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=1, 
                                    max_tokens=6,
                                    top_p=0.1)
```

{Try it!}(python3 temp.py 5)
Here we can that the response generated 5 times was the same. That is because it taking the top 10% most probable response which is the same.