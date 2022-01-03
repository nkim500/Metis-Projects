# Improving risk management process for DraftKings in UFC moneyline betting by identifying upset results
Nick Kim

## Abstract
The goal of this project is to pitch a model that predicts upsets in a UFC fight, where less favored fighter results in a win over a more favored fighter. Professional fight records of each fighters, the betting odds for their match-ups, and engineered features from the raw features were used for exploratory data analysis which acted as a basis for the pitch.

## Design
Online sports betting companies ("OSBs"), such as DraftKings, generate revenue based on taking a cut of the bets they receive on the betting market they create. Especially in a two-way betting with fixed payouts, where the bets can be placed on either outcome of a sporting event, the payouts need to be designed in a way that the bookmaker would come out relatively risk-neutral. Therefore, OSBs are essentially in a risk management business using metrics such as tracking error (difference between expected return versus actual return) and value-at-risk (the expected loss amount at certain confidence intervals) and need to have accurate insights on all possible outcomes. However, unexpected events are commonplace in sports like UFC, where an underdog prevails over a favored contender. The idea in this project aims to tackle this uncertainty for the benefit of OSBs by proposing a predictive model for upset results. 

## Data
The data source comes from ![Kaggle](https://www.kaggle.com/rajeevw/ufcdata/discussion/186873). The full dataset with engineered features have about 150 attributes and 6,300 observations consisting of UFC bouts that took place between 2010 and 2020, the historical fight records for fighters competing in these bouts, the fighter profiles, and closing betting odds assigned to each bouts. 

## Algorithms
Feature engineering includes calculation of implied probability to win derived from the betting odds. This project consists of exploratory data analysis using MS Excel and Tableau and did not involve any specific modeling process. 

## Communication
The output is communicated in a 5-minute presentation containing visualizations. 


