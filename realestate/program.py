import csv
import os.path
import statistics

from data_type import purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)
    query_my(data)


def print_header():
    print("--------------------------------------------------------")
    print("                    Real Estate Data Mining")
    print("--------------------------------------------------------")


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        purchases = []
        for row in reader:
            p = purchase.create_dict(row)
            purchases.append(p)
        return purchases
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(type(row),row)


# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         # read the first line in given file
#         header = fin.readline()
#         print(f'found header: {header}')
#
#         # To store all the remaining line
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])

# def get_price(p):
#     return p.price


def query_data(data):  #: list[purchase]):
    # if data was sorted by price
    data.sort(key=lambda p: p.price)
    # most expensive house?
    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))
    # least expensive house?
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))
    # average price house?
    # ----------------------
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    # avg_price = statistics.mean(prices)
    # -------------------------------

    price = [
        p.price
        for p in data
    ]
    avg_price = statistics.mean(price)
    print("The average home price is ${:,}".format(int(avg_price)))
    # average price of 2 bedroom houses
    # ---------------------
    # prices = []
    # for pur in data:
    #     if(pur.beds == 2):
    #         prices.append(pur.price)
    # ------------------------------------
    two_bedroom = [
        p
        for p in data
        if announce(p, f'2-bedroom, found {p.beds}') and p.beds == 2
    ]
    two_bed_homes = (
        p
        for p in data
        if announce(p, f'2-bedroom, found {p.beds}') and p.beds == 2
    )
    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break;
        homes.append(h)

    avg_price = statistics.mean([announce(p.price, 'price') for p in homes])
    avg_baths = statistics.mean((p.baths for p in homes))
    print("The average price of two bed room is ${:,}  {} baths".format(int(avg_price), int(avg_baths)))


def announce(item, msg):
    print(f"PUlling item {item} for {msg}")
    return item


def query_my(data):
    # find all the house that have 3 bedroom
    three_bedroom = (
        tx
        for tx in data
        if tx.beds == 3
    )
    for p in three_bedroom:
        print(p.price, "has three bedroom")
    # find all the house that for sale
    # find all the house that near to me


if __name__ == '__main__':
    main()
