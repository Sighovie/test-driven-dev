def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

# a test to check that an item is not in a collection.
def test_not_in(collection, item):
    assert item not in collection, "was not expecting {0} to contain {1}".format(collection,item)

# a test to ensure an item is not in between two other items  

def test_between(value, test_value):
        assert test_value < value and test_value > value ,"expect {0} to be between the lower or upper limits of  {1}".format(test_value,value)

        
#test_are_equal(40, 49)
#test_not_equal("A", "A")
#test_is_in(["Fred","Boy","Garry","Jude", "item"],"Boy")
#test_not_in(["Joe","Grace","Richard","George","Mark"], "Grace")
#test_between(600, 700)