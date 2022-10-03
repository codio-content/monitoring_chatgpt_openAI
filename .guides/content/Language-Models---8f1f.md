##

One way to analyze natural language is to use a **language model**.

## What is a Language Model?
A language model is a model which understands language -- more precisely how words occur together in natural language. A language model is used to predict what word comes next.

There are a few different types of language model, including **probabilistic language models** and **machine learning language models**. Within each type of language models, there are a number of design decisions in the creation of the model, including the mechanics of the model creation (e.g. unigram vs bigram for probabilistic, Neural Network setup for machine learning).

Another design decision for a language model aside from model type is the text it is built from or trained on. Language data can come from a wide range of sources:
* chat platforms
* text repositories
* websites
* news articles
* books

Ideally, you would create or train your language model on text from the same context it will be deployed in. For example, a model trained on social media sites would be more informal and use different words than a model trained on research articles. For more general purposes, there are general purpose language models.

