# PyTorch Attention

This directory contains the notebook to illustrate self attention in NLP on Seq2Seq models, as implemented by PyTorch. This implementation is done on the English-French translation pairs from the dataset hosted <a href="https://download.pytorch.org/tutorial/data.zip">here</a>. English sentences in the dataset are considered to be the sources and their corresponding French sentence counterparts are considered the target.
</br></br>

## Parameter values

<div style="margin-left:auto;margin-right:auto">
  <table>
    <tr>
      <th>Parameter</th>
      <th>Values</th>
    </tr>
    <tr>
      <td>Embedding Dimension</td>
      <td>256</td>
    </tr>
    <tr>
      <td>Hidden Dimension</td>
      <td>256</td>
    </tr>
    <tr>
      <td>Input Dimension</td>
      <td>Number of tokens in the English Vocabulary</td>
    </tr>
    <tr>
      <td>Output Dimension</td>
      <td>Number of tokens in the French Vocabulary</td>
    </tr>
    <tr>
      <td>LSTM Layers</td>
      <td>1</td>
    </tr>
    <tr>
      <td>LSTM Direction</td>
      <td>1</td>
    </tr>
  </table>
</div>
</br>

## Encoder

The Encoder contains an Embedding Layer and an LSTM RNN. A zero valued tensor is created with dimensions of (sequence length, batch size, embedding dimensions) to store the encoder outputs at each timestep. The source language tensors are passed to the encoder, starting from the first word/token in the sentence, till the EOS token. The output from every encoder timestep are in a way stacked, hence, the record of output from every timestep is recorded. For hidden and cell states, those only from the last timestep are recorded and later passed as hidden and cell state inputs to the first timestep of the decoder.
</br></br>

## Decoder

The target language tensors are passed to the decoder. The initial token passed is the SOS token and the next word is predicted by every token. Every word in the target sentence batches is passed to the decoder one by one (i.e. one word at a time from every sentence across the batches) until the last word of the sentence in the batch, excluding the EOS token. The EOS token is supposed to be predicted by the last word of the sentence. 

The Decoder consists of the Embedding Layer and an LSTM RNN. The word is first passed to the embedding layer and this embedded sequence is concatenated with the hidden output of the previous step from the RNN (in the case of the first time step, i.e. SOS Token, hidden input to that step will be the hidden output from the last time step of the encoder) and is passed to a Fully Connected layer, for the output to have the size of the size of the sequence length of the encoder output. This is done to obtain the attention weights, which needs to be multiplied with the encoder outputs. These weights are then multiplied with the encoder outputs. This gives us the attention applied output values from the encoder. We concatenate this with the embedding layer output from the same decoder timestep and a linear layer is used to reduce this output to the embedding dimension size so that it can be passed to the Decoder LSTM of that timestep.

The Decoder LSTM output from that timestep are then passed to a FC layer to obtain as many values as the number of tokens in the target vocabulary and then softmax is applied on top of it to obtain the predictions. The token with the highest value is considered to be the prediction.
