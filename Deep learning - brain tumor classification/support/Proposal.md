# Binary classification - MRI images of brain tumor

Brain tumor is a mass or growth of abnormal cells in the brain. About 700,000 people in the US are living with a primary brain tumor and new cases arise at a pace of 85,000 per year. Brain tumors in general can affect various physical cabailities of the patient and the quality of life for the patient and people involved. While the survival rate is fairly high at 75% in general, 30% of cases are diagnosed as malignant and the five-year relative survival rate following a malignant tumor diagnosis is 36% and the same rate for glioblastoma, the most common malignant brain tumor, is 7% with median survival duration of 8 months. 

Data science techniques are known to improve medical diagnostics accuracy when accompanied by a specialist. In that context, this project aims to build a classification model for diagnosing brain tumor from MRI images using deep learning techniques. 

- Data:
  - The dataset comes from [Kaggle](https://www.kaggle.com/abhranta/brain-tumor-detection-mri).
  - There are 3,000 grayscale MRI images in the training dataset evenly split between those that have tumors and those that do not. There is another 60 images in the test dataset without labels. 
  - MRI images is currently in a jpeg format which will be appropriately preprocessed for neural network and other deep learning technique implementation. 

- Algorithms:
  - Exploratory data analysis techniques and visualizations for surveying the datasets
  - Deep learning algorithms including CNN will be applied  

- Tools:
  - Matplotlib, Seaborn, Numpy, pandas and others 
  - Scikit-learn, TensorFlow + Keras among others
  - Other classification modele packages such as random forest classifier or naive bayes classifier will be used for baseline modeling

- Minimum viable product: 
  - Baseline classification model output and interpretation of such outputs, potentially accompanied by relevant exploratory data analyses
