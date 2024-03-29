# -*- coding: utf-8 -*-
"""NLP_TEST_Shyamashree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A9BA6iAAsswL1iBN55QuKB1L47to6As7
"""

'''
1. What you understand by Text Processing? Write a code to perform text processing ?
Ans.
Text Processing is an essential step in natural language processing. It helps to analyze
and sorting unstructured text data to extract meaningful insights.Some applications are
language translation, sentiment analysis and spam fitering etc.
'''
import nltk
import re
import string
def text_processing(text):
  text = text.lower()
  text = re.sub(r'\d+','',text) #removing digit
  text = re.sub(r'[^\w\s]', '', text) #removing punctuation
  return text

text_processing(text="Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!")

'''
2. What you understand by NLP toolkit and spacy library? Write a code in which any one gets used.
Ans.
NLTK Kit: Natural language processing is a field focuses on making human language usable by computer programs. NLTK, or Natural
Language Toolkit is a python package that we can use for natural language processing. Some example, text processing, sentimant
analysis.
Spacy Library: Spacy is free and open source library with a lot of built-in-capabilities. It plays a crucial role for processing
amd analyzing data in the field of NLP. Nowadays unstructured data is generated by companies, governments and population at an
incredible rate. So making dicision and conclusion, we need to analyze the data. Spacy can help to do that.

'''
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
def tokenize_text(text):
  text = word_tokenize(text)
  return text
tokenize_text(text="I am very to hear it. Can you tell me the reason?")

'''
3. Describe Neural Networks and Deep Learning in Depth .
Ans.
Neural Network is a method of artificial intelligence that teaches computers to process data which is inspired by
human brain. It uses interconnected nodes or neurons.It consists of three layers: input layer, hidden layer and output layer.
input layer receives input data and then it goes through hidden layer and finally it gives output through output layer.

Deep learning is a field of machine learning which simulates human brain. It uses layer of interconnected nodes.
It is useful for complex data. That is why it takes more time to train. It also consists of three layers: input layer, hidden
layer and output layer. Input layer receives input from user and then it goes through hidden layer which process the data and then
finally it gives prodiction through output layer.
'''

'''
4.what you understand by Hyperparameter Tuning?
Ans. Hyperparameter Tuning is findind a set optimal  hyperparameter. The combination of hyperparameter minimizes the loss function
to produce better results and maximizes the model's performance. Actually it helps to improve model's performance by reducing error.

'''

'''
5. What you understand by Ensemble Learning?
Emsemble learning is a technique combining individual model to give a stronger and more accurate predictive model.
A problem in machine learning is that individual models tend to perform poorly. In other words, they tend to have
low prediction accuracy. In ensemble learning, we combine multiple models to get one with a better performance.
'''

'''
6. What do you understand by Model Evaluation and Selection ?
Ans.
 Assessing and Choosing the Best Performing Models. In the rapidly
 evolving field of machine learning, the ability to select the most suitable
 model for a given problem is crucial.

'''

'''
7. What you understand by Feature Engineering and Feature selection? What is the difference between them?
Ans.
Feature Engineering is a process of transformation of raw data into features suitable for modelingto improve
the accuracy of the algorithm and removing unnecessary features.
Feature Selection is a selection focuses on selecting the most informative subset of features from the dataset

'''

