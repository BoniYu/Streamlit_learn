import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import requests
from io import StringIO
from nba_api.stats.endpoints import leaguedashplayerstats

st.title("NBA Player Stats Dashboard")

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit, seaborn, matplotlib, numpy
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2026))))


# Web scraping of NBA player stats
@st.cache_data
def load_data(year):
    season_str = f"{year-1}-{str(year)[2:]}"
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season_str,
        per_mode_detailed='PerGame',
        timeout=60
    )
    df = stats.get_data_frames()[0]
    df = df.fillna(0)
    rank_cols = [c for c in df.columns if c.endswith('_RANK')]
    df = df.drop(columns=rank_cols)
    return df

    
playerstats = load_data(selected_year)

# the dataframe is too big, letting people choose which columns to display
all_columns = playerstats.columns.tolist()
default_cols = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'AGE', 'GP', 'PTS', 'REB', 'AST']
selected_columns = st.sidebar.multiselect('Columns', all_columns, default=default_cols)
st.dataframe(playerstats[selected_columns])





