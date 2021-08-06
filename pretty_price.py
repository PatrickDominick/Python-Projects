def pretty_price(price, change):
    price = price.split(".")[0]
    change = change.split(".")[1]
    print(f"{price}.{change}")

    pretty_price("3.21", ".99")