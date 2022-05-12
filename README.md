# Visual Analytics - Spring 2022
# Portfolio Assignment 2

This repository contains the code and descriptions from the second assigned project of the Spring 2022 module Visual Analytics as part of the bachelor's tilvalg in Cultural Data Science at Aarhus University - whereas the overall Visual analytics portfolio (zip-file) consist of 4 projects, 3 class assignments as well as 1 self-assigned.

## Repo structure
### This repository has the following directory structure:

| **Folder** | **Description** |
| ----------- | ----------- |
| ```in``` | Contains the input data (will be empty) |
| ```out``` | Contains the results (outputs like plots or reports)  |
| ```src``` | Contains code for assignment 1 |
| ```utils``` | Contains helping functions that may have been used throughoyt the code |

Also containing a MITLICENSE for guidelines of how to reproduce and use the data in this repository, as well as a .txt reqirements-file, where the required installments will be listed.


## Assignment description
The official description of the assignment from github/brightspace:

For this assignment, you will take the classifier pipelines we covered in lecture 7 and turn them into two separate .py scripts. Your code should do the following:

One script should be called logistic_regression.py and should do the following:
- Load either the MNIST_784 data or the CIFAR_10 data
- Train a Logistic Regression model using scikit-learn
- Print the classification report to the terminal and save the classification report to out/lr_report.txt

Another scripts should be called nn_classifier.py and should do the following:
- Load either the MNIST_784 data or the CIFAR_10 data
- Train a Neural Network model using the premade module in neuralnetwork.py
- Print output to the terminal during training showing epochs and loss
- Print the classification report to the terminal and save the classification report to out/nn_report.txt

### The goal of the assignment 
The goal of this assignment was to demonstrate general knowledge abput .py scripts with simple classifiers that can act as benchmarks for future reasearch. 
The results are two report belogning to respectively the logistic_regression script and the nn_classifier script (see output folder)

## Methods
To solve this assignment i have worked with ```opencv``` for the general image processing. Furthermore i have used ```neural networks``` with ```numpy``` as well as ```tensorflow```, which is where the ```CIFAR_10```data is from. At last, the script is also build around multiple functions/methods and machine learning tools from ```sklearn``` shuch as ```LabelBinarizer```, ```train_test_split```, ```classification_report```and ```accuracy_score```.

## Usage (reproducing results)
For this .py script the following should be written in the command line:
- change directory to the folder /src 
- write the command: python logistic_regression.py or nn_classifier.py
- when processing there will be a message introducing the results, which is the two different classification reports
- The two reports is then shown in the output folder


## Discussion of results
something about:
- what a user defined input could have done to the reproducability of the script 
- the numbers on the report
- the difference between using a simple logistic regression classifier and a neural netowork class woth numpy 
