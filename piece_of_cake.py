def get_recipe_price(prices, optionals=None, **ingredients):

    if not prices:
        return "try again"

    if not optionals:
        optionals = []

    shopping_cart = 0
    for price in prices:
        if price not in optionals:
            num_for_mul = ingredients[price] / 100
            shopping_cart = shopping_cart + int(prices[price]) * num_for_mul

    return shopping_cart


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
