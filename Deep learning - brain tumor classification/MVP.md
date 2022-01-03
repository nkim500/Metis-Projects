# Minimum viable product for brain tumor MRI image classification

This project aims to train a deep learning model to classify MRI images of human brains by whether it contains a tumor or not. About 3,000 MRI images were used to train the models using different structures. 

The baseline convolutional neural network, with the structure specified below, was only able to achieve an accuracy of 2%. 
![Image](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/06%20Deep%20Learning/support/baseline%20CNN%20summary.png)

Epochs:           20
Steps per epoch:  25

The second CNN was built using MobileNetv2's feature maps based on ImageNet dataset. On top of the MobileNet architecture, 3 additional dense layers (as described below) were added. 
- Dense, 100 filters, activation relu
- Dense, 50 filter, activation relu
- Dense, binary classification output layer

With 20 epochs and 50 steps per epoch, performance of the transfer learning CNN model was able to improve to training accuracy of 98% and validation accuracy of 97%. Summary of the model fitting process is shown below: 
![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/06%20Deep%20Learning/support/MobileNet%20CNN%20model%20fit.png)

