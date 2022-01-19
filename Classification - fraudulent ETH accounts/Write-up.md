# Classifying fraudulent Ethereum accounts
by Nick Kim

## Abstract
The goal of this project was to create a binary classfication model that determines whether an Ethereum account is fraudulent or not. The trained classification model is able to take in an Ethereum account address as an input and opine on the legitimacy of the account based on the account's activity. 

## Design
Cryptocurrency ecosystem is growing and in the process of establishing structure, but is also characterized by wide variety of fraudulent activities. While there are different efforts to recordkeep reported frauds and the associated accounts, this project considers a more proactive approach - creating a fraud account classification model which could be the basis for a potential counterparty screening tool. In evaluating the models, the emphasis was placed on precision to minimize undue caution between legitimate users and avoid disruption for legitimate transactions. 

## Data
The primary data source is from [Kaggle](https://www.kaggle.com/vagifa/ethereum-frauddetection-dataset), which consists of data from publicly available Ethereum blockchain. The raw dataset consisted of about 10,000 rows and 40 features including the binary target variable. Each row is an Ethereum account and attributes consist of the account's activity such as number of transactions conducted, amount of tokens received, and unique number of transacting parties. Target variable is imblanaced (roughly 20% positive and 80% negative class). 

## Algorithms
- Minor feature engineering such as converting strings to numeric categories 
- Exploratory data analysis to visualize patterns in data 
- GridSearchCV to determine optimal parameters for classification models

Models
- Logistic Regression (excluded from final evaluation)
- kNN
- RandomForest
- Extra-Trees
- XGBoost Classifier

Model Evaluation and Selection
- The dataset was split 20% for holdout and remainder to 10-folds when cross-validating with GridSearchCV. Main metrics for evaluating model performance was precision, along with accuracy, recall, F-beta, ROC-AUC, log-loss, and execution time. 
- Model performance at default threshold (0.50) is as follows<sup>*</sup>: 
(model / precision / accuracy / AUC / Log-loss / execution time in teesting)
1. kNN          / 0.77 / 0.90 / 0.927 / 0.63 / 0.199s
2. RandomForest / 0.99 / 0.99 / 0.999 / 0.04 / 0.027s
3. Extra-Trees  / 0.99 / 0.99 / 0.999 / 0.03 / 0.005s
4. XGBoost      / 0.97 / 0.99 / 0.997 / 0.04 / 0.003s
<sup>* As scripts were executed again, the evaluation metrics in the code outputs may differ from above</sup>
- Decision-tree based models outperformed in general. Extra-Trees displayed siginificant speed advantage over RandomForest, while displaying similar level of classification quality. However, RandomForest was able to reach 100% precision at a hard-decision threshold of 0.64, keeping the decline in recall relatively minimal whereas Extra-Trees only reached 100% precision at threshold of 0.88, at which point recall dropped siginficantly. Therefore, RandomForest is the preferred classification model.

## Communication
The output is communicated in a 5-minute presentation containing visualizations using Seaborn and Matplotlib. 
