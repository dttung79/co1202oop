from product import Product

def test_constructor_and_getters():
    p = Product("Pen", 3.0, 5)
    assert p.name == "Pen"
    assert p.price == 3.0
    assert p.quantity == 5

def test_set_price_01():
    p = Product("Pen", 3.0, 5)
    p.price = 4.0
    assert p.price == 4.0

def test_set_quantity_01():
    p = Product("Pen", 3.0, 5)
    p.quantity = 6
    assert p.quantity == 6

def test_set_name_01():
    p = Product("Pen", 3.0, 5)
    p.name = "Pencil"
    assert p.name == "Pencil"

def test_set_price_02():
    p = Product('Pen', 3.0, 5)
    try:
        p.price = -1
        assert False    # This should not be executed
    # if exception is raised, the following line will be executed
    except ValueError as e:
        assert str(e) == "Price cannot be negative"

def test_set_quantity_02():
    p = Product('Pen', 3.0, 5)
    try:
        p.quantity = -1
        assert False    # This should not be executed
    # if exception is raised, the following line will be executed
    except ValueError as e:
        assert str(e) == "Quantity cannot be negative"
    
def test_set_name_02():
    p = Product('Pen', 3.0, 5)
    try:
        p.name = ""
        assert False    # This should not be executed
    # if exception is raised, the following line will be executed
    except ValueError as e:
        assert str(e) == "Name cannot be empty"

def test_show(capsys):
    p = Product("Pen", 3.0, 5)
    p.show()
    captured = capsys.readouterr() # capture the output into captured.out
    assert captured.out == "Name: Pen, Price: 3.0, Quantity: 5\n" # check the output