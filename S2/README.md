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

After the forward pass, the weights w1-w8 need to be finetuned so that the further calculations start to become optimal, so as to reduce the error between the predicted and ground truth values.

For example, the value of h1 is w1\*i1 + w2\*i2. This equation is used to calculate h1 during the forward pass. After that, the activation function (sigmoid, in this case) is applied to h1 and this gives us the value of a_h1. This value is further used to calculate the value of o1, which is equal to w5\*a_h1 + w6\*a_h2, based upon the connections shown in Figure 1. Then, the activation of o1 is calculated and this gives us the value of a_o1. This value is compared with the actual target output value and the error is calculated, which indicates how far the predicted value is from the actual value. Since there are two output neurons and two target values, the errors from both the predicted values are summed to obtain the total error value.


Before the next iteration of forward propagation takes place, the weights are slightly adjusted. This is done using one of the many available optimization algorithms. In this case, we are using the "Stochastic Gradient Descent" algorithm. In this algorithm, the partial derivative of the output error with respect to every weight is calculated. This tells us how much and in what direction does the error travel in the error-weight graph, for every change in the weight in a particular direction.

For example, let's say we are calculating the gradient of error with respect to weight w5 at first. This tells us what level of impact does the change in weight value w5 have on the total error. To calculate this gradient, we use the chain level differentiation, as their are multiple nodes/neurons in between the weight w5 and the error E_Total, which influence the change in value of error E_Total.

</br>
<b>Figure 4 : Backpropagation starting from the final layers</b>

![image](https://user-images.githubusercontent.com/65642947/118336608-a74f1400-b52f-11eb-9dd2-ad4ab74fe251.png)

When calculating the gradient of total error with respect to w5, we do not consider E2 as according to Figure 1, w5 has no effect on E2.

Similarly, we calculate the gradients/partial derivatives of the total error with respect to weights just before the final layer (w5, w6, w7, w8) and consider the nodes that bare an impact on the respective weights when their values are changed. 

Next, to calculate the gradients of the error with respect to the previous layers, there are additional nodes that come into the picture. For example, when calculating the gradient of error with respect to weight w1, we need to consider the two connections to the node a_h1, which are borne by weights w7 and w5. In order to do this, we first calculate the gradient of error with respect to the node a_h1 first, which includes the connections from nodes o1 and o2 and then we sum these gradient values. Further, there is a single common connection from a_h1 to weight w1, which goes through h1. We multiply this gradient with the summed gradient values from the two connections leading upto a_h1.

</br>
<b>Figure 5 : Backpropagation as it moves on to the initial layers</b>

![image](https://user-images.githubusercontent.com/65642947/118337304-2264fa00-b531-11eb-9176-bdd5d5e914d0.png)

Similarly, we calculate the weights w2, w3 and w4, which lie in the first layer and have multiple connections leading up to them.

After calculating the gradients for all the weights, we adjust the weights using the SGD algorithm, which states

<i>New weight = Old weight - Learning Rate * Gradient of error with respect to that weight</i>

Once all the existing weights in the connection are adjusted, the forward pass takes place again and the output is calculated again. After that, the weights are adjusted again using backpropagation. This keeps on going for a specific number of iterations as specified by the user. The effectiveness of this algorithm can be viewed by observing the total error value at each iteration. The algorithm results in reduction of the total error, given the learning rate is neither too large to prevent error from overshooting nor too small to prevent error stagnation.

</br>
<b>Figure 6 : Iterations indicating the reduction of total error through the use of SGD Optimization Algorithm</b>

![image](https://user-images.githubusercontent.com/65642947/118337998-b2f00a00-b532-11eb-9ca9-76d17870ae02.png)

It can be observed from the above figure that E_Total keeps reducing at every iteration.

It is also indicated in the following error graph with a Learning Rate of 0.5

</br>
<b>Figure 7 : Error Graph for Learning Rate of 0.5</b>

![image](https://user-images.githubusercontent.com/65642947/118338243-432e4f00-b533-11eb-8656-c38a80a78590.png)

</br>
<b>Figure 8 : Error Graph for Learning Rate of 0.1</b>

![image](https://user-images.githubusercontent.com/65642947/118338454-cb145900-b533-11eb-8ad8-dee9a9386eee.png)

</br>
<b>Figure 9 : Error Graph for Learning Rate of 0.2</b>

![image](https://user-images.githubusercontent.com/65642947/118338509-f5fead00-b533-11eb-82e4-39e8d434bb95.png)

</br>
<b>Figure 10 : Error Graph for Learning Rate of 0.8</b>

![image](https://user-images.githubusercontent.com/65642947/118338583-20e90100-b534-11eb-8c0a-1412fa69efce.png)

</br>
<b>Figure 11 : Error Graph for Learning Rate of 1.0</b>

![image](https://user-images.githubusercontent.com/65642947/118338638-47a73780-b534-11eb-937a-84a3fded6296.png)

</br>
<b>Figure 12 : Error Graph for Learning Rate of 2.0</b>

![image](https://user-images.githubusercontent.com/65642947/118338708-6e656e00-b534-11eb-8cfd-f8221313f609.png)

As we can see here, as the LR is increasing, the error seems to be converging better. This will not be the case everytime, as the current network that we are using is a simple 2 neuron network. Ideally, we need to start from a low LR and we need to slowly increase it till we find an optimal LR.


