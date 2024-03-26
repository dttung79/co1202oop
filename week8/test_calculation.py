from calculation import calculate_shipping_fee

def test_shipping_01():
    weight = -1
    weight_unit = 'Pounds'
    distance = 10
    distance_unit = 'Miles'
    selected_method = 'Standard'
    try:
        total = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert str(e) == 'Weight must be greater than 0'
def test_shipping_02():
    weight = 1
    weight_unit = 'Pounds'
    distance = 10
    distance_unit = 'Miles'
    selected_method = 'Standard'    
    total = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert f'{total:.2f}' == '5.85'