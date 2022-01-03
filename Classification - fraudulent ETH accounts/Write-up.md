# Classifying fraudulent Ethereum accounts
Nick Kim

## Abstract
The goal of this project was to create a binary classfication model that determines whether an Ethereum account is fraudulent or not. The trained classification model is able to take in an Ethereum account address as an input and opine the legitimacy of the account based on the account's activity. 

## Design
Cryptocurrency ecosystem is growing and in the process of establishing structure, but is also characterized by wide variety of fraudulent activities. While there are different efforts to recordkeep reported frauds and the associated accounts, the project proposes a method to approach this issue of fraud in a more proactive manner with classification models that can determine the legitimacy of an Ethereum account. By providing the ability to check counterparty risk to the public, the user confidence and effectively the adoption of the cryptocurrency should be positively impacted. Emphasis is placed on precision of model predictions as legitimate user transactions should not be negatively impacted by the model output. 

## Data
The primary data source is from [Kaggle](https://www.kaggle.com/vagifa/ethereum-frauddetection-dataset), for which the source is believed to be the publicly available Ethereum blockchain information. The raw dataset consisted of about 10,000 rows and 40 features including the binary target variable. Each row is an Ethereum account and attributes consist of the account's activity such as number of transactions conducted, amount of tokens received, and unique number of transacting parties. Target variable is imblanaced (roughly 20% positive and 80% negative class). 

## Algorithms
- Minor feature engineering such as converting strings to numeric categories 
- Exploratory data analysis to visualize patterns in data 
- GridSearchCV to determine optimal parameters for classification models
- Feature importance to understand RandomForest logic better

Models
- Logistic Regression (excluded from final evaluation)
- kNN
- RandomForest
- Extra-Trees
- XGBoost Classifier

Model Evaluation and Selection
- The dataset was split 20% for holdout and remainder to 10-folds when cross-validating with GridSearchCV. Main metrics for evaluating model performance was precision, along with accuracy, recall, F-beta, ROC-AUC, log-loss, and execution time. 
- Model performance at default threshold is as follows: 
(model / precision / accuracy / AUC / Log-loss / execution time in teesting)
1. kNN          / 0.77 / 0.90 / 0.927 / 0.63 / 0.199s
2. RandomForest / 0.99 / 0.99 / 0.999 / 0.04 / 0.027s
3. Extra-Trees  / 0.99 / 0.99 / 0.999 / 0.03 / 0.005s
4. XGBoost      / 0.97 / 0.99 / 0.997 / 0.04 / 0.003s
- Decision-tree based models outperformed in general. Extra-Trees displayed siginificant speed advantage over RandomForest, while displaying similar level of classification quality. However, RandomForest was able to reach 100% precision at a hard-decision threshold of 0.64, keeping the decline in recall relatively minimal whereas Extra-Trees only reached 100% precision at threshold of 0.88, at which point recall dropped siginficantly. Therefore, RandomForest is considered as the classification model of choice.

## Communication
The output is communicated in a 5-minute presentation containing visualizations using Seaborn and Matplotlib. 


