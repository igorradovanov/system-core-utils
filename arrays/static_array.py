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
def removeEnd(arr, length):
    if length > 0:
        #Overwrite value and decrease the length
        arr[length - 1] = 0