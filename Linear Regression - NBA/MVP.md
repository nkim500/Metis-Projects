# Analyzing annual salaries of NBA players and their on-court performance

This project aims to interpret the relationship between NBA players and their on-court production. 

The following is a correlation coefficient for each predictor variables (with some basic feature engineering) from the initial dataset against the target variable. 

![picture](https://raw.githubusercontent.com/nkim500/Metis_Projects/main/02_Linear_Regression/support/Baseline%20r.png)

The following is another baseline model output, based on a narrower set of data selected based on intuition. 

![picture](https://github.com/nkim500/Metis_Projects/blob/main/02_Linear_Regression/support/Baseline%20r%20for%20smaller%20df.png?raw=true)

The following is a pairplot of subset of features from the initial dataset, which displays distribution of a variable against another in the dataset. Certain characteristics stand out, such as right-skewedness of the target variable 'salary_usd' and collinearity among certain features. 

![picture](https://github.com/nkim500/Metis_Projects/blob/main/02_Linear_Regression/support/pairplot.png?raw=true)

The model outputs and pairplot will help to guide the next steps in feature engineering, followed by model validation techniques, and ultimately in improving model r^2.
