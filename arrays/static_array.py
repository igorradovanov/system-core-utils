def insertEnd(arr, n, length, capacity):
    """
    Inserts an element at the end of the array.

    Args:
        arr (list): The array to insert the element into.
        n: The element to be inserted.
        length (int): The current length of the array.
        capacity (int): The maximum capacity of the array.

    Returns:
        None
    """
    if length < capacity:
        arr[length] = n