def get_recipe_price(prices=None, optionals=None, **ingredients):

    if prices is not None and ingredients is not None and len(ingredients) == len(prices):
        if optionals is None:
            optionals = []

        shopping_cart = 0
        for price in prices:
            if price not in optionals:
                num_for_mul = ingredients[price]/100
                shopping_cart = shopping_cart + int(prices[price])*num_for_mul
        print(int(shopping_cart))
    else:
        print("Bad input")


get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
