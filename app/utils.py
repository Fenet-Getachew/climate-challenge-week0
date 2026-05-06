import streamlit as st
import pandas as pd
import glob
import os

@st.cache_data
def load_all_data():
    """
    Loads all cleaned CSVs from the data directory and combines them.
    """
    path = "data/" # Adjust path if necessary
    all_files = glob.glob(os.path.join(path, "*_clean.csv"))
    
    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename)
        # Extract country name from filename (e.g., 'ethiopia_clean.csv' -> 'Ethiopia')
        country_name = os.path.basename(filename).split('_')[0].capitalize()
        df['Country'] = country_name
        df_list.append(df)
    
    master_df = pd.concat(df_list, ignore_index=True)
    master_df['Date'] = pd.to_datetime(master_df['Date'])
    master_df['Year'] = master_df['Date'].dt.year
    return master_df