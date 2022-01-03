# Minimum viable product for topic modeling of rap lyrics

This project aims to train a classification model to identify structure and (latent) topics within rap lyrics from various hip-hop artists. The final project output should be a basis for content-based recommendation system.

With songs from close to 40 artists, each verse including chorus is considered as an individual document. The entire corpus after basic data cleaning and tokenization is heavily right-skewed with most tokens only logging once.
![image](https://github.com/nkim500/Metis_Projects/blob/main/05%20Unsupervised_NLP/support/distribution%20of%20words.png?raw=true)

Baseline topic modeling output with the said data is shown below (along with the inputs and parameters). The segmentation of latent topics within the corpus is very unclear as seen from the pyLDAvis' output intertopic distance map (left) and term frequency list for a given topic (right), implying the need for further preprocessing on the data. 
![image](https://github.com/nkim500/Metis_Projects/blob/main/05%20Unsupervised_NLP/support/pyLDAvis_raw2.png?raw=true)


- CountVectorizer, English stop words, max_df = 0.01, min_df = 2, regex removes words consisting of less than 3 letters

- Latent Dirichlet Allocation, 10 topics
