# Sentiment Analysis on Stanford Sentiment Bank

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S5/main.ipynb)

This directory contains the "main.ipynb" notebook prepared for training the Stanford Sentiment Bank for Sentiment Analysis, using the LSTM Model and Data Augmentations such as "Random Augmentations" from EDA and "Back Translation".

## Stanford Sentiment Bank Overview

The Stanford Sentiment Bank contains 11855 sentences. Each sentence is assigned an ID and this ID is mapped to labels ranging from values 1-5, with the following sentiments:
<ul>
  <li>1 - Very Negative</li>
  <li>2 - Negative</li>
  <li>3 - Neutral</li>
  <li>4 - Positive</li>
  <li>5 - Very Positive</li>
</ul>

These 11855 sentences are initially broken down to phrases and these phrases are mapped to IDs. These have labels attached to them, that determine their sentiment. These sentiment labels on individual phrases determine the final sentiment label of the sentence when all these phrases are combined to form sentences.

The <b>pytreebank</b> library (https://pypi.org/project/pytreebank/) contains the sentences, phrases and their corresponding labels in a tree structure, with the sentence and its label present at the top of the tree.

For the purpose of sentiment analysis as part of this directory, only the root sentences have been used and the individual phrases making up the sentences have been discarded. Hence, only the root node from every tree of the pytreebank has been considered. 
