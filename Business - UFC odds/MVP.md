# Exploratory data analysis of UFC fights and betting odds

### Brief intro
This project aims to help fine-tune opening odds for an online sports betting company. The dataset contains fight statistics and closing betting odds for UFC fights. UFC has grown in popularity over the years as you can see from the number of fights per annum in the bar chart below. The continued success of this sport makes UFC an interesting opportunity for online sports betting companies to capitalize on.

![Image](https://github.com/nkim500/Metis_Projects/blob/main/03%20Business/support/fight_freq_pa.png?raw=true)



Opening odds are listed on respective online sports betting venues around the time when fights are announced. The listed odds will change over the course of time depending on new information as well as due to influx of bets, until the fight begins when the closing odds take effect. By having an accurate forecast of the closing odds, online sports betting companies, or effectively the bookmaker, can maximize their revenue potential from each fight.

When a moneyline reads -110 / +120 for a fight between a fighter from the red corner ("Red fighter") vs. a fighter from the blue corner ("Blue fighter"), the odds imply that the Red fighter is more favored to win the bout. For whoever is betting on the fight, this implies that if the Red fighter in fact wins the fight, a bet of $110 for the Red fighter pays out $100. On the other hand, if the Blue fighter wins the fight, a bet of $100 for the Blue fighter pays out $120. The spread for this particular moneyline would be 230. While this moneyline implies the probability for either fighter to win is relatively even, if the probability of winning is as close as a coin toss, both sides of the moneyline could have negative readings (e.g. -110 / -105)

Many times, either fighter is expected to have a relatively similar probability of winning, as you can see from the charts below (e.g. distribution of all spreads). Furthermore, the spread for a title bout tends to have more extreme moneyline readings.

![Image](https://github.com/nkim500/Metis_Projects/blob/main/03%20Business/support/Dashboard%201.png?raw=true)

![Image](https://github.com/nkim500/Metis_Projects/blob/main/03%20Business/support/Dashboard%203.PNG?raw=true)



The modeling process subsequent to data cleaning and EDA will use fighter profile, their previous records, the same information on the opponent, and other relevant information to forecast the closing moneyline.
