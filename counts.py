def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

def count_upper_case2(message):
    return sum([1 for c in message if c.isupper()])
    
    
    
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case {}".format(count_upper_case("a"))
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("£$%%A^Bc") == 1, "Special characters with 2 upper"


print("All passed")
