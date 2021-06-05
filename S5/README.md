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

The <b>pytreebank</b> library (https://github.com/JonathanRaiman/pytreebank) contains the sentences, phrases and their corresponding labels in a tree structure, with the sentence and its label present at the top of the tree.

For the purpose of sentiment analysis as part of this directory, only the root sentences have been used and the individual phrases making up the sentences have been discarded. Hence, only the root node from every tree of the pytreebank has been considered. 


## Data Pre-Processing

### Dataset Preparation

After the sentences are fetched from the root node of the trees from the pytreebank, they are read onto a dataframe using the `to_labeled_lines()` method of the pytreebank. This produces a dictionary with three keys, namely - `train`, `test` and `dev`. As the name suggests, `train` is the train set, `test` is the test set and `dev` is the validation set.

The dataframe produces by these three dictionaries are then combined to obtain the complete dataset. This complete dataset is then again split to Train Dataset and Validation Dataset, with the desired proportion of data in each of them (70-30, in this case). Augmentations are done on the Train Dataset and later, with this augmented Train Set and the original (untouched) Validation Set are then used to build the Dataset objects from the <i>torchtext.legacy.data</i> module. 

### Dataset Augmentation

As mentioned in the <i>Dataset Preparation</i> section, augmentations are performed on the Train Dataset. Here, a certain portion of the Train Dataset is chosen and augmentations are performed on them and the resulting augmented sentences are added to the dataset (original sentences are not replaced by the augmented sentences) to provide invariance and to also add data to the dataset.

For the analysis present in this directory, three types of augmentations are performed :
<ol>
  <li>Random Augmentations (EDA)</li>
  <ul>
    <li>Random Swap</li>
    <li>Random Delete</li>
  </ul>
  <li>Back Translation</li>
</ol>

For EDA [[1]](#1), 5% of the Train Dataset has been picked, based upon the following figure in the EDA Research Paper [[1]](#1) (page 3):

![image](https://user-images.githubusercontent.com/65642947/120890203-bbfa6580-c61e-11eb-8ca7-b537df93b68f.png)


Random Swap and Random Delete have been performed using <i>nlpaug</i> (https://github.com/makcedward/nlpaug), each with a fraction of 1/3 samples from the 5% of the Train Dataset that was picked earlier. 1 augmented sentence was generated for every sentence and 1% of the words in each sentence were picked for augmentation, following the information from the EDA Research Paper[[1]](#1) (page 4):

![image](https://user-images.githubusercontent.com/65642947/120890249-fc59e380-c61e-11eb-94d4-230f543e2d7a.png)


For the remaining samples of that 5% that was picked from the Train Set earlier, Back Translation was applied using <i>googletrans v3.1.0a0</i> (https://github.com/ssut/py-googletrans). 

## Model Preparation

The model used here is based off of an RNN Network. It uses an Embedding Layer, a 2 Layer, Unidirectional LSTM Cell and a Fully Connected Layer. When the Input is passed onto the model, its Embeddings are produced and it is then packed to address the varying input text lengths. It is then passed onto the 2 Layer LSTM Cell. The final Hidden Layer Output is passed onto the Fully Connected Layer and this is the output from the model.

![SST LSTM](https://user-images.githubusercontent.com/65642947/120892961-53b38000-c62e-11eb-8807-a8e4f60a9199.jpg)

## Parameters

Following are the parameter values used for this NLP Task:

<ul>
  <li><b>Dataset Split :</b> Train - 70, Val - 30 </li>
  <li><b>Batch Size :</b> 16 </li>
  <li><b>Embedding Size :</b> 300 </li>
  <li><b>FC Layer Hidden Nodes :</b> 100 </li>
  <li><b>Batch Size :</b> 16 </li>
  <li><b>Dropout :</b> 0.2 </li>
  <li><b>Optimizer :</b> Adam </li>
  <li><b>Learning Rate :</b> 0.00001 </li>
  <li><b>Loss Function :</b> Cross Entropy Loss </li>
</ul>

> ## References
  >><a id="1">[1]</a> 
    Jason Wei and Kai Zou (2019). 
    <a href="https://arxiv.org/abs/1901.11196v2">EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks </a> (pp. 2 - 4).
    arXiv:1901.11196v2 [cs.CL].
