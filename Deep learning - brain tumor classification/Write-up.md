# Brain Tumor Classification with CNN on MRI images
by Nick Kim

## Abstract
The goal of this project was to identify brain MRI images which contain intracranial tumor using convolutional neural network ("CNN"). A simple CNN model built from scratch achieved a very high recall score, which was further incrementally improved by employing transfer learning. 

## Design
Diagnosing all cancers developing internally is a difficult task as the most precise option of biopsy would require a certain level of invasive procedure. In the case of brains, biopsy in itself increases risk for the patient (or non-patient) and therefore image-based diagnosis is the main option for those concerned. However, image-based diagnostics are known to be vulnerable to errors, according to one study at about 5% rate for adults. The project aims to find out whether machine learning techniques can be a helpful tool for medical practitioners facing these issues. 

## Data
The main dataset comes from Kaggle ([here](https://www.kaggle.com/abhranta/brain-tumor-detection-mri)), with additional data also from Kaggle ([here](https://www.kaggle.com/masoudnickparvar/brain-tumor-mri-dataset)). The main dataset consists of 3,000 MRI images split evenly between those containing tumors and those without, which are shown below. The additional dataset adds about 7,000 images with the positive class (with tumor) outsizing the negative class by 2:1. Prior to model training, training dataset images were resized to pixel dimension of 224 by 224 with augmentation. 

![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/06%20Deep%20Learning/support/sample%20training%20data.png)


## Algorithms
- Image preprocessing techniques
- Exploratory data analysis to inspect data 
- PCA

Models
- Convolutional neural network ("Custom CNN model")
- Transfer learning with MobileNetv2 ("MobileNet model")
- Logistic regression for baseline modeling

Model Evaluation and Selection
- Logistic regression, with PCA, established 73% accuracy as a baseline. This was quickly outperformed by deep learning techniques. 
- Custom CNN model with 5 convolutional layers were trained on the main dataset of 3,000 observations. It achieved above 99% training accuracy, but given the size of the training dataset and simplicity of the model, the ability to generalize was questionable. 
- Custom CNN model and MobileNet model were trained with an expanded dataset of additional 7,000 observations. Both models demonstrated high levels of training accuracy and Custom CNN model achieved 97% accuracy and recall. MobileNet model incrementally improved the predictive performance to 98% accuracy (and 99% recall).  
- While model training time was not as important in model selection process, due to computational budget constraints, MobileNetv2 was selected for speed as a base layer for transfer learning. 
- Certain convolutional filters were able to capture the tumor as outlined by the activation heatmap shown below. However, given the nature of the task at hand, there remains a need to improve the model with capturing certain types of tumor images as implied by the recall score.

Custom CNN model - 1st convolutional layer output
![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/06%20Deep%20Learning/support/1_conv2d_5.png)


Custom CNN model - last convolutional layer output
![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/06%20Deep%20Learning/support/5_conv2d_8.png)

## Communication
The output is communicated in a 5-minute presentation containing visualizations using Keract and VisualKeras, among others. 


