# Recommendations on street team placement in NYC to promote WomenTechWomenYes ("WTWY") annual summer gala and awareness
By Nick Kim

## Abstract
This project aims to identify and recommend time & location which maximizes WTWY's engagement with New Yorkers in promoting its annual gala and its reach in general. Exploratory data analysis was deployed on subway turnstile dataset, analyzing patterns and trends in NYC subway traffic. The findings are visualized in a presentation recommending a marketing campaign spanning about a week at locations attracting the highest level of traffic at certain time windows. 

## Design
This hypothetical advisory scenario designed by Metis aims to support a marketing campaign in New York City for a non-profit organization. The broad goal is to identify locations with high traffic such that the organization's street team would be able to efficiently engage its desired demographic. Its annual summer gala which is being promoted supposedly takes place in "early summer" and therefore the marketing was envisioned to be in months leading up to the event. By understanding the movement via NYC subway traffic data within various timeframes, WTWY is expected to successfully plan its marketing accordingly in line with its resource constraints.  

## Data
The primary dataset sourced from [MTA](http://web.mta.info/developers/turnstile.html) includes a time series data of cumulative entry and exit counts at each turnstiles in  NYC subway stations recorded generally at a 4-hour interval. Each cumulative entry and exit record is timestamped and linked to a specific turnstile, station and turnstile groupings in between, as well as tagged with a simple description. About 19 million observations from January to July in 2019, 2020 and 2021 were ingested and analyzed for exploratory data analysis. 

## Algorithms
Exploratory data analysis techniques are used in this analysis. 
1. Calculating summary/descriptive statistics to understand and clean datasets (e.g. mean, median and standard deviations)
2. Creating data visualization to communicate the findings via a heat map, violin plot, bar plot and line chart

## Tools
- SQLite3 and DB Browser to ingest a specified set of data relevant for analysis
- Pandas and Numpy indirectly to manipulate data
- Seaborn and Matplotlib to visualize

## Communication
The findings and recommendations are communicated in a 5-minute presentation, attached [in this repository](https://github.com/nkim500/Metis_Projects/blob/1ba73910e9af00ff64a177670f5bcbbb315acb55/01_EDA_MTA/Final/01%20EDA%20-%20MTA.pdf). 
