import pandas as pd
import numpy as np

apps = pd.read_csv(r'C:\Users\Lucy Kelly\Code Practice\Android App Project\apps.csv')
apps = apps.drop_duplicates()
# List of characters to remove
chars_to_remove = ['+', ',', '$']
# List of column names to clean
cols_to_clean = ['Installs', 'Price']

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))
