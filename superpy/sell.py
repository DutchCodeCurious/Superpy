import datetime as dt
import pandas as pd
import uuid
from maintenance import check_if_date


def show_data_by_name(product_name):
    data = pd.read_csv("bought.csv")
    return data.loc[data["product_name"] == product_name]


def update_sell_data(product_name, sell_price, sold_stock, sell_date=None):

    if not isinstance(product_name, str):
        raise TypeError("Product has to be a string")

    if not isinstance(sell_price, (int, float)):
        raise TypeError("Sell_price has to be a number")

    if not isinstance(sold_stock, int):
        raise TypeError("Sold_stock has to be a whole number")

    if sell_date is None:
        sell_date = dt.date.today()

    check_if_date(sell_date)

    df = pd.read_csv('bought.csv', sep=",")
    df_sold = pd.read_csv('sold.csv')
    id_list = df_sold['id'].tolist()
    product_name = product_name.lower()
    sold_id = df.loc[df["product_name"] == product_name]

    if len(sold_id) > 1:
        print(df.loc[df["product_name"] == product_name])
        id = input("Copy and pass the id from sold product: ")
        sold_id_find = df.loc[df["id"] == id]
        id = sold_id_find.id.item()

    if id == 0:
        id = sold_id.id.item()

# make sold data complete
    sold_data = []
    sold_data = df.loc[df["id"] == id]
# Check if not multiple product_names are used

    sold_data.loc[sold_data.id ==
                  id, 'quantity'] = sold_stock
    sold_data = pd.DataFrame(sold_data)
    sold_data["sell_price"] = sell_price
    sold_data["sell_date"] = sell_date
    sold_data["sold_id"] = uuid.uuid4()
    sold_data["expired"] = False
    sold_data = pd.DataFrame(sold_data)

# Check if product is in stock
    if df.loc[df.id == id].empty:
        raise ValueError("Product not found in the bought data")

# Check if stock is big enough
    if sold_stock > df.loc[df.id == id, 'quantity'].item():
        raise ValueError("To much stock, amount stock not in inventory")

    if (df.loc[df.id == id, 'quantity'].item() - sold_stock) == 0:
        df_drop = pd.DataFrame(df)
        df_drop.drop(df_drop.loc[df_drop.id ==
                     id].index, inplace=True)
        df_drop.to_csv('bought.csv', index=False)
        print("Removed from inventory")


# Check if id from sold product in sold.csv
    elif sold_data.id.item() in id_list:
        data = df_sold.loc[df_sold['id'] == sold_data.id.item()]

        if sell_price == data.sell_price.item():
            df.loc[df.id == sold_data.id.item(), 'quantity'] = (
                df.quantity - sold_stock)
            df_sold.loc[df_sold.id == sold_data.id.item(), 'quantity'] = (
                df_sold.quantity + sold_stock)
            df.to_csv('bought.csv', index=False)
            df_sold.to_csv('sold.csv', index=False)
            print("bought & sold stock are updated")


# Update sold & bought data
    elif sold_data.quantity.item() >= 1:

        df.loc[df.id == id,
               'quantity'] = (df.quantity - sold_stock)
        df.to_csv('bought.csv', index=False)
        sold_data.to_csv('sold.csv', mode='a', index=False, header=False)
        print("sold.csv & bought.csv zijn bijgewerkt")

# Update sold data --- Bought data verwijderen na update?!
    else:

        sold_data.to_csv('sold.csv', mode='a', index=False, header=False)
        print("sold.csv is bijgewerkt")
