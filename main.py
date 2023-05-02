import pandas as pd

#save filepath to variable for easier access

melbourne_file_path = "input/melbourne-housing-snapshot/melb_data.csv"

#read the data and store it in the DF titled melbourne_data

melbourne_data = pd.read_csv(melbourne_file_path)