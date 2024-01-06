from static_array import StaticArray

s_array = StaticArray()

def test_insertEnd():
    # Test case 1: Inserting an element into an empty array
    arr = [None] * 5
    length = 0
    capacity = 5
    s_array.insertEnd(arr, 10, length, capacity)
    assert arr == [10, None, None, None, None]

    # Test case 2: Inserting an element into a partially filled array
    arr = [1, 2, 3, None, None]
    length = 3
    capacity = 5
    s_array.insertEnd(arr, 4, length, capacity)
    assert arr == [1, 2, 3, 4, None]

    # Test case 3: Inserting an element into a full array
    arr = [1, 2, 3, 4, 5]
    length = 5
    capacity = 5
    s_array.insertEnd(arr, 6, length, capacity)
    assert arr == [1, 2, 3, 4, 5]  # The array should remain unchanged

    print("All test cases pass")

test_insertEnd()

def test_removeEnd():
    # Test case 1: Removing an element from an empty array
    arr = [None] * 5
    length = 0
    s_array.removeEnd(arr, length)
    assert arr == [None, None, None, None, None]

    # Test case 2: Removing an element from a partially filled array
    arr = [1, 2, 3, None, None]
    length = 3
    s_array.removeEnd(arr, length)
    assert arr == [1, 2, 0, None, None]

    # Test case 3: Removing an element from a full array
    arr = [1, 2, 3, 4, 5]
    length = 5
    s_array.removeEnd(arr, length)
    assert arr == [1, 2, 3, 4, 0]

    # Test case 4: Removing an element from an array with length 1
    arr = [10]
    length = 1
    s_array.removeEnd(arr, length)
    assert arr == [0]

    print("All test cases pass")


def test_insertMiddle():
    # Test case 1: Inserting an element into an empty array
    arr = [None] * 5
    length = 0
    s_array.insertMiddle(arr, 0, 10, length)
    assert arr == [10, None, None, None, None]

    # Test case 2: Inserting an element into the middle of a partially filled array
    arr = [1, 2, None, None, None]
    length = 2
    s_array.insertMiddle(arr, 1, 3, length)
    assert arr == [1, 3, 2, None, None]

    print("All test cases pass")

test_insertMiddle()

def test_removeMiddle():
    # Test case 1: Removing the middle element from an array with odd length
    arr = [1, 2, 3, 4, 5]
    length = 5
    s_array.removeMiddle(arr, 2, length)
    assert arr == [1, 2, 4, 5, 5]

    # Test case 2: Removing the middle element from an array with even length
    arr = [1, 2, 3, 4]
    length = 4
    s_array.removeMiddle(arr, 1, length)
    assert arr == [1, 3, 4, 4]

    print("All test cases pass")

test_removeMiddle()