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
* **Python libraries:** pandas, streamlit, seaborn, matplotlib, numpy
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
    return df

    
playerstats = load_data(selected_year)

# the dataframe is too big, letting people choose which columns to display
all_columns = playerstats.columns.tolist()
# Select only the columns to be displayed in the app
default_cols = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'AGE', 'GP', 'PTS', 'REB', 'AST']
# Sorting through the columns for Teams to display in the sidebar
sorted_unique_team = sorted(playerstats.TEAM_ABBREVIATION.unique())
# Sidebar - Team selection
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
# Filter the data based on selected team and columns
filtered_data = playerstats[playerstats.TEAM_ABBREVIATION.isin(selected_team)][default_cols]
# Display the filtered data in the app
st.dataframe(filtered_data)

# To display current number of players
st.header('Player Stats')
st.write('Number of Players: ' + str(len(filtered_data.index)))

notes = """
TO download a file. It is already in the st.dataframe but if we want a custom download button, we can use this code. It is not used in the current version of the app.

csv = filtered_data.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='nba_player_stats.csv',
    mime='text/csv',
)
"""

# Drawing a heatmap. This is optional
if st.button('Show Heatmap'):
    st.header('Heatmap')
    fig, ax = plt.subplots(figsize=(7, 5))
    corr = filtered_data.corr(numeric_only=True)
    #masking the upper triangle of the heatmap to avoid redundancy
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    st.pyplot(fig)









