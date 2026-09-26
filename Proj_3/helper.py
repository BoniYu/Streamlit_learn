import nba_api.stats.endpoints
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

pd.set_option('display.max_columns', None)  # so nothing gets truncated

stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season="2022-23",
    per_mode_detailed='PerGame'
)
df = stats.get_data_frames()[0]

print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nDtypes:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())