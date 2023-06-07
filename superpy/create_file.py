import csv
import os

parent_dir = os.getcwd()
bought = os.path.join(parent_dir, "bought.csv")
sold = os.path.join(parent_dir, "sold.csv")


# Create the file sold.csv
def sold_file_create():
    fieldnames = ['product_name', 'quantity', "buy_price", 'expire_date',
                  'id', 'buy_date', 'sell_price',  'sell_date',
                  'expired', 'sold_id']

    if not os.path.exists(sold):
        with open(sold, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fieldnames)
    else:
        print("File 'sold' exists.")


# Create the file bought.csv
def bought_file_create():
    fieldnames = ['product_name', 'quantity',
                  "buy_price", 'expire_date', 'id', 'buy_date']

    if not os.path.exists(bought):
        with open(bought, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fieldnames)
    else:
        print("File 'bought' exists.")
