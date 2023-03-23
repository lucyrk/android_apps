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
        
# counting number of apps in each category, avg price, avg rating
app_category_price_rating = apps[['Category', 'Rating', 'Price']]
app_category_price_rating.groupby('Category').agg('mean')
app_category_count = apps[['Category', 'App']].groupby('Category').count()
app_category_info = app_category_price_rating.merge(app_category_count, on='Category')

#renaming columns and resetting index
app_category_info = app_category_info.rename(columns={'App': 'Number of apps', 'Rating': 'Average rating', 'Price': 'Average price'})
app_category_info = app_category_info.reset_index()

#finding free finance apps
free_finance_apps = apps.loc[(apps['Category']=='FINANCE') & (apps['Price'] == 0)]

# reading user_reviews file
user_reviews = pd.read_csv(r'C:\Users\Lucy Kelly\Code Practice\Android App Project\user_reviews.csv')

#merging user reviews with free finance apps
merged_df = free_finance_apps.merge(user_reviews, on='App')
finance_sentiment_score = merged_df[['App', 'Sentiment Score']]
finance_sentiment_score = finance_sentiment_score.groupby('App').mean().reset_index()

top_10_user_feedback = finance_sentiment_score.sort_values('Sentiment Score', ascending=False)
