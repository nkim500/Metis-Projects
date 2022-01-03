# Project proposal for identifying fraudulent wallets on Ethereum blockchain

Ethereum allows its users to create their own applications, such as smart contracts with several lines of codes. The codes, as is the blockchain ledger itself, is available to public to view. Once a smart contract is deployed, the code cannot be manipulated until it is fully executed. While a small minority, 'fraudulent' transactions involving these smart contracts and Ethereum blockchain do take place, at times manifesting into headlines such as ["A $50 Million Hack Just Showed That the DAO Was All Too Human"](https://www.wired.com/2016/06/50-million-hack-just-showed-dao-human/). Using a fraudulent Ethereum wallet dataset, the project aims to train a classification model that is able to identify wallets that have deployed 'fraudulent' contracts to support the Ethereum Foundation in instilling user confidence.

- Data:
  - The dataset comes from [Kaggle](https://www.kaggle.com/vagifa/ethereum-frauddetection-dataset).
  - Each rows of about 9,800, represents a wallet on the Ethereum blockchain
  - Each columns of about 50 or more features, includes wallet address, average minute between transactions involving the said wallet, # of sent transactions, # of received transactions, # of created contracts, # of unique 'received from' addresses, # of unique 'sent to' addresses, maximum and minimum value received, average value received, total amount of Ether transacted, Ether balance, data points regarding other Ethereum-based tokens used in transactions involving the wallet, and fraudulent wallet flag.   

- Algorithms:
  - Exploratory data analysis techniques and visualizations for surveying the datasets
  - Classification model and validation techniques

- Tools:
  - Matplotlib, Seaborn, Numpy, pandas and others for data manipulation
  - Scikit-learn for classification model

- Minimum viable product: 
  - Baseline classification model output and interpretation of such outputs, potentially accompanied by relevant exploratory data analyses
