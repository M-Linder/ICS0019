# This is not example for writing real tests!
def test_sum(xyz):
    assert sum(xyz) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum([1, 2, 3])
    print("Everything passed")
