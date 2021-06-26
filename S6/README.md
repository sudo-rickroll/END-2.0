# Encoder-Decoder LSTM Model for Sentiment Analysis on Tweets

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S6/main.ipynb)


This directory contains the PyTorch code for Encoder-Decoder architecture and its in-depth output at every timestep.

The model used here contains the following architecture :

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/65642947/123500330-fc1b9980-d65a-11eb-94f0-1e56ad9bb27f.png"> 
</p>

Both the Encoder and the Decoder contain a Single Layer, Unidirectional LSTM RNN each.

The above structure is accomplished by the following code blocks :

### Encoder :

<p align="center" width="100%">
    <img width="60%" src="https://user-images.githubusercontent.com/65642947/123515205-fbfbb800-d6b3-11eb-9962-e4cd1ccf8cab.png"> 
</p>

The output from the embedding layer would have the shape (batch_size, sequence_length, embedding_dimensions). In the first For Loop (line #4), we are iterating over every batch, i.e. iterating over every sentence. In lines 5 and 6, we are setting input hidden vector and input cell state to be tensors of 0 of size (1, 1, embedding_dimensions) which translates to (num_layers\*no. of directions, sequence_length, embedding_dimensions). Since we are parsing every sentence word by word, the first For Loop (# 4) will be for every sentence and the second For Loop (# 8) will be for every token/word. Since we will be passing these hidden and cell state vectos as input to the LSTM to the second For Loop, we will have to modify dimensions to match the input vector dimensions for every token to be processed at any particular timestep. In line # 9, the input, hidden and cell state will be passed to the LSTM for one token at a time, forcing only one timestep from the LSTM encoder. For example, for token 1 in sentence 1, the input vector will have the shape (batch[0], sequence[0,0], embedding_dimension[0,0,0]) and the shapes of hidden and cell states are as mentioned previously, with zero tensor corresponding to the shape of the input vector. output_sequence_list is a list containing output from every token in the sequence as elements, which is then concatenated later to get the output for the sentence, in line # 11 and in the same line, the output_batch_list has elements corresponding to output from every sentence obtained after concatenating corresponding tensors of the sentences in the batch. The final output is a tensor obtained by concatenating the elements in this output_batch_list to otain the tensors of every sentence in the batch, formed by the concatenation of tensors from the sentences in a batch. The lists corresponding to hidden vector and cell states follow the shapes of their corresponding output list counterparts.


