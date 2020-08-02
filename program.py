import os
import csv
try:
    import statistics
except:
    import python2_statistics as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------------')
    print('  REAL ESTATE DATA MINING APP  ')
    print('-------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'Sacramentorealestatetransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    # sort data by price (in place)
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house
    high_price = data[-1]
    print("Most expensive: ${:,}, beds: {}, baths: {}".format(
        high_price.price, high_price.beds, high_price.baths))

    # least expensive house
    low_price = data[0]
    print("Least expensive: ${:,}, beds: {}, baths: {}".format(
        low_price.price, low_price.beds, low_price.baths))

    # average house price
    average_price = statistics.mean([p.price for p in data])
    print("Average price: ${:,}".format(int(average_price)))

    # average two (2) bdrm house price
    two_bdrm = (p for p in data
                if announce(p, '2-bdrm, found {}'.format(p.beds)) and p.beds == 2
                )

    homes = []
    for h in two_bdrm:
        if (len(homes) > 5):
            break
        homes.append(h)

    average_price_two_bdrm = statistics.mean(
        (announce(p.price, 'price') for p in homes))
    average_baths_two_bdrm = statistics.mean((p.baths for p in homes))
    average_sqft_two_bdrm = statistics.mean((p.sq__ft for p in homes))
    print("Average price (2-bdrm): ${:,}, baths: {}, sq ft: {}".format(
        int(average_price_two_bdrm),
        round(average_baths_two_bdrm, 1),
        round(average_sqft_two_bdrm, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
