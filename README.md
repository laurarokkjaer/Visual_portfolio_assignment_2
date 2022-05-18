Link to repository: https://github.com/laurarokkjaer/Visual_portfolio_assignment_2
# Visual Analytics - Spring 2022
# Portfolio Assignment 2

This repository contains the code and descriptions from the second assigned project of the Spring 2022 module Visual Analytics as part of the bachelor's tilvalg in Cultural Data Science at Aarhus University - whereas the overall Visual analytics portfolio (zip-file) consist of 4 projects, 3 class assignments as well as 1 self-assigned.

## Repo structure
### This repository has the following directory structure:

| **Folder** | **Description** |
| ----------- | ----------- |
| ```in``` | Contains the input data (will be empty) |
| ```out``` | Contains the results (outputs like plots or reports)  |
| ```src``` | Contains code for assignment 2 |
| ```utils``` | Contains utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), and which have been used in the assignments |

Also containing a ```MITLICENSE``` for guidelines of how to reproduce and use the data in this repository, as well as a ```.txt``` reqirements-file, where the required installments will be listed.


## Assignment description
The official description of the assignment from github/brightspace: [assignment description](https://github.com/CDS-AU-DK/cds-visual/blob/main/assignments/assignment2.md).

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


### Data source
The data used in this assignment is the CIFAR-10 dataset from [the cifar-10 dataset website](https://www.cs.toronto.edu/~kriz/cifar.html). 

Reference: [Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf), Alex Krizhevsky, 2009.

## Methods
To solve this assignment i have worked with ```opencv``` for the general image processing. Furthermore, i have used ```neural networks``` with ```numpy``` as well as ```tensorflow```, which is where the ```CIFAR_10```data is from. At last, the script is also build around multiple functions/methods and machine learning tools from ```sklearn``` shuch as ```LabelBinarizer```, ```train_test_split```, ```classification_report```and ```accuracy_score```.

## Usage (reproducing results)
These are the steps you will need to follow in order to get the script running and working:
- load the given data into ```input```
- make sure to install and import all necessities from ```requirements.txt``` 
- change your current working directory to the folder before src in order to get access to the input and utils folder as well 
- the following shpuld be written in the command line:

      - cd src (changing the directory to the src folder in order to run the script)
      
      - python logistic_regression.py/nn_classifier.py (calling the function within the script)
      
- when processed results there will be a messagge saying that the script has succeeded and the outputs can be seen in the output folder 


## Discussion of results
The first thing to get into in terms of the results of this assignment is the different classification reports respectively the logistic regression vs. neural network classifier. The neural network classifier is more flexible than the logistic regression which might be the answer to why the accuracy is higher with the nn_classifier.py script. But since the difference between 32% and 35% is not that big, I would argue that the logistic regression works just as fine.
For furter development it would have been interesting to have a look at the resluts using the MNIST_784 dataset instead of CIFAR10. The solution to that would have been to create just one script which takes an argument in which the user can choose to run the script with one of the two datasets. 
