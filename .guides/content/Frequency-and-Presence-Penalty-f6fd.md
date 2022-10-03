----
We have now covered temperature,top_p and max_tokens from our response variable. 
```python
response = openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
```

## Frequency Penalty
 **Frequency penalty** is used to decrease the likelihood  of the same line being repeated word for word. Frequency is a number between -2.0 and 2.0. Frequency penalty works by lowering the chances of a word being selected again the more times that word has already been used.





## Presence Penalty 
**Presence Penalty** can be used to measure the probability of the completion to introduce a new topic. The presence penalty does not consider how many times the word has been used, but just if the word exists in the text overall. Think of frequency_penalty as a way to not have too many same-word repetitions. Think of presence_penalty as a way to not have too much topic repetition









