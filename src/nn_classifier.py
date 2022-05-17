# path tools
import sys,os
sys.path.append(os.path.join("utils"))

# image processing
import cv2

# tools from sklearn
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

# neural networks with numpy
import numpy as np
from tensorflow.keras.datasets import cifar10 
from utils.neuralnetwork import NeuralNetwork 

# Defining a function, giving it an appropiate name, with no arguments 
def main():
    # Load data
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
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
    
    # Making the images greyscale
    X_train_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_train])
    X_test_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_test])
    
    # Normalizing the traning and test
    X_train_scaled = X_train_grey/255
    X_test_scaled = X_test_grey/255
    
    # BInarizing the labels
    lb = LabelBinarizer()
    y_train = lb.fit_transform(y_train)
    y_test = lb.fit_transform(y_test)
    
    # Reshaping the data for both training and test
    nsamples, nx, ny = X_train_scaled.shape
    X_train_dataset = X_train_scaled.reshape((nsamples,nx*ny))
    
    
    nsamples, nx, ny = X_test_scaled.shape
    X_test_dataset = X_test_scaled.reshape((nsamples,nx*ny))
    
    # Using neural network model 
    print("[INFO] training network...")
    input_shape = X_train_dataset.shape[1]
    nn = NeuralNetwork([input_shape, 64, 10])
    print(f"[INFO] {nn}")
    #Fitting the datasets
    nn.fit(X_train_dataset, 
           y_train, 
           epochs = 10, 
           displayUpdate = 1)
    
    # Making the predictions
    predictions = nn.predict(X_test_dataset)
    y_pred = predictions.argmax(axis=1)
    
    # Printing the clsassificationreport
    report = classification_report(y_test.argmax(axis=1), 
                                   y_pred, 
                                   target_names = labels)
    print(report)

    # Using .write to save the report in a .txt file in my outputfolder
    with open("output/nn_report.txt", 'a') as my_txt_file:
        my_txt_file.write(report)
  
    
# python program to execute
if __name__ == "__main__":
    main()