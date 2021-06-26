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

For Dataset preparation, we first load all the sentences from <i>datasetSentences.txt</i> into a dataframe. Then, we get the id's of these sentences from <i>dictionary.txt</i>. If any sentence in <i>datasetSentences.txt</i> does not have an ID for it in the <i>dictionary.txt</i>, this item will be dropped.

## Part B - Neural Machine Translation on "CMU Question-Answer" Dataset and "Quora Duplicate Question Pair" Dataset using LSTM Encoder-Decoder


### CMU Question-Answer Translation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/CMU_QA_Dataset_.ipynb)


### Quora Question Duplication

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/Quora_Q%26Q_Pair_Dataset.ipynb)
