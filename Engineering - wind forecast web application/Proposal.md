# Wind speed and direction forecasting around Plumb Beach, Brookyln

Wind powered sports require a specific condition to be met for participants to engage in the activity. In the case of kitesurfing, the wind speed and wind direction are some of the major factors that determine the feasibility of the sports. For an average rider with average kitesurfing equipments, the general threshold for wind speed to successfully engage in the sports is 12 knots (14mph or 22kph).  

Certain parts of the world - e.g. Cabarete, Aruba, Northern coasts of Brazil and parts of Sicily - are blessed with a long seasonal window displaying consistent wind condition for kitesurfing. However, in most parts of the world, the optimal conditions - if available - are presented with a much narrower seasonal window, and not always consistently even within it. Due to this dependency on the environmental conditions, most beginners who are limited to local conditions typically need to dedicate the entire day on the beach waiting for the right conditions to practice.

In order to facilitate the learning process for beginners, as well for all riders bound to local conditions, this project aims to deploy a wind speed and direction forecasting model to a web application, such that participants can plan ahead accordingly and make efficient use of their time for kitesurfing. 

- Data:
  - The base dataset comes from [National Centers for Environmental Information ("NCEI")](https://www.ncei.noaa.gov), which is a US government agency operated by an office of the National Oceanic and Atmospheric Administration ("NOAA").
  - The base dataset contains a historical hourly weather condition data dating back to 2012 for John F. Kennedy International Airport, which acts as a proxy for the weather conditions at Plumb Beach in Brooklyn. This dataset will train a neural network model to forecast (i) wind speed and (ii) wind direction.
  - The model will generate hourly wind forecasts on a daily basis based on the regularly incoming data from [National Weather Service](https://www.weather.gov), also an agency operated by NOAA, using the publicly available API. 

- Algorithms:
  - Neural network model (Keras)

- Tools:
  - Python packages to request and ingest data
  - SQL for data storage
  - Streamlit or Flask for web application

- Minimum viable product: 
  - Baseline forecasting model output and basic pipeline infrastructure overview
