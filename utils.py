import pandas as pd

def load_data():
  data = pd.read_csv('seoul3_real_estate_1000.csv')
  
  return data