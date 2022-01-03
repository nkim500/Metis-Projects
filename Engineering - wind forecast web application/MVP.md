# Minimum viable product for wind forecast data web application

This project aims to create a dashboard on a web application displaying wind forecast data for select locations. The general architecture representing the flow of data is shown in the chart below:

![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/8cd22af7ed7e8beec9c644c8809024cff8cc371c/07%20Engineering/Flowchart%20-%20weather%20data.drawio.svg)

The web application will perform 2 main functions: 
1. Show wind and other weather forecast items for a location in a map
   - There is metadata on c. 7,000 US stations and using this information, API calls can be made to generate forecast for the next days. 
   - Web app will take the user's queried location and will retrieve forecasts for the location and locations nearby
2. Show which location has been preferrable for kitesurfing historically and the corresponding data
   - For select locations in the US, historical datasets are available which will be used to analyze the seasonality of these locations

