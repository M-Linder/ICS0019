# -*- coding: utf-8 -*-
# This is not example for writing homework tests!

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

# this test fails!
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
