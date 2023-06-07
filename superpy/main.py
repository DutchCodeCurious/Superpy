import argparse
from buy import bought
from sell import update_sell_data
from maintenance import expire_check
import info as i
import graph as gp
from convert import convert_csv
import create_file as cf
import date as d


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inventory Management System')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Create the 'bought' subparser
    bought_parser = subparsers.add_parser(
        'bought', help='Add a product to inventory')
    bought_parser.add_argument('product_name', help='Name of the product')
    bought_parser.add_argument(
        'count', type=int, help='Number of items bought')
    bought_parser.add_argument(
        'buy_price', type=float, help='Price at which the items were bought')
    bought_parser.add_argument(
        'expire_date', type=str,
        help='Date when the items expire (YYYY-MM-DD)')
    bought_parser.add_argument(
        '-bd', '--buy_date', type=str, default=None,
        help='Date when the items were bought (YYYY-MM-DD)')

    # Create the 'update_sell_data' subparser
    sold_parser = subparsers.add_parser(
        'sold', help='Update the sales data of a product')
    sold_parser.add_argument(
        'product_name', help='Name of the product')
    sold_parser.add_argument(
        'sell_price', type=float, help='Price at which the items were sold')
    sold_parser.add_argument(
        'sold_stock', type=int, help='Number of items sold')
    sold_parser.add_argument(
        '--sell_date', type=str, default=None,
        help='Date when the items were sold (YYYY-MM-DD)')

    # Create the 'bought_data_by_date' subparser
    bought_date_data = subparsers.add_parser(
        'bought_by_date', help='Shows stock by chosen dates')
    bought_date_data.add_argument('date1', type=str, help='Start date')
    bought_date_data.add_argument('date2', type=str, help='End date')

    # Create the 'sold_data_by_date' subparser
    sold_date_data = subparsers.add_parser(
        'sold_by_date', help='Shows sold data by chosen dates')
    sold_date_data.add_argument('date1', type=str, help='Start date')
    sold_date_data.add_argument('date2', type=str, help='End date')

    # Create the 'show_revenue_by_date' subparser
    revenue_by_date = subparsers.add_parser(
        'revenue_by_date', help='Shows revenue by chosen dates')
    revenue_by_date.add_argument('date1', help='Start date')
    revenue_by_date.add_argument('date2', help='End date')
    revenue_by_date.add_argument(
        '-f', '--file', help='If Some text after file, a file will be made')

    # Create the 'convert_csv' subparser
    convert_parser = subparsers.add_parser(
        'convert', help='convert csv file to exel or json file')
    convert_parser.add_argument('input_file', help='File to be convert')
    convert_parser.add_argument(
        'output_file', help='Name of new file')
    convert_parser.add_argument(
        'output_format', help='Choose between json or exel')

    # Create the 'sold_file_create' & 'bought_file_create' subparser
    subparsers.add_parser(
        'create_sold', help='Creates the sold.csv in current directory')
    subparsers.add_parser(
        'create_bought', help='Creates the bought.csv in curent directory')

    # Create the 'show_profit' subparser
    profit_parser = subparsers.add_parser('profit', help='Shows total profit')
    profit_parser.add_argument(
        '-f', '--file', default=None,
        help='If Some text after file, a file will be made')

    # Create the 'show_sold_data' subparser
    subparsers.add_parser('sold_data', help='Shows sold data')

    # Create the 'show_stock_data' subparser
    stock_parser = subparsers.add_parser(
        'stock_data', help='Shows data of the stock')
    stock_parser.add_argument(
        '-f', '--file', default=None,
        help='If something here, a file of stock will be made')

    # Create the 'show_revenue' subparser
    revenue_parser = subparsers.add_parser(
        'show_revenue', help='Shows revenue')
    revenue_parser.add_argument(
        '-f', '--file', default=None,
        help='If Some text after file, a file will be made')

    # Create the 'expire_check' subparser
    subparsers.add_parser(
        'expire_check',
        help='checks if items are expired and moves item to sold')

    # Create the 'show_value_stock' subparser
    subparsers.add_parser('value_stock', help='Shows value of stock')

    # Creat the 'graph' subparser
    subparsers.add_parser('stock_graph', help="Shows stock in a bar graph")
    subparsers.add_parser('sold_graph', help="Shows sold stock in a bar graph")

    # Creat the 'date' subparser
    subparsers.add_parser('get_date', help='Gets the date stored in date.txt')
    date_parser = subparsers.add_parser(
        "set_date", help='Sets date in date.txt')
    date_parser.add_argument('--date', default=None,
                             help='Set date, default is today')
    adv_parser = subparsers.add_parser(
        "advance_date", help="Advance date by number of given days")
    adv_parser.add_argument(
        'num', help="Number of days wanted to advance", type=int)

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()

    if args.command == 'bought':
        bought(args.product_name, args.count, args.buy_price,
               args.expire_date, args.buy_date)
    elif args.command == 'sold':
        update_sell_data(args.product_name, args.sell_price,
                         args.sold_stock, args.sell_date)
    elif args.command == 'sold_data':
        i.show_sold_data()
    elif args.command == 'stock_data':
        i.show_stock_data(args.file)
    elif args.command == 'expire_check':
        expire_check()
    elif args.command == 'value_stock':
        print(i.show_value_stock())
    elif args.command == 'bought_by_date':
        i.bought_data_by_date(args.date1, args.date2)
    elif args.command == 'sold_by_date':
        i.sold_data_by_date(args.date1, args.date2)
    elif args.command == 'show_revenue':
        i.show_revenue(args.file)
    elif args.command == 'profit':
        i.show_profit(args.file)
    elif args.command == 'revenue_by_date':
        i.revenue_by_date(args.date1, args.date2, args.file)
    elif args.command == 'stock_graph':
        gp.graph_stock()
    elif args.command == 'sold_graph':
        gp.graph_sold()
    elif args.command == 'convert':
        convert_csv(args.input_file, args.output_file, args.output_format)
    elif args.command == 'create_sold':
        cf.sold_file_create()
    elif args.command == 'create_bought':
        cf.bought_file_create()
    elif args.command == 'get_date':
        print(d.get_date())
    elif args.command == 'set_date':
        d.set_date(args.date)
    elif args.command == 'advance_date':
        d.advance_date(args.num)
