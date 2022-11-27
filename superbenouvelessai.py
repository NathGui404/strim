# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:44:54 2022

@author: nguil
"""

import streamlit as st
import pandas as pd
import numpy as np


st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Here we use "magic commands":
df_weather

data = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

# Adding code so we can have map default to the center of the data
midpoint = (np.average(data['lat']), np.average(data['lon']))



