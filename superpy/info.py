import pandas as pd
from datetime import datetime as dt
from datetime import date
from maintenance import check_if_date


df_bought = pd.read_csv("bought.csv")
df_sold = pd.read_csv("sold.csv")


def show_sold_data():
    data = pd.read_csv("sold.csv")
    print(data[["product_name", "quantity", "buy_price",
          "sell_price", "sell_date", "expired"]])


def show_stock_data(prompt=None):
    data = pd.read_csv("bought.csv")
    data[["product_name", "quantity", "buy_price",
          "expire_date", "buy_date"]]

    if prompt is not None:
        n_data = data[["product_name", "quantity", "buy_price",
                       "expire_date", "buy_date"]]
        df = pd.DataFrame(n_data)
        df.to_csv('stock.csv', index=False)
    else:
        print(data[["product_name", "quantity", "buy_price",
                    "expire_date", "buy_date"]])


def bought_data_by_date(date1, date2):

    check_if_date(date1)
    check_if_date(date2)

    df_bought["buy_date"] = pd.to_datetime(df_bought["buy_date"])
    mask = (df_bought['buy_date'] > date1) & (df_bought['buy_date'] <= date2)
    if df_bought.loc[mask].empty:
        raise ValueError(f"No data for dates: {date1}, {date2}")
    print(df_bought.loc[mask])


def sold_data_by_date(date1, date2):

    check_if_date(date1)
    check_if_date(date2)

    df_sold["sell_date"] = pd.to_datetime(df_sold["sell_date"])
    mask = (df_sold['sell_date'] > date1) & (df_sold['sell_date'] <= date2)
    if df_sold.loc[mask].empty:
        raise ValueError(f"No data for dates: {date1}, {date2}")
    else:
        data = df_sold.loc[mask]
        print(data[["product_name", "quantity", "buy_price",
              "sell_price", "buy_date", "sell_date"]])


def show_value_stock():
    df = pd.DataFrame(df_bought)
    stock_value = df.quantity * df.buy_price

    df["stock_value"] = stock_value
    df.loc["Total"] = df["stock_value"].sum(numeric_only=True, axis=0)
    df.loc["Total", "product_name"] = ""
    df.loc["Total", "quantity"] = ""
    df.loc["Total", "buy_price"] = ""

    return df[["product_name", "quantity", "buy_price", "stock_value"]]


def show_revenue(file, data=df_sold):
    df = pd.DataFrame(data)
    revenue = (df.quantity * df.sell_price)

    df["revenue"] = revenue
    df.loc[df.expired is True, "revenue"] = (
        (df.quantity * df.buy_price) * -1)
    df.loc["Total"] = df["revenue"].sum(numeric_only=True, axis=0)
    df.loc["Total", "product_name"] = ""
    df.loc["Total", "quantity"] = ""
    df.loc["Total", "sell_price"] = ""

    if file is not None:
        data = df[["product_name", "quantity", "sell_price", "revenue"]]
        df = pd.DataFrame(data)
        df.to_csv('revenue.csv', index=False)
    else:
        print(df[["product_name", "quantity", "sell_price", "revenue"]])


def show_profit(file, data=df_sold):
    df = pd.DataFrame(data)
    profit = (df.quantity * df.sell_price) - (df.quantity * df.buy_price)

    df["profit"] = profit
    df.loc[df.expired is True, "profit"] = (
        (df.quantity * df.buy_price) * -1)
    df.loc["profit"] = df["profit"].sum(numeric_only=True, axis=0)
    df.loc["profit", "product_name"] = ""
    df.loc["profit", "quantity"] = ""
    df.loc["profit", "sell_price"] = ""
    df.loc["profit", "buy_price"] = ""

    if file is not None:
        data = df[["product_name", "quantity",
                   "sell_price", "buy_price", "profit"]]
        df = pd.DataFrame(data)
        df.to_csv('profit.csv', index=False)
    else:
        print(df[["product_name", "quantity", "sell_price", "buy_price",
                  "profit"]])


def revenue_by_date(date1, date2, prompt):

    check_if_date(date1)
    check_if_date(date2)

    df_sold["sell_date"] = pd.to_datetime(df_sold["sell_date"])
    mask = (df_sold['sell_date'] > date1) & (df_sold['sell_date'] <= date2)
    if df_sold.loc[mask].empty:
        raise ValueError(f"No data for dates: {date1}, {date2}")

    data = df_sold.loc[mask]
    df = pd.DataFrame(data)
    revenue = (df.quantity * df.sell_price)
    df["revenue"] = revenue
    df.loc[df.expired is True, "revenue"] = (
        (df.quantity * df.buy_price) * -1)
    df.loc["Total"] = df["revenue"].sum(numeric_only=True, axis=0)
    df.loc["Total", "product_name"] = ""
    df.loc["Total", "quantity"] = ""
    df.loc["Total", "sell_price"] = ""

    if prompt is not None:
        df.to_csv('revenue_by_date.csv', index=False)
    else:
        print(df[["product_name", "quantity", "sell_price", "revenue"]])


def profit_by_name(date1, date2):

    check_if_date(date1)
    check_if_date(date2)

    data = sold_data_by_date(date1, date2)
    show_profit(data)


def show_data_by_name(product_name):
    print(df_bought.loc[df_bought["product_name"] == product_name])
