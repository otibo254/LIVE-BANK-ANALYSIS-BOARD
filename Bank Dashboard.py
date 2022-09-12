#Importing dependencies
from logging import PlaceHolder
import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import csv


#Loading the dataset
df = pd.read_csv("C:/Users/stevi/Desktop/BANK LIVE DASHBOARD/bank.csv")

#Setting page configurations
st.set_page_config(
    page_title="Live Dashboard.",
    page_icon="🎇",
    layout="wide"
)
st.caption("Breezie Foundation.")
#Setting page title
st.title("Live Bank Staff Dashboard💫💫.")
st.subheader("Interactively use the board.")
st.success("👈Choose area of specialisation in the sidebar.")


#Creating filters
job_filter = st.sidebar.selectbox("Choose area of specialisation:",pd.unique(df['job']))
st.sidebar.write("occupation:",job_filter)

PlaceHolder = st.empty()

#Filtering job data to a unique selection
df = df[df['job']==job_filter]

for seconds in range(800):
    
    df['age_new'] = df['age'] * np.random.choice(range(1,6))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,6))
    
    #KPI intergrations
    avg_age = np.mean(df['age_new'])
    count_housing = int(df[(df["housing"]=='yes')]['housing'].count() + np.random.choice(range(1,25)))
    balance = np.mean(df['balance_new'])
    
    with PlaceHolder.container():
        KPIA,KPIB,KPIC = st.columns(3)
        KPIA.metric(label="Age🕰️:", value=round(avg_age), delta=round(avg_age) -10)
        KPIB.metric(label="Housing🏬:", value=int(count_housing), delta= -10 + count_housing)
        KPIC.metric(label="Account Balance 💰ksh:", value=f"ksh {round(balance,2)}", delta= - round(balance/count_housing) * 100)
        
        #Creating charts and graphical displays
        graph1,graph2 = st.columns(2)
        with graph1:
            st.markdown(" ###### Heatmap:")
            graph1 = px.density_heatmap(data_frame=df, y='age_new', x='education')
            st.write(graph1)
            
        with graph2:
            st.markdown(" ###### Pie Display:")
            graph2 = px.area(data_frame=df, y='balance',x='duration')
            st.write(graph2)
            
        st.markdown("Tabular Display:")
        st.dataframe(df)
        time.sleep(1)
        
               