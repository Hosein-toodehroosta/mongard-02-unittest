# Learning assert


shoe = {"name":"Nike", "price": 400}

def apply_discount(product, discount):
    price = product["price"] - discount
    assert 0 <= price <= product["price"] , 'The discount should be between 0 and 100'
    return price


print( apply_discount(shoe, 700) )