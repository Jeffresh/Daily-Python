# Task
#
# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi
# amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money Raghu earned.
from collections import Counter

if __name__ == '__main__':
    shoe_number = int(input())
    shoes_size = list(map(int, input().split()))
    customer_number = int(input())

    counter_shoes = Counter(shoes_size)
    earning = 0
    for _ in range(customer_number):
        size, cost = map(int, input().split())
        if size in counter_shoes and counter_shoes[size]:
            earning += cost
            counter_shoes[size] -= 1

    print(earning)
