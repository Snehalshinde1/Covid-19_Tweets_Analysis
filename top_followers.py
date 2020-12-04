import pandas as pd
from datetime import datetime


def date_range(sd,ed,f1):
    df = pd.read_csv(f1)
    start_date=sd
    SD=datetime.strptime(start_date,'%m/%d/%Y')
    end_date=ed
    ED=datetime.strptime(end_date,'%m/%d/%Y')
    df['date'] = pd.to_datetime(df['date'])
    after_start_date = df["date"] >= SD
    before_end_date = df["date"] <= ED
    between_two_dates = after_start_date & before_end_date
    filtered_dates = df.loc[between_two_dates]
    return filtered_dates

def top_followers(filtered_dates,num_users):
    df=filtered_dates
    top_followers_count = df.nlargest(num_users, ['user_followers'])
    user_names = top_followers_count['user_name'].tolist()
    user_followers = top_followers_count['user_followers'].tolist()
    return user_names, user_followers









