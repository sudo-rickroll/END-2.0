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

The following code block illustrates the code of the main logic for processing the inputs at every timestep, by the LSTM - 

<p align="center" width="100%">
    <img width="60%" src="https://user-images.githubusercontent.com/65642947/123515205-fbfbb800-d6b3-11eb-9962-e4cd1ccf8cab.png"> 
</p>

In the Encoder, the input is passed through an Embedding Layer initially. The output from the embedding layer would have the shape (batch_size, sequence_length, embedding_dimensions). 
<ul>
    <li>In the first For Loop (line #4), we are iterating over every batch, i.e. iterating over every sentence. </li>
    <li>In lines 5 and 6, we are setting input hidden vector and input cell state to be tensors of 0 of size (1, 1, embedding_dimensions) which translates to (num_layers\*no. of directions, sequence_length, embedding_dimensions). </li>
    <li>Since we are parsing every sentence word by word, the first For Loop (# 4) will be for every sentence and the second For Loop (# 8) will be for every token/word. Since we will be passing these hidden and cell state vectos as input to the LSTM to the second For Loop, we will have to modify dimensions to match the input vector dimensions for every token to be processed at any particular timestep. </li>
    <li>In line # 9, the input, hidden and cell state will be passed to the LSTM for one token at a time, forcing only one timestep from the LSTM encoder. For example, for token 1 in sentence 1, the input vector will have the shape (batch[0], sequence[0,0], embedding_dimension[0,0,0]) and the shapes of hidden and cell states are as mentioned previously, with zero tensor corresponding to the shape of the input vector.</li>
    <li><i>output_sequence_list</i> is a list containing output from every token in the sequence as elements, which is then concatenated later to get the output for the sentence in line # 11 and in the same line, the <i>output_batch_list</i> has elements corresponding to output from every sentence obtained after concatenating corresponding tensors of the sentences in the batch.</li>
    <li>The final output is a tensor obtained by concatenating the elements in this output_batch_list to otain the tensors of every sentence in the batch, formed by the concatenation of tensors from the sentences in a batch. The lists corresponding to hidden vector and cell states follow the shapes of their corresponding output list counterparts.</li>
</ul>

### Decoder :

The following code block illustrates the code of the main logic for processing the hidden layer outputs from Encoder passed as context vector at the first timestep, by the LSTM at every timestep -

<p align="center" width="100%">
    <img width="60%" src="https://user-images.githubusercontent.com/65642947/123520084-9ec03080-d6cc-11eb-8908-3c7e2420d070.png"> 
</p>

The hidden vector output from the Encoder is passed onto the decoder as the context vector and the cell state is also passed for use by this decoder. 
This hidden vector will have the shape (num_layers \* lstm_directions, batch_size, hidden_dimensions). 
Number of LSTM layers used in this case is 1. 
The LSTM is forcibly run for only 1 timestep at a time. 
<ul>
    <li>In line # 4, the first for loop takes into account the number of layers.</li>
    <li>In line # 5, the For loop is run for every encoded sentence in the encoder output vector. Inside this loop, in line # 7 and # 8, the hidden and cell vectors for this sentence is extracted.</li>
    <li>In the next For Loop in line # 9, which is run for every encoded token from Encoder ouput, these hidden and cell vectors are used. The Input for every step is set to 0 as the output is calculated based on the hidden and cell states from the encoder.</li>
    <li>After calculation of output vector, hidden vector and cell state at every time step, the resultant vectors are stored in their corresponding lists, similar to the steps followed to store the data during the Encoder process while concatenating them at the end of their corresponding For Loops to obtain the resultant vectors.</li>
</ul>

After the end of all the looping sequences, the obtained final hidden vector is passed onto a Fully Connected Layer and these are converted to probabilistic values, which will be the output from the model.




