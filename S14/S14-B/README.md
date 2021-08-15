# Sentence Classification (Grammatically Correct or not) using BERT

Here, BERT is used to classify sentences based upon whether they are gramatically correct or not, through the classification token appended at the start of the sentence. Here, sentences contain the classification and seperator tokens as against the conventional start of string and end of string tokens. This model is trained on the CoLA Dataset.

The sample predictions and training logs have been pasted below:

## Sample Predictions

```
Sentence : They preferred them arrested.
Prediction : gramatically correct
```
```
Sentence : John is tall on several occasions.
Prediction : gramatically correct
```
```
Sentence : Bill's story about Sue may be amazing, but Max's is virtually incredible.
Prediction : gramatically correct
```
```
Sentence : Vera sent a baby alligator to Max and a leather dinosaur to Phyllis.
Prediction : gramatically correct
```
```
Sentence : Lou put the umbrella was broken.
Prediction : gramatically incorrect
```

## Training Logs

```
======== Epoch 1 / 4 ========
Training...
  Batch    40  of    241.    Elapsed: 0:00:14.
  Batch    80  of    241.    Elapsed: 0:00:27.
  Batch   120  of    241.    Elapsed: 0:00:41.
  Batch   160  of    241.    Elapsed: 0:00:55.
  Batch   200  of    241.    Elapsed: 0:01:09.
  Batch   240  of    241.    Elapsed: 0:01:24.

  Average training loss: 0.48
  Training epcoh took: 0:01:24

Running Validation...
  Accuracy: 0.81
  Validation Loss: 0.43
  Validation took: 0:00:04

======== Epoch 2 / 4 ========
Training...
  Batch    40  of    241.    Elapsed: 0:00:15.
  Batch    80  of    241.    Elapsed: 0:00:31.
  Batch   120  of    241.    Elapsed: 0:00:46.
  Batch   160  of    241.    Elapsed: 0:01:01.
  Batch   200  of    241.    Elapsed: 0:01:16.
  Batch   240  of    241.    Elapsed: 0:01:31.

  Average training loss: 0.31
  Training epcoh took: 0:01:31

Running Validation...
  Accuracy: 0.82
  Validation Loss: 0.44
  Validation took: 0:00:04

======== Epoch 3 / 4 ========
Training...
  Batch    40  of    241.    Elapsed: 0:00:15.
  Batch    80  of    241.    Elapsed: 0:00:30.
  Batch   120  of    241.    Elapsed: 0:00:45.
  Batch   160  of    241.    Elapsed: 0:01:00.
  Batch   200  of    241.    Elapsed: 0:01:16.
  Batch   240  of    241.    Elapsed: 0:01:31.

  Average training loss: 0.20
  Training epcoh took: 0:01:31

Running Validation...
  Accuracy: 0.82
  Validation Loss: 0.51
  Validation took: 0:00:04

======== Epoch 4 / 4 ========
Training...
  Batch    40  of    241.    Elapsed: 0:00:15.
  Batch    80  of    241.    Elapsed: 0:00:30.
  Batch   120  of    241.    Elapsed: 0:00:46.
  Batch   160  of    241.    Elapsed: 0:01:01.
  Batch   200  of    241.    Elapsed: 0:01:16.
  Batch   240  of    241.    Elapsed: 0:01:31.

  Average training loss: 0.13
  Training epcoh took: 0:01:31

Running Validation...
  Accuracy: 0.83
  Validation Loss: 0.59
  Validation took: 0:00:04

Training complete!
Total training took 0:06:12 (h:mm:ss)
```
