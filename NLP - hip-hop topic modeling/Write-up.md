# Topic modeling with rap lyrics
Nick Kim

## Abstract
The goal of this project was to understand latent topics within rap lyrics using natural language processing techniques and topic modeling algorithms. The motivation for this project was a personal one, though content based filtering that this project can develop to would add a layer of robustness to recommendation systems currently employed by music content providers. 

## Design
The music and culture of rap and hip-hop are ubiquitous and a popular form of content enjoyed worldwide. This genre is also further segmented by subgenres with distinct styles and contents, but they share certain common denominators that help identify them as a member of this genre. The project used natural language processing techniques and topic modeling on lyrics of songs from roughly 40 very well-established rap artists to uncover the common denominator.

## Data
The dataset comes from Kaggle ([here](https://www.kaggle.com/mathisco01/wu-tang-clan-lyrics-dataset?select=scrapes), [here](https://www.kaggle.com/rikdifos/rap-lyrics), and [here](https://www.kaggle.com/juicobowley/drake-lyrics)). The raw dataset consists of song lyrics from roughly 40 artists. The dataset was processed in two different ways for topic modeling - by each verse (translating to about +10,000 documents) and by each line within a verse (+100,000 documents).  These documents were processed using NLP techniques and decomposed via SVD for further modeling, consisting roughly of 30,000 word tokens. 

## Algorithms
- Text processing techniques, including part of speech tagging using spaCy and encoding error fix via FTFY
- Exploratory data analysis to inspect data 
- SVD
- PCA

Models
- Latent Dirichlet Allocation, Non-Negative Matrix Factorization, and Correlation Explanation topic modeling 
- K-Means and DBSCAN clustering models for unsupervised learning on document-topic matrix

Model Evaluation and Selection
- LDA, NMF and CorEx were trained at various parameter levels using vectorized documents also using various parameters, including stop words (with or without parts of speech tagging), maximum document frequency and maximum features.
- Due to the nature of the data, CorEx which allowed for anchoring with keywords was able to separate documents into more comprehensible topics than others, judging from domain knowledge. The performance of CorEx model was further reinforced by its correlation score. 
- Clustering techniques K-Means and DBSCAN were also used on the doc-topic matrices however did not perform very well at various parameters and was not considered for inclusion in the communication, as more text processing seems to be warranted first.


## Communication
The output is communicated in a 5-minute presentation containing visualizations using Seaborn and pyLDAvis. 


