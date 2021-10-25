# Minimum viable product for classification modeling of fraudulent Ethereum wallets

This project aims to train a classification model to identify and, in the future, predict Ethereum wallets engaged in fraudulent activity. While further analysis is warranted, initial thoughts on cost-benefit analysis leans towards prioritizing recall over precision and accuracy. 

The binary target variable, flag for fraudulent wallet, consists roughly 20% of the raw dataset:

![Image](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/pie_flag.png?raw=true)

A pairplot on predictor variables, generated for simple visual inspection of these features, did not provide any meaningful insight on data separability. Many of the predictor variables display a right-skewed distribution. The orange hue indicates observations which were flagged as '1'. The pairplot can be found [here](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/pairplot_all.png?raw=true)


Other than standard scaling for the purposes of KNN, data has not been preprocessed for the following outputs in baseline modeling. The baseline model metrics are as follows: 

* The score for kNN is
  * Training:  93.16%
  * Test set:  92.19%
  * **F1 Score:  82.40%**
  * Precision:  79.78%
  * **Recall:  85.21%**

* The score for decision tree (with max depth of 10) is
  * Training:  97.06%
  * Test set:  93.14%
  * **F1 Score:  84.79%**
  * Precision:  83.38%
  * **Recall:  86.25%**

* The score for random forest (with 100 trees) is
  * Training:  99.95%
  * Test set:  95.43%
  * **F1 Score:  89.32%**
  * Precision:  83.38%
  * **Recall:  96.17%**

The initial findings show that the random forest classifier was able to outperform other simple classifier models with a recall around 96% on the validation set. 

Within the remaining timeframe, below items will be visited to improve model effectiveness: 
1. Ability to generalize
2. Feature engineering, including the wallet's most frequently transacted ERC20 token, which is a categorical feature in a string format
3. Ensemble methods combining various models 

Lastly, the random forest classifier currently ranks the feature importance as following: 
![Image](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/Feature_importance_baseline.png?raw=true)