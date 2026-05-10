import pandas as pd

df = pd.read_json("data/events/7298.json")
print(df.head())
print(df.columns)

# TODO: updates
# want if event name includes either WFC, LFC, or Women's then keep in the data else want to delete the data files 
# to look for: passes, shots, players name, locations(x, y)