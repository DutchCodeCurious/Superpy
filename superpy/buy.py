import csv
import datetime as dt
import uuid
import os
import pandas as pd
from maintenance import check_if_date


parent_dir = os.getcwd()
bought = os.path.join(parent_dir, "bought.csv")
current_date = dt.date.today()
df_bought = pd.read_csv("bought.csv")


def bought(product_name, count, buy_price, expire_date, buy_date=None):

    if buy_date is not None:
        check_if_date(buy_date)
    if buy_date is None:
        buy_date = dt.date.today()

    expected_types = {
        product_name: str,
        count: int,
        buy_price: float,
    }

    for param, expected_type in expected_types.items():
        if not isinstance(param, expected_type):
            raise TypeError(
                f"{param} must be of type {expected_type.__name__}.")

    check_if_date(expire_date)

    id = uuid.uuid4()
    product_details = [product_name.lower(),
                       count,
                       buy_price,
                       expire_date,
                       id,
                       buy_date
                       ]

    with open(os.path.join(parent_dir, "bought.csv"), 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(product_details)
        csvfile.close()

    print(f'{product_name} is added!')
