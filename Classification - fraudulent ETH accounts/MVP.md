# Minimum viable product for classification modeling of fraudulent Ethereum wallets

This project aims to train a classification model to identify and, in the future, predict Ethereum wallets engaged in fraudulent activity. While further analysis is warranted, initial thoughts on cost-benefit analysis leans towards prioritizing recall over precision and accuracy. 

The model output is intended to be used as a cautionary notice (in a manner similar to a blacklist, but without enforceability) to the blockchain users who will be transacting with the fraudulent wallets as identified by the model. In other words, the users will be referencing this model output but still can transact as needed, thereby instilling user confidence in making transactions on the blockchain but avoiding potential headlines such as ["A $50 Million Hack Just Showed That the DAO Was All Too Human"](https://www.wired.com/2016/06/50-million-hack-just-showed-dao-human/).

The binary target variable, the flag for fraudulent wallet marked as '1', consists roughly 20% of the raw dataset:

![Image](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/pie_flag.png?raw=true)

A [pairplot](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/pairplot_all.png?raw=true) on predictor variables, generated for simple visual inspection of these features, did not provide any meaningful insight on data separability. Many of the predictor variables display a right-skewed distribution. The orange hue indicates observations which were flagged as 'fraudulent'.


Other than standard scaling for the purposes of kNN, data was not processed for the following outputs in baseline modeling. The baseline model metrics are as follows: 

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

The initial findings show that the random forest classifier was able to outperform other classifiers with a recall around 96% on the validation set. 

Within the remaining timeframe, below items will be visited to improve model effectiveness: 
1. Address target variable imbalance
2. Ability to generalize
3. Feature engineering, including the wallet's most frequently transacted ERC20 token, which is a categorical feature in a string format
4. Ensemble methods combining various models 

Lastly, the random forest classifier ranks the feature importance on the raw dataset as shown below: 
![Image](https://github.com/nkim500/Metis_Projects/blob/main/04%20Classification/support/Feature_importance_baseline.png?raw=true)
