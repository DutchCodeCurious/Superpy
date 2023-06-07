import pandas as pd
import matplotlib.pyplot as plt

b_data = pd.read_csv("bought.csv")
s_data = pd.read_csv("sold.csv")


def graph_stock():
    grouped_data = b_data.groupby('product_name')[
        'quantity'].sum().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(grouped_data['product_name'], grouped_data['quantity'])
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Product Quantity')
    plt.xticks(rotation=45)
    plt.show()


def graph_sold():
    filtered_data = s_data[s_data['expired'] is False]

    grouped_data = filtered_data.groupby('product_name')[
        'quantity'].sum().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(grouped_data['product_name'], grouped_data['quantity'])
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Sold Product Quantity')
    plt.xticks(rotation=45)
    plt.show()
