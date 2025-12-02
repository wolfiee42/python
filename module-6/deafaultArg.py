import time

def net_price (list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)

# print(net_price(500, 0, 0.05))
# print(net_price(500))

def count (end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(5)