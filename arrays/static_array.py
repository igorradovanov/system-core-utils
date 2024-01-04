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

def removeEnd(arr, length):
    """
    Removes the element at the end of the array and updates the length.

    Args:
        arr (list): The array from which the element needs to be removed.
        length (int): The current length of the array.

    Returns:
        None
    """
    if length > 0:
        # Overwrite value and decrease the length
        arr[length - 1] = 0

def insertMiddle(arr, i, n, length):
    """
    Inserts an element at the middle index of the array and shifts the remaining elements to the right.

    Args:
        arr (list): The input array.
        i (int): The index at which the element needs to be inserted.
        n: The element to be inserted.
        length (int): The length of the array.

    Returns:
        None
    """
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n

def removeMiddle(arr, i, length):
    """
    Removes the element at the middle index of the array and shifts the remaining elements to the left.

    Args:
        arr (list): The input array.
        i (int): The index of the middle element to be removed.
        length (int): The length of the array.

    Returns:
        None
    """
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]