#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
import requests
import datetime
from collections import namedtuple
from geopy.geocoders import Nominatim
import altair as alt

    
st.sidebar.markdown("Navigate to:")
choice = st.sidebar.selectbox("", ["Wind forecast","Historical"])

url = "https://raw.githubusercontent.com/nkim500/Metis_Projects/main/07_Engineering/US_stations.csv"
df = pd.read_csv(url)

station_i = namedtuple("station", "usaf wban station_code st_name country state call latitude longitude elevation begin end forecastlink")

stuco = [] 
stations_us = []
idx = 1
for i in range(len(df)):
    stuco.append([str(idx) + " " + str(df["station_code"][i]), df["state"][i], df["call"][i], df["latitude"][i], df["longitude"][i]])
    usaf = df["usaf"][i]
    wban = df["wban"][i]
    station_code = str(idx) + " " + str(df["station_code"][i])
    st_name = df["st_name"][i]
    country = df["country"][i]
    state = df["state"][i]
    call = df["call"][i]
    latitude = df["latitude"][i]
    longitude = df["longitude"][i]
    elevation = df["elevation"][i]
    begin = df["begin"][i]
    end = df["end"][i]
    forecastlink = df["forecast_api_endpoint"][i]
    stations_us.append(station_i(usaf, wban, station_code, st_name, country, state, call, latitude, longitude, elevation, begin, end, forecastlink))
    idx += 1

df_station = pd.DataFrame(stuco, columns=['code', 'state', 'call', 'lat','lon'])

states = alt.topo_feature('https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/us-10m.json', 'states')



if choice == "Wind forecast":
    
    st.title("Find wind in your local area")
    
    col1, col2 = st.columns([0.01,8])

#     with col1:
#         None
    with col2:

        background = alt.Chart(states).mark_geoshape(
            fill='lightgray',
            stroke='white'
        ).properties(
            title=alt.TitleParams('Map of US weather stations', fontSize=24),
            width=2000,
            height=1000
        ).project('albersUsa')

        hover = alt.selection(type='single', on='mouseover', nearest=True,
                              fields=['lat', 'lon'])

        base = alt.Chart(df_station).encode(
            longitude='lon:Q',
            latitude='lat:Q',
        )

        text = base.mark_text(dy=-10, align='right', fontSize=18, ).encode(
            alt.Text('code', type='nominal'),
            opacity=alt.condition(~hover, alt.value(0), alt.value(1))
        )

        points = base.mark_point().encode(
            color=alt.value('steelblue'),
            size=alt.condition(~hover, alt.value(1), alt.value(100))
        ).add_selection(hover)

        background + points + text

        user_input = st.text_input("Input station code", "593 SOUTH")


        def searchstation(user_input):
            for i in stations_us:
                if i.station_code == user_input:
                    return i


        def address_gen(station_i):
            geolocator = Nominatim(user_agent="geoapiExercises")

            location = geolocator.reverse((float(station_i.latitude),float(station_i.longitude)))

            return(str(location))


        def tw_forecast (x):
            api = requests.get(x).json()
            dates_t = []
            dates_wd = []
            dates_ws = []
            output_t = []
            output_wd = []
            output_ws = []

            for i in api['properties']['temperature']['values']:
                date, hour = i['validTime'].split("T")[0], i['validTime'].split("T")[1].split("+")[0]
                dateobject = datetime.datetime.strptime(date + " " + hour, '%Y-%m-%d %H:%M:%S')
                forhowmany = int(i['validTime'].split("T")[2].split("H")[0])
                forecast = round(i['value'],2)

                if forhowmany == 1:
                    dates_t.append(dateobject)
                    output_t.append(forecast)
                else:
                    dates_t.append(dateobject)
                    output_t.append(forecast)
                    while forhowmany > 1:
                        dateobject += datetime.timedelta(hours=1)
                        dates_t.append(dateobject)
                        output_t.append(forecast)
                        forhowmany -= 1

            for i in api['properties']['windDirection']['values']:
                date, hour = i['validTime'].split("T")[0], i['validTime'].split("T")[1].split("+")[0]
                dateobject = datetime.datetime.strptime(date + " " + hour, '%Y-%m-%d %H:%M:%S')
                forhowmany = int(i['validTime'].split("T")[2].split("H")[0])
                forecast = round(i['value'],2)

                if forhowmany == 1:
                    dates_wd.append(dateobject)
                    output_wd.append(forecast)
                else:
                    dates_wd.append(dateobject)
                    output_wd.append(forecast)
                    while forhowmany > 1:
                        dateobject += datetime.timedelta(hours=1)
                        dates_wd.append(dateobject)
                        output_wd.append(forecast)
                        forhowmany -= 1

            for i in api['properties']['windSpeed']['values']:
                date, hour = i['validTime'].split("T")[0], i['validTime'].split("T")[1].split("+")[0]
                dateobject = datetime.datetime.strptime(date + " " + hour, '%Y-%m-%d %H:%M:%S')
                forhowmany = int(i['validTime'].split("T")[2].split("H")[0])
                forecast = round(i['value']/1.852,5)

                if forhowmany == 1:
                    dates_ws.append(dateobject)
                    output_ws.append(forecast)
                else:
                    dates_ws.append(dateobject)
                    output_ws.append(forecast)
                    while forhowmany > 1:
                        dateobject += datetime.timedelta(hours=1)
                        dates_ws.append(dateobject)
                        output_ws.append(forecast)
                        forhowmany -= 1

            return dates_t, dates_ws, dates_wd, output_t, output_ws, output_wd


        def distance_calc(a, b):
            R = 3963
            lat1 = math.radians(float(a.latitude))
            lon1 = math.radians(float(a.longitude))
            lat2 = math.radians(float(b.latitude))
            lon2 = math.radians(float(b.longitude))

            lat_d = lat1 - lat2
            lon_d = lon1 - lon2

            p = math.sin(lat_d / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_d / 2)**2
            c = 2 * math.atan2(math.sqrt(p), math.sqrt(1 - p))

            distance = R * c

            return distance

        def n_neighbors(input_station, n):

            placeholder1 = []
            placeholder2 = []

            for i in stations_us:
                placeholder1.append(i)
                placeholder2.append(distance_calc(input_station,i))

            distances = np.array(placeholder2)
            location_idx = np.argsort(distances)[:n].tolist()

            for i in location_idx:
                try:
                    generate_charts(placeholder1[i])
                except KeyError:
                    print("Forecast not available for the station")

        def generate_charts(station_i):

            if len(station_i.forecastlink) < 2:
                print("Forecast not available for the station")
            else:
                tt, tws, twd, temp, winds, windd = tw_forecast(station_i.forecastlink)
                X = np.arange(0, len(windd))
                Y = np.ones(X.shape[0])*50
                # U = [np.cos(math.radians(i)) for i in windd]
                # V = [np.sin(math.radians(i)) for i in windd]
                U = [np.cos(math.radians(i)) if index % 3 == 0 else 0 for index, i in enumerate(windd)]
                V = [np.sin(math.radians(i)) if index % 3 == 0 else 0 for index, i in enumerate(windd)]
                windscore = sum(1 if tws[idx] >= tws[idx].replace(hour=6) and tws[idx] <= tws[idx].replace(hour=20) and i >= 9 else 0 for idx, i in enumerate(winds))/len(winds)

                fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(20,8), gridspec_kw = {'height_ratios':[3, 3, 1]})
                fig.suptitle(station_i.station_code + "; " + "Wind score: {:.1%}".format(windscore) + "; " + address_gen(station_i), fontsize=16)
                ax1.set_title("Temperature")
                ax1.scatter(tt, temp)
                ax1.set_ylabel("celsius")
                ax1.margins(x=0)
                ax2.set_title("Wind speed")
                ax2.scatter(tws, winds)
                ax2.axhline(y=9, color = 'lightsteelblue')
                ax2.axhline(y=12, color = 'slategrey')
                ax2.set_ylabel("knots")
                ax2.margins(x=0)
                ax3.set_title("Wind direction")
                ax3.quiver(X, Y, U, V, scale_units = 'x', headwidth = 4, headlength = 4, headaxislength=4, width=0.001, scale=0.5, pivot='tail') 
                ax3.get_xaxis().set_visible(False)
                ax3.get_yaxis().set_visible(False)
                ax3.margins(x=0)
                fig.tight_layout(pad=3)
                fig.subplots_adjust(top=0.9, bottom=0.1)
                st.pyplot(fig);

        x = searchstation(user_input)

        n_neighbors(x,5)





if choice == "Historical":
    
    st.title("See historical wind trends for known places to kitesurf in the US")

    call_list = ['KACK','KACY','KBLM','KDLS','KEYW','KFRG','KHSE','KHTO','KJFK','KMIA','KMKG','KOAK','KPIL', 'PHKO']
    alias_list = ['Nantucket, MA', 'Ocean City, NJ', 'Sandy Hook Beach, NJ', 'Hood River, OR', 'Key West, FL', 'Gilgo Beach, NY',\
                  'Cape Hatteras, Outerbanks, NC', 'East Hampton, NY', 'Plumb Beach, Brookyln, NY','Miami Beach, FL', \
                  'Muskegon, MI', 'Crissy Field, San Francisco, CA', 'South Padre Island, TX', 'Kailua Bay, Oahu Island, HI']

    def searchstation_c(option):
        for i in stations_us:
            if i.call == option:
                return address_gen(i)

    alias_dict = dict(zip(call_list, alias_list))

    alias_coord = []

    def coordfind(x):
        for i in stations_us:
            if i.call == x:
                alias_coord.append([i.latitude, i.longitude, i.call, alias_dict[i.call]])
    for i in call_list:
        coordfind(i)

    df_alias = pd.DataFrame(alias_coord, columns=['lat','lon','call', 'alias'])
    df_alias.drop_duplicates(subset=['call'], inplace=True)

    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        title=alt.TitleParams('Well known kitesurfing locations in the US', fontSize=24),
        width=1100,
        height=750
    ).project('albersUsa')


    # Points and text
    hover = alt.selection(type='single', on='mouseover', nearest=True,
                          fields=['lat', 'lon'])

    # selection = alt.selection_interval(bind='scales')

    base = alt.Chart(df_alias).encode(
        longitude='lon:Q',
        latitude='lat:Q',
    )

    text = base.mark_text(dy=-10, align='right', fontSize=18, ).encode(
        alt.Text('alias', type='nominal'),
        opacity=alt.condition(~hover, alt.value(0), alt.value(1))
    )

    points = base.mark_point().encode(
        color=alt.value('steelblue'),
        size=alt.condition(~hover, alt.value(30), alt.value(100))
    ).add_selection(hover)

    background + points + text



    option = st.selectbox("Select a location to see data:",
                          ('Crissy Field, San Francisco, CA', 'Key West, FL', 'Miami Beach, FL', 'Kailua Bay, Oahu Island, HI', 'Nantucket, MA', \
                          'Muskegon, MI', 'Cape Hatteras, Outerbanks, NC', 'Ocean City, NJ', 'Sandy Hook Beach, NJ', 'East Hampton, NY', \
                          'Gilgo Beach, NY', 'Plumb Beach, Brookyln, NY', 'Hood River, OR', 'South Padre Island, TX'))

    if option == 'Crissy Field, San Francisco, CA':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KOAK_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KOAK_mth.svg)")

    elif option == 'Key West, FL':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KEYW_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KEYW_mth.svg)")

    elif option == 'Miami Beach, FL':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KMIA_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KMIA_mth.svg)")

    elif option == 'Kailua Bay, Oahu Island, HI':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/PHKO_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/PHKO_mth.svg)")

    elif option == 'Nantucket, MA':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KACK_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KACK_mth.svg)")

    elif option == 'Muskegon, MI':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KMKG_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KMKG_mth.svg)")

    elif option == 'Cape Hatteras, Outerbanks, NC':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KOAK_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KOAK_mth.svg)")

    elif option == 'Ocean City, NJ':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KACY_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KACY_mth.svg)")

    elif option == 'Sandy Hook Beach, NJ':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KBLM_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KBLM_mth.svg)")

    elif option == 'East Hampton, NY':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KHTO_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KHTO_mth.svg)")

    elif option == 'Gilgo Beach, NY':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KFRG_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KFRG_mth.svg)")

    elif option == 'Plumb Beach, Brookyln, NY':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KJFK_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KJFK_mth.svg)")

    elif option == 'Hood River, OR':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KDLS_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KDLS_mth.svg)")

    elif option == 'South Padre Island, TX':
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KPIL_avg.svg)")
        st.markdown("![image](https://raw.githubusercontent.com/nkim500/Metis_Projects/bf524ff8f46c9b077d171a0060d7f2844f269aeb/07_Engineering/support/KPIL_mth.svg)")

    else:
        st.markdown("Select your location")

