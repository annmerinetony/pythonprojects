products = [
    {"p_id": 100, "p_name": "a52s", "brand": "samsung", "band": "5g", "price": 37000},
    {"p_id": 101, "p_name": "a55", "brand": "samsung", "band": "5g", "price": 32000},
    {"p_id": 102, "p_name": "iphone12", "brand": "apple", "band": "4g", "price": 67000},
    {"p_id": 103, "p_name": "iphone13", "brand": "apple", "band": "4g", "price": 87000},
    {"p_id": 104, "p_name": "mi11i", "brand": "mi", "band": "5g", "price": 21000},
    {"p_id": 105, "p_name": "redminote10", "brand": "mi", "band": "4g", "price": 17000},
    {"p_id": 106, "p_name": "redmi1opro", "brand": "mi", "band": "4g", "price": 20000},
    {"p_id": 107, "p_name": "motoedge", "brand": "motorola", "band": "5g", "price": 27000},
    {"p_id": 108, "p_name": "motofusion", "brand": "motorola", "band": "5g", "price": 30000},
]
# mob in range 15000-20000
mobile_filter=[mob for mob in products if mob["price"] in range(15000,20001)]
print(mobile_filter)
# mob with band=5g
mobile_filter=[mob["p_name"] for mob in products if mob["band"]=="5g"]
print(mobile_filter)

# price in descending order
products.sort(key=lambda mob:mob["price"],reverse=True)
print(products)
# costly mobile
costly_mobile=max( products,key=lambda m:m["price"])
print(costly_mobile)
cheapest_mobile=min( products,key=lambda m:m["price"])
print(cheapest_mobile)


