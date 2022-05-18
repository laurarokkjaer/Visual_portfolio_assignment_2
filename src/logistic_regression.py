# path tools
import sys,os
sys.path.append(os.path.join("..", "utils"))
# image processing
import cv2

# neural networks with numpy
import numpy as np
from tensorflow.keras.datasets import cifar10 
from neuralnetwork import NeuralNetwork

# machine learning tools
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Defining a function, giving it an appropiate name, with no arguments 
# This function takes the cifar10 data and splits it into test-training set
def logistic_regression():
    # Loading the data into training-test
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    # Defining the labels
    labels = ["airplane",
          "automobile",
          "bird",
          "cat",
          "deer",
          "dog",
          "frog",
          "horse",
          "ship",
          "truck"]
    # Making the images greyscale for both trainng and test set
    X_train_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_train])
    X_test_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_test])
    # Normalizing images 
    X_train_scaled = X_train_grey/255
    X_test_scaled = X_test_grey/255
    
    # Reshaping the data
    nsamples, nx, ny = X_train_scaled.shape
    X_train_dataset = X_train_scaled.reshape((nsamples,nx*ny))
    
    nsamples, nx, ny = X_test_scaled.shape
    X_test_dataset = X_test_scaled.reshape((nsamples,nx*ny))
    
    # Deining the logistic classifier
    clf = LogisticRegression(penalty = "none",
                         tol = 0.1,
                         solver = "saga",
                         multi_class = "multinomial").fit(X_train_dataset, y_train)
    
    # Making the predictions
    y_pred = clf.predict(X_test_dataset)
    # Printing the classification report 
    report = classification_report(y_test, y_pred, target_names = labels)
    #print(report)
    
    # Using .write to save the report in a .txt file in my outputfolder
    with open('../output/lr_report.txt', 'w') as my_txt_file:
        my_txt_file.write(report)
    
    print("Script succeeded: The following shows the classification report, which is also saved to the output-folder")
    print(report)

logistic_regression()

    