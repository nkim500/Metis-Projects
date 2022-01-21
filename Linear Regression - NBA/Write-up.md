# Interpreting the relationship between an NBA Player's salary and its predictor variables
Nick Kim

## Abstract
The goal of this project was to create a regression model which can interpret an NBA Player's salary in a mathematical way. Various feature combinations for each NBA players and the respective team(s), and appropriate derivatives of those features, were created for model training. Through multiple iterations of feature engineering, training, and validating, the final set of regression models, namely linear and ridge, lifted the R^2 from 0.53~0.57 at baseline to 0.6 at final.

## Design
By finding the most informative set of on-court performance predictor variables and using the appropriate regression model(s), we should be able to understand an athlete's fair value. While the motivation for the project originates from curiosity, understanding the fair value of athletes and the drivers should be helpful for the athletes themselves as well giving actionable information to stakeholders such as franchises, managers, trainers and agents.

## Data
The primary data source was [Basketball-Reference.com](https://www.basketball-reference.com/). The raw dataset consisted of about 2,800 rows and 48 features including the target. 25 of these features were per season on-court performance statistics, 6 of these were awards received by the athlete for the season, 5 of his team's regular season performance, 4 of the team's playoff performance (if any), and remainder attributable to the player profile. Much of the final set of predictor variables were engineered derivatives of them. 

## Algorithms
Feature engineering includes:
- Log-transformation of the target variable, annual salary of an athlete
- Converted positions, awards and other categorical features to binary dummy variables
- Created certain predictor variables specifically to address feature interactions

Models
- Ordinary least squared regression
- Regularizaiton and the appropriate scaling for LASSO, Ridge, and Elastic Net regression
- Regularization on its own for feature reduction support and with cross-validation for validation/testing

Model Evaluation and Selection
- The dataset was split 20% for test and remainder to 5-folds when cross-validating. Main metrics for evaluating model performance was R^2 and mean absolute error. 
- The regression models for the holdout performed as following: 
(model / R^2 / MAE with inverse log of base 10 applied)
1. Linear / 0.6066 / 1.2
2. Ridge / 0.6063 / 1.2
3. Elastic Net / 0.5856 / 1.2
4. Lasso / 0.5618 / 1.3
- Polynomial regression outperformed other models with a 0.675 R^2 at final testing. However, possibly also inferrable from the higher MAE (inversed) of 1.6, the polynomial regression was excluded from final consideration for showing signs of overfitting.

## Communication
The output is communicated in a 5-minute presentation containing visualizations using Seaborn and Matplotlib. 


