import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('india.csv')

st.set_page_config(layout='wide',page_title="India Primary Parameter Analysis")

listOfStates = df['State'].unique().tolist()
listOfStates.insert(0,'Overall India')

st.sidebar.title("India ka Data Viz")

selectedStates = st.sidebar.selectbox("Select a state",listOfStates)
primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represent primary parameter")
    st.text("Color represent secondary parameter")

    if selectedStates == 'Overall India':
        # plot for india

        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=5,size=primary,
                                color=secondary,mapbox_style='carto-positron',width=1200, height=600,
                                hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    else:
        #plot for state
       stateDf = df[df['State'] == selectedStates]

       fig = px.scatter_mapbox(stateDf, lat='Latitude', lon='Longitude', zoom=5, size=primary,
                               color=secondary, mapbox_style='carto-positron', width=1200, height=600,
                               hover_name='District')
       st.plotly_chart(fig, use_container_width=True)