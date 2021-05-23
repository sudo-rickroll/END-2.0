# Predicting the sum of MNIST Classification and a random single number digit

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sudo-rickroll/END2/blob/main/S3/main.ipynb)

This folder contains the package for prediction of the sum of an MNIST image and a random single digit number.

This project contains the following folder and file components:

<ul>
  <li><b>checkpoint</b> - The folder where the model checkpoint is stored.</li>
  <li><b>config</b> - The folder where the configuration file is stored.</li>
  <li><b>graphs</b> - The package where the python module to plot output graphs exists.</li>
  <li><b>images</b> - The folder where the output images (like graphs) are stored.</li>
  <li><b>models</b> - The package where the python module for model/architecture exists.</li>
  <li><b>parsers</b> - The package where the python modules to parse the configuration file and the command line arguments, exists.</li>
  <li><b>utils</b> - The package where the python modules for utility functions like dataset, dataloader and for the processes like train, test and running the pipeline, exists.   </li>
  <li><b>main.ipynb</b> - The colab notebook file to run the entire process and displays log the outputs during the process. (<i>Note: In this notebook, the process is run considering that the repository is already cloned to google drive.</i>)</li>
  <li><b>main.py</b> - The python file that contains the entry point to the entire pipeline.</li>
</ul>

## Using this repository

### On local desktop machine

Clone this entire subdirectory in the <b>END2</b> repository onto your local desktop using the following commands one by one (press enter key after each command) through git bash or terminal:</br>
`git clone --depth 1 --filter=blob:none --sparse "https://github.com/sudo-rickroll/END2/"`</br>
`cd "END2"`</br>
`git sparse-checkout set S3`</br>





