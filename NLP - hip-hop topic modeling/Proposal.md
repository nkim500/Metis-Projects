# Project proposal for clustering rap by lyrics

Rap and hip-hop (used interchangeably herein) are music genres understood to have been around for about 50 years since its birth in - arguably - 1973. Generally, rap tends to employ larger amount of and wider variety of words per song. Furthermore, while many music genres containing vocals tend to focus on the pitch, note and voice, rap is charaterized by rhyming schemes and stylized delivery of the lyrics over a repetitive beat with a 4/4 time signature. 

Over the course of its history, the genre has evolved from a niche sub-segment to a mainstream genre, generating numerous artists whose names are familiar worldwide. Naturally, the maturation process of the genre also catalyzed various sub-genres which can be described by multiple factors, such as where the artist is from and what year the song was released. This project will try to categorize the styles of rap by analyzing the lyrics of some of the most famous rap artists over the past 30 years or so. 

- Data:
  - The dataset comes from Kaggle ([here](https://www.kaggle.com/mathisco01/wu-tang-clan-lyrics-dataset?select=scrapes), [here](https://www.kaggle.com/rikdifos/rap-lyrics), and [here](https://www.kaggle.com/juicobowley/drake-lyrics)).
  - Each text file attributable to an artist, compile lyrics of several songs from the artist
  - Each text file will be further segmented (e.g. by each verse) into an observation, which should generate a tabular dataset comprising of slightly more than 1,000 rows and 100 words for each row.

- Algorithms:
  - Exploratory data analysis techniques and visualizations for surveying the datasets
  - Natural language processing techniques including, but not limited to, tokenizing, text-data vectorization, and SVD for pre-processing
  - Unsupervised modeling, including clustering will be applied

- Tools:
  - Matplotlib, Seaborn, Numpy, pandas, NLTK, and spaCy and others for data visualization and manipulation
  - Scikit-learn, LSA, NMF, TF-IDF, count-vectorization among others for preparing the data for analysis

- Minimum viable product: 
  - Baseline topic modeling and EDA outputs will be presented
