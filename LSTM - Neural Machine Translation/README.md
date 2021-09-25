# Neural Machine Translation on "CMU Question-Answer" Dataset and "Quora Duplicate Question Pair" Dataset using LSTM Encoder-Decoder

<ul>
  <li><h3> CMU Question-Answer Translation </h3>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/CMU_QA_Dataset_.ipynb)

This dataset includes manually-generated factoid question/answer pairs with difficulty ratings from Wikipedia articles. Dataset includes articles, questions, and answers. For our training, we only consider the "Question" and "Answer" columns from 3 different iterations of the dataset - S08, S09 and S10 (indicating datasets from Spring of 2008, 09 and 10). In the dataset, one question can frequently appear multiple times in case those questions were answered by multiple individuals. 

#### Dataset Preparation

The tab-seperated data from all 3 iterations (S08, 09 and 10) are loaded into a dataframe, skipping 3 rows with data that seem erroneus to be parsed. Unicodes of special characters are encoded using the python engine in the pandas library. Only the "Questions" and "Answers" columns are loaded into the dataframe in the process. Rows with "na" values are discarded.

Using the torchtext legacy utilities, two "SRC" and "TRG" <i>Field</i> objects are created for preprocessing, one for the "Questions" column and the other for the "Answers" column. Then, we define a function for spacy_en tokenizer for tokenization of the sentences in english using spacy. Then we create a torchtext legacy dataset and split the dataset in 70-30 proportions into train and test datasets.

#### Model

This is an encoder-decoder architecture. We use a two-layered, unidirectional LSTM in both encoder and decoder, with a dropout of 0.5 in-between the layers. Encoder contains an embedding layer and LSTM layer. Decoder contains an LSTM layer and a Fully Connected layer. 

We use PPL as a metric in place of accuracy to measure the performance of the model as it is a translation model that translates sentences for answers to the questions and not a class-prediction model. We do not use teacher forcing while evalating the test dataset.
  </li>
  
  <li><h3> Quora Question Duplication</h3>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S7/Part%20B/Quora_Q%26Q_Pair_Dataset.ipynb)

This dataset consists of over 400,000 lines of potential question duplicate pairs. Each line contains IDs for each question in the pair, the full text for each question, and a binary value that indicates whether the line truly contains a duplicate pair. For our training purposes, we only consider question pairs that are marked as duplicate in the dataset (where value of "is_duplicate" column is 1). Prediction is made using a translation model and a translated question is produced for every question provided.

#### Dataset preparation

The tab-seperated data from the dataset is loaded into a dataframe. Unicodes of special characters are encoded using the python engine in the pandas library. Only the "question1" and "question2" columns are loaded into the dataframe in the process. Rows with "na" values are discarded.

Using the torchtext legacy utilities, two "SRC" and "TRG" <i>Field</i> objects are created for preprocessing, one for the "question1" column and the other for the "question2" column. Then, we define a function for spacy_en tokenizer for tokenization of the sentences in english using spacy. Then we create a torchtext legacy dataset and split the dataset in 70-30 proportions into train and test datasets.

#### Model

This is an encoder-decoder architecture. We use a two-layered, unidirectional LSTM in both encoder and decoder, with a dropout of 0.5 in-between the layers. Encoder contains an embedding layer and LSTM layer. Decoder contains an LSTM layer and a Fully Connected layer. 

We use PPL as a metric in place of accuracy to measure the performance of the model as it is a translation model that translates sentences from question1 with similarity in meaning to another question and not a class-prediction model. We do not use teacher forcing while evalating the test dataset.</li>
</ul>
