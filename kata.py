def func_wardrobe():
#  50a + 75b + 100c + 120d = 250
# # 120 not possible
#  25(2a + 3b + 4c) = 250
#  2a + 3b + 4c = 10
#  2(a + 2c) + 3b = 10
# 3b --> even and 3b<10 --> b = 0, 2
# if b = 0
#   a + 2c = 5
#   a,c = (5, 0), (3, 1), (1, 2)
#  ((5,0, 0), (3, 0, 1), (1, 0, 2)
# if b = 2
#   a + 2c = 2
#   a,c = 0, 1   a,c = 2,0
# (0, 2, 1), (2, 2, 0)
# 
    possibilities = [(5,0, 0), (3, 0, 1), (1, 0, 2), (0, 2, 1), (2, 2, 0)]
    out = []
    for p in possibilities:
        a = [50]*p[0]
        b = [75]*p[1]
        c = [100]*p[2]
        out.append(a+b+c)
    return out

def return_cheapest():
    options = func_wardrobe()
    prices = {50: 59, 75: 62, 100: 90, 120: 111}
    cheapest_price = 500
    cheapest_option = None
    for i in options:
        price = 0
        for element in i:
            price = price + prices[element]
        if price < cheapest_price:
            cheapest_price = price
            cheapest_option = i
    return cheapest_option, cheapest_price


def fizzbuzz(n):
    if n%15 == 0:
        return "FizzBuzz"
    if n%3 == 0:
        return "Fizz"
    if n%5 == 0:
        return "Buzz"
    return n

# if __name__ == "__main__":
#     print(func_wardrobe())
#     print(return_cheapest())