# Task
#
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

from collections import OrderedDict

if __name__ == '__main__':
    consumer_list_size = int(input())
    consumer_dict = OrderedDict()
    for _ in range(consumer_list_size):
        item, space, price = input().rpartition(' ')
        consumer_dict[item] = consumer_dict.get(item, 0) + int(price)
    print(*[" ".join([item, str(price)]) for item, price in consumer_dict.items()], sep="\n")
