# Wind forecast app for kitesurfers 
Nick Kim

## Abstract
The goal of this project was to deploy a web app that captures wind and temperature data designed for kitesurfing. Underneath the hood, Python script takes in a user query via the Streamlit app and reqeuests weather forecast data from API endpoints hosted by the US government website Weather.gov. The API output for the queried location is parsed and processed to provide weather forecast data in a visual, along with the same for the neighboring locations. Furthermore, historical data for select locations in the US known for kitesurfing is presented to give guidance on seasonality of the local winds. 

## Design
Kitesurfing requires a particular weather condition to be met. While there are many useful weather forecast data and apps available, having a view that is specific for the needs of a kitesurfer would be beneficial for those just starting out in the sports and for those who are crunched with time to piece the necessary forecast information together. This app aims to collect the relevant information in a dashboard and present it to the user to facilitate their beach day planning ahead of time. 

## Data
Wind speed, wind direction and dry bulb temperature forecast data is collected using Weather.gov API, which is accessed by plugging in the latitude and longitude of US weather stations from a csv file. There were about 7,000 coordinates for weather observation points, but was narrowed down to about 4,500 based on the availability of forecast API endpoint. The historical weather data for about 17 locations dating back to 2012, generally speaking, are downloaded from NOAA website and stored in a SQL database.

## Web application
- The web application based on Streamlit and Python script will allow user to query a station code, retrievable from the displayed US weather station map. The script will retrieve forecast data from Weather.gov's API endpoints for relevant stations and visualize wind speed, wind direction and temperature for the next one week period, depending on whether the data is available. 
- [Web app can be accessed via here](https://share.streamlit.io/nkim500/metis_projects/main/07_Engineering/streamlit_app_2.py)
- [Web app script can be found here](https://github.com/nkim500/Metis_Projects/blob/main/07_Engineering/streamlit_app_2.py)

## Tools
- Weather.gov API and `requests` Python package for data access
- Altair and Matplotlib for visualization
- SQLite3 for data storage
- Streamlit for app development and deployment

## Communication
The output is communicated in a 5-minute presentation containing visualizations. 


