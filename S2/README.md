# Neural Network Backpropagation

This folder demonstrates the backpropagation technique in a Neural Network.

The NN_Backprop.xlsx excel workbook in this folder has been created to give a detailed demonstration of Back Propagation in Neural Networks

Consider a simple 2 input, 2 output Neural Network with 1 hidden layer consisting of 2 neurons.

</br>
<b>Figure 1 : Simple Neural Network</b>

![image](https://user-images.githubusercontent.com/65642947/118331899-df9e2480-b526-11eb-9232-b956a1f91b4a.png)

Here, i1 and i2 are the input neurons, t1 and t2 are the final target/ground truth values for the network. h1 and h2 are the hidden neurons and a_h1, a_h2 are the respective activations of those neurons that are obtained by applying sigmoid function to the outputs from h1 and h2 neurons. Similarly, o1 and o2 are the output neurons and a_o1 and a_o2 are their respective activations. E1 and E2 are the errors associated with outputs from a_o1 and a_o2 and E_Total is the cumulative error, which is E1+E2.

There are 8 weight values, ranging from w1 to w8 that play a major role in predicting the output. For convenience, bias in this simple neural network has been turned off. The two inputs i1 and i2, target values t1 and t2 and weights w1-w8 are initially set with arbitrary values before beginning the calculations. The learning rate (LR) used to update the weights is set at 0.5 but results have been illustrated for different learning rates.

Following are the arbitrary values that have been set for some of the parameters.

<ul>w1 = 0.15</ul>
<ul>w2 = 0.2</ul>
<ul>w3 = 0.25</ul>
<ul>w4 = 0.3</ul>
<ul>w5 = 0.4</ul>
<ul>w6 = 0.45</ul>
<ul>w7 = 0.5</ul>
<ul>w8 = 0.55</ul>
<ul>i1 = 0.05</ul>
<ul>i2 = 0.1</ul>
<ul>t1 = 0.01</ul>
<ul>t2 = 0.99</ul>
<ul>LR = 0.5</ul>

</br>
<b>Figure 2 : Value assignments</b>

![image](https://user-images.githubusercontent.com/65642947/118333278-0cebd200-b529-11eb-9af6-15b1a5bf33c7.png)

The connection layers of these inputs, weights and outputs are shown in Figure 1 above.

First, a forward pass of the values through these connections take place. These are the initial set of random calculations to arrive at a prediction value but since the values are random at first, chances are that the predicted value could be far from the ground truth values. 

In this forward pass, the intermediate values such as the outputs of hidden layers, their activations, outputs from the output neurons and errors associated with the actual and predicted values are calculated. The objective of this forward pass is to arrive at an output, be it perfect or not.

</br>
<b>Figure 3 : Forward pass equations</b>
![image](https://user-images.githubusercontent.com/65642947/118334020-699bbc80-b52a-11eb-98d3-6902fa6cc96f.png)
