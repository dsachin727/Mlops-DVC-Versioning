import pandas as pd
import os

data = {'Name': ['Sachin', 'Rahul', 'Saurav', 'McArthy'],
        'Age': [47, 48, 49, 50],
        'Country': ['India', 'India', 'India', 'Australia']}

df = pd.DataFrame(data)

#print(df)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#to make path for data
filepath = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(filepath, index=False)

# # Adding new row to df for V2
new_row_loc = {"Name": "Daren", "Age": 20, "Country": "Germany"}
df.loc[len(df.index)] = new_row_loc

#to update to csv file
df.to_csv(filepath, index=False)