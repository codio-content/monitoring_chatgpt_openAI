##
Now that we have covered temperatures, another argument we have to cover is `max_tokens`. Switch which print statement is commented out. 

```python
print(response)
#print(response["choices"][0]["text"])
```

It will make seeing the token variable easier. Now, lets start with what are tokens. 

## Definition: Token
The GPT family of models process text using ***tokens***. Tokens are numerical representation of words or characters.
- The process of tokenization involves dividing plain text, such as a phrase, sentence, paragraph, or entire documents into smaller chunks of data so that it is easier to analyze.
- These smaller chunks of data are referred to as *tokens*, which may include words, phrases, or sentences.

|||
Here are some helpful rules of thumb for understanding tokens in terms of lengths:
<b>1 token ~= 4 chars in English</b>
<b>1 token ~= ¾ words</b>
<b>100 tokens ~= 75 words</b>
Or 
<b>1-2 sentence ~= 30 tokens</b>
<b>1 paragraph ~= 100 tokens</b>
<b>1,500 words ~= 2048 tokens</b>
|||
One can tokenize in two ways:

* Tokenizing by word - The benefit to using tokenization by word is that we can pinpoint words that are frequently used. If we were analyzing a group of restaurant ads in NY, and found that the word "vegan" was used often, then we might assume that there are plenty of vegan options at these restaurants.

* Tokenizing by sentence - When tokenizing by sentence, we have the ability to analyze how the words in the sentence correlate with each other, which allows us to better understand the context of the words. If we were analyzing a group of restaurant ads in NY, and found that the sentence "No vegan options." was used, then we can determine that there are not plenty of vegan options at these restaurants.

OpenAI provides a tokenizer tool to experiment on. 
(https://beta.openai.com/tokenizer)

Lastly, OpenAI imposes a 2048 token limit in order to maintain latency. If we do some math 3/4 of 2048 is over 1500 words.  OpenAI works in a "pay as you go " model. Tokens are one of the units used to determine pricing for an API call.

## Word and Token


The API treats words according to their context in the text data. Remember The same word can have 2 different tokens count depending on the structure of the text.

Lets go back to our [playground](https://beta.openai.com/tokenizer) and try the following: 

"red is my favorite color."
![images/cap1](images/cap1.PNG)

Now if we change the lowercase `r` in red to capital `R`. check the token id to see if anything changed. 

![images/cap2](images/cap2.PNG).

Try playing with different iterations. You will find out That

* The token generated for word varies depending on its placement within the sentence or if capitalize or not. 
* Tokens can include trailing space characters

The more we know about tokens it can help with better prompt design. For example, prompts ending with a space character may result in lower-quality output. This is because the API already incorporates trailing spaces in its dictionary of tokens.

More on tokens and how to count them can be found on the OpenAI [website](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)