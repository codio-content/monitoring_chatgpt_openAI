##

To generate a response to a prompt, we use `openai.Completion.create`. 
```python
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)
```

Copy the code above into the file on the left and click the button below to run the code file.

{Try it!}(python3 temp.py)

The `model` argument is mandatory and the prompt is specified using the `prompt` argument.

There are many additional optional arguments that can be specified in our API call. You can get a sense of these settings using the right-hand pane of the [OpenAI playground](https://beta.openai.com/playground). Clicking on **View code** on the upper right will translate the sliders and text boxes into code.

![images/panelGIF](images/panelGIF.gif)

Here is an example of an API call using more arguments:
```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

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
We will cover what each of these arguments does throughout this lesson.


## Temperature
Lets start by seeing how **temperature** impacts the response generated. Temperature defaults to 1 and accepts values between 0 and 1 inclusive.

Try changing the value of temperature from 1 to 0 and compare how our response changed. 
```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0)
```

{Try it!}(python3 temp.py 1)

|||challenge
## Try these variations:

* Try the code when you set `temperature=0.5`

{Try it!}(python3 temp.py 2)

* Try the code when you set `temperature=0.7`

{Try it!}(python3 temp.py 3)
|||

**Temperature** controls how much randomness is in the output. When closer to 0 or the lower the temperature, the more we get an output that we would expect or of high probability. The AI model will choose words with a higher probability of occurrence when at lower temperature. [You can read more about temperature in the OpenAI docs.](https://beta.openai.com/docs/api-reference/completions/create#completions/create-temperature) 

Lower temperature is suitable for cases when we need stability, most probable output. Lets write a function to run the `temperature=0` 5 times and  `temperature=1` 5 times. In order to make our text look way more clean we can comment out our original print statement, which we will be using later. We can use the following code to simply print the text without the extra information.
``` python
print(response["choices"][0]["text"])
```
{Try it!}(python3 temp.py 3)
This is a sample code to run the outputs 5 times. Compare the outputs when switching temperature from 0 to 1. 
```python
for i in range(5):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0, 
                                    max_tokens=6)
  #print(response)
  print(response["choices"][0]["text"])
  ```
{Try it!}(python3 temp.py 4)
We can see that when we use the `temperature=0` we get the same answer. However, when we set the `temperature=1` we more or less get different answer with each iteration. A temperature between 0.70–0.90 is the most common for creative tasks.

The [OpenAI playground](https://beta.openai.com/playground). Comes with one visual tool that helps show the probability of words. If you scroll down to the `show probabilities` in the playground, it is off by default but you can turn it on and compare. 

<img src="images/cap3.PNG" width="200">

If you scroll back up. You can play around with different temperatures and try to see how probabilities correlate with the output given a temperature. 

<img src="images/cap4.PNG" width="200">


## n

We can use the `n` parameters in order to generate multiple completions. It can use up your tokens fairly quickly be warned. By default, it is set to `n=1`. Lets remove our for loop and add an extra argument to our response and set that equal to 5. 

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=1, 
                                    max_tokens=6,
                                    n=5)
print(response)
```
{Try it!}(python3 temp.py 4)

We can further clean up our text by changing our print statement to the following:
```python
for i in (response["choices"]):
  print(i["text"]) 
```
|||
### Best of  
The `best_of` parameter generates multiple responses to a query, then after selects the best one “n” completions. Generating multiple completion can consume your token quota.
|||

Try running a code such that `n=5` and `best_of=4`.
```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=1, 
                                    max_tokens=20,
                                    n=5,
                                    best_of=4)
```
{Try it!}(python3 temp.py 5)

You will generate an error essentially saying you requested that the server return more choices that it will generate. `n` needs less than or equal to `best_of`. We don't need to use `n` in order to use `best_of`. It will generate 4 completions but only print the "best" one.
```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=1, 
                                    max_tokens=20,
                                    best_of=4)
```
{Try it!}(python3 temp.py 6)