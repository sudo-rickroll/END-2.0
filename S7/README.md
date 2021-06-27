# Sentiment Analysis and Neural Machine Translation

## Part A - Sentiment Analysis on Stanford Tree Bank 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20A/SST_Analysis_using_LSTM_(without_PyTreeBank).ipynb)

Stanford Tree Bank is a dataset used for sentiment analysis. It contains sentiment values for phrases and sentences containing those phrases. Every sentence has a sentiment value and the phrases making that sentence are further broken down into smaller parts and they have been assigned some sentiment values as well.
The Sentiment Values for the phrases range from 0 to 1. The ranges for different sentiments are as follows:
<ul>
  <li> 0 ≤ Value < 0.2 -> Very Negative</li>
  <li> 0.2 ≤ Value < 0.4 -> Negative</li>
  <li> 0.4 ≤ Value < 0.6 -> Neutral</li>
  <li> 0.6 ≤ Value < 0.8 -> Positive</li>
  <li> 0.8 ≤ Value ≤ 1 -> Very Positive</li>
</ul>

It contains 3 main text files:
<ul>
  <li><i>datasetSentences.txt</i> -> Contains the whole sentences and their id's (id's here are to be neglected as they do not represent the true id of the sentence with respect to the other phrases).</li>
  <li><i>dictionary.txt</i> -> Contains sentences, phrases and their id's (id's here are the ones that need to be considered).</li>
  <li><i>sentiment_labels.txt</i> -> Contains the sentiment values with respect to id's in <i>dictionary.txt</i>.</li>
</ul>
</br>

### Dataset preparation

For Dataset preparation, we first load all the sentences from <i>datasetSentences.txt</i> into a dataframe. Then, we get the id's of these sentences from <i>dictionary.txt</i>. If any sentence in <i>datasetSentences.txt</i> does not have an ID for it in the <i>dictionary.txt</i>, this item will be dropped. The two columns will be named as "Sentences" and "Labels", in the dataframe.
Then, using torchtext legacy utilities, we create Field for processing of "Sentences" and LabelField for processing of "Labels". We use the "Spacy" tokenizer in both the Fields.
Then, we create a dataset and we further split it into training and validation datasets in a 70-30 proportion.
Using these datasets, we create a BucketIterator to so that batches can be prepared out of the dataset for loading into the model at a later stage during training.

### Model

The model consists of an embedding layer, followed by packing of this output sequence from embedding layer. Then, we feed it to a 2-layer, unidirectional LSTM.
Then, the data is passed to a Fully Connected layer and for the output of it, a log softmax is applied. This will generate probabilistic outputs.

## Part B - Neural Machine Translation on "CMU Question-Answer" Dataset and "Quora Duplicate Question Pair" Dataset using LSTM Encoder-Decoder


### CMU Question-Answer Translation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/CMU_QA_Dataset_.ipynb)

This dataset includes manually-generated factoid question/answer pairs with difficulty ratings from Wikipedia articles. Dataset includes articles, questions, and answers. For our training, we only consider the "Question" and "Answer" columns from 3 different iterations of the dataset - S08, S09 and S10 (indicating datasets from Spring of 2008, 09 and 10). In the dataset, one question can frequently appear multiple times in case those questions were answered by multiple individuals. 

### Dataset Preparation

The tab-seperated data from all 3 iterations (S08, 09 and 10) are loaded into a dataframe, skipping 3 rows with data that seem erroneus to be parsed. Unicodes of special characters are encoded using the python engine in the pandas library. Only the "Questions" and "Answers" columns are loaded into the dataframe in the process. Rows with "na" values are discarded.

Using the torchtext legacy utilities, two "SRC" and "TRG" <i>Field</i> objects are created for preprocessing, one for the "Questions" column and the other for the "Answers" column. Then, we define a function for spacy_en tokenizer for tokenization of the sentences in english using spacy. Then we create a torchtext legacy dataset and split the dataset in 70-30 proportions into train and test datasets.

### Model

This is an encoder-decoder architecture. We use a two-layered, unidirectional LSTM in both encoder and decoder, with a dropout of 0.5 in-between the layers. Encoder contains an embedding layer and LSTM layer. Decoder contains an LSTM layer and a Fully Connected layer. 

We use PPL as a metric in place of accuracy to measure the performance of the model as it is a machine translation model. We do not use teacher forcing while evalating the test dataset.

### Quora Question Duplication

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/Quora_Q%26Q_Pair_Dataset.ipynb)
