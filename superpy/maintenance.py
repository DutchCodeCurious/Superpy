from datetime import datetime as dt
from datetime import date
import pandas as pd
import uuid
import numpy as np


current_date = date.today()
present = dt.now()


# Checks expire dates
def expire_check():
    df_bought = pd.read_csv("bought.csv")
    df = df_bought[(pd.to_datetime(df_bought['expire_date']) < present)]
    key = df['id'].tolist()
    if key == 1:
        remove_by_id(key)
    if len(key) > 1:
        for i in key:
            remove_by_id(i)
            print("Product expired")
    else:
        print("No expired product")


# Check expired dates
def remove_by_id(id):
    df_bought = pd.read_csv("bought.csv")
    data = df_bought.loc[df_bought["id"] == id]
    data = pd.DataFrame(data)
    data["sell_price"] = np.nan
    data["sell_date"] = np.nan
    data["sold_id"] = uuid.uuid4()
    data["expired"] = True
    data = pd.DataFrame(data)
    data.to_csv("sold.csv", mode="a", index=False, header=False)
    df = pd.DataFrame(df_bought)
    df.drop(df.loc[df.id == id].index, inplace=True)
    df.to_csv('bought.csv', index=False)
    print("Removed by id, date expired")


# Check if input is a date
def check_if_date(target):
    t = dt.strptime(target, "%Y-%m-%d")
    if not isinstance(t, date):
        raise TypeError(f"{target} is not a valid date.")
