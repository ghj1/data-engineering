import pandas as pd
import sys
df = pd.read_parquet('yellow_tripdata_2021-07.parquet')
df.to_csv('yellow_tripdata_2021-07.csv')