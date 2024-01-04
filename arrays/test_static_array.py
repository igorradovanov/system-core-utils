from static_array import insertEnd, removeEnd, removeMiddle

def test_insertEnd():
    # Test case 1: Inserting an element into an empty array
    arr = [None] * 5
    length = 0
    capacity = 5
    insertEnd(arr, 10, length, capacity)
    assert arr == [10, None, None, None, None]

    # Test case 2: Inserting an element into a partially filled array
    arr = [1, 2, 3, None, None]
    length = 3
    capacity = 5
    insertEnd(arr, 4, length, capacity)
    assert arr == [1, 2, 3, 4, None]

    # Test case 3: Inserting an element into a full array
    arr = [1, 2, 3, 4, 5]
    length = 5
    capacity = 5
    insertEnd(arr, 6, length, capacity)
    assert arr == [1, 2, 3, 4, 5]  # The array should remain unchanged

    print("All test cases passed!")

test_insertEnd()

def test_removeEnd():
    # Test case 1: Removing an element from an empty array
    arr = [None] * 5
    length = 0
    removeEnd(arr, length)
    assert arr == [None, None, None, None, None]

    # Test case 2: Removing an element from a partially filled array
    arr = [1, 2, 3, None, None]
    length = 3
    removeEnd(arr, length)
    assert arr == [1, 2, None, None, None]

    # Test case 3: Removing an element from a full array
    arr = [1, 2, 3, 4, 5]
    length = 5
    removeEnd(arr, length)
    assert arr == [1, 2, 3, 4, 0]

    # Test case 4: Removing an element from an array with length 1
    arr = [10]
    length = 1
    removeEnd(arr, length)
    assert arr == [0]

    print("All test cases passed!")

test_removeEnd()