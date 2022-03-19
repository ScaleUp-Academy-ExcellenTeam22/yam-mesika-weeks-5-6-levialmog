def get_recipe_price(prices=None, optionals=None, **ingredients):
    if optionals is None:
        optionals = []
    if prices is None:
        prices = {}

    shopping_cart = 0
    for price in prices:
        if price not in optionals:
            num_for_mul = ingredients[price]/100
            shopping_cart = shopping_cart + int(prices[price])*num_for_mul
    print(int(shopping_cart))


get_recipe_price({})
