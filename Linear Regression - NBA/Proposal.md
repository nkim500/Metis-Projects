# Project proposal for interpreting the relationship between Non-Fungible Tokens ("NFTs") and their prices

While valuation of artistic assets or collectibles in general are not standardized in process as well as, say, regulated financial products are and in large part based on subjectivity, this project aims to find whether there are any features that makes a Non-Fungible Token more expensive than another. 

Non-Fungible Tokens ("NFTs") are 'digital assets' stored on certain blockchain ledgers such as Ethereum and can be 'minted' as almost anything from short films to virtual cannabis farms. The blockchain ledgers enable verification of product originality and secured record of ownership (in perpetuity, in theory). The underlying technology and general interest in cryptocurrency assets have recently garnered excitement in NFTs as well, specifically around digital arts and sports collectibles, often in connection with their extravagant price tags. 

NFTs have primary and secondary markets where they are bought and sold like any other artworks. This project will attempt to quantify any relationships between valuations of various types of NFTs and their features, if any exist, by analyzing recent primary and secondary NFT transaction details available on these markets and additional sources in the manner described below.

- Data:
  - Primary dataset will be scraped and compiled from websites with NFT transaction information, including but not limited to sites such as SuperRare (https://superrare.com/), Foundation (https://foundation.app/), NBA Top Shop (https://nbatopshot.com/), Open Sea (https://opensea.io/), and Coinranking.com (https://coinranking.com/). 
  - Each rows of about 1,000, will represent an individual NFT artwork
  - Each columns of about 10 or more features, will include latest sale price in Ethereum ("ETH") (the target value), art dimension, art type (e.g. animation, moving, real, abstract, has character/subject), days since creation (age of the NFT), edition #, secondary transactions information (frequency traded in per days since created, max price change in %, median price change in % between transactions)

- Algorithms:
  - Exploratory data analysis techniques and visualizations for surveying the datasets
  - Linear regression model and validation techniques to interpret any patterns within the data

- Tools:
  - BeautifulSoup and Selenium for data collection (web scraping)
  - Matplotlib, Seaborn, Numpy, pandas and others for data manipulation
  - Scikit-learn for linear regression model

- Minimum viable product: 
  - Linear regression model output (e.g. coefficients, R2, etc) using subset of data and interpretation of such outputs in the context of the target variable
