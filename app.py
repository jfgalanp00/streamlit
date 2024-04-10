import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
    np.random.rand(1000, 2) / [50,50] + [42.345266829697074, -3.695264647515759],
    columns= ['lat','lon']
)

st.map(map_data)