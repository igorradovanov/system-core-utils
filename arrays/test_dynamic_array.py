from dynamic_array import DynamicArray


def test_get():
    # Test case 1: Get element at index 2
    arr = DynamicArray(5)
    arr.pushback(1)
    arr.pushback(2)
    arr.pushback(3)
    assert arr.get(2) == 3

    # Test case 2: Get element at index 5 (out of range)
    assert arr.get(5) == -1

    print("All test cases pass")


test_get()


def test_set():
    # Test case 1: Set element at index 1
    arr = DynamicArray(5)
    arr.pushback(1)
    arr.pushback(2)
    arr.pushback(3)
    arr.set(1, 5)
    assert arr.get(1) == 5

    # Test case 2: Set element at index 5 (out of range)
    arr.set(5, 10)  # Should not modify the array

    print("All test cases pass")


test_set()


def test_pushback():
    # Test case 1: Push back element 10
    arr = DynamicArray(5)
    arr.pushback(1)
    arr.pushback(2)
    arr.pushback(3)
    arr.pushback(10)
    assert arr.get(3) == 10

    # Test case 2: Push back element 20 (resize)
    arr.pushback(20)
    arr.pushback(40)
    assert arr.getCapacity() == 10
    print("All test cases pass")


test_pushback()


def test_popback():
    # Test case 1: Pop back element from non-empty array
    arr = DynamicArray(5)
    arr.pushback(1)
    arr.pushback(2)
    arr.pushback(3)
    assert arr.popback() == 3
    assert arr.getSize() == 2

    # Test case 2: Pop back element from empty array
    arr = DynamicArray(5)
    try:
        arr.popback()
    except IndexError:
        print("Pop back from empty array raises IndexError")


test_popback()
